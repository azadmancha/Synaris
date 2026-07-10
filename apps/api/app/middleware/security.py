import asyncio
import time
from collections import defaultdict
from typing import Optional

from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp


class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    """Add security headers to every HTTP response.

    This middleware enforces browser-level protections and prevents common
    cross-site injection issues from being exposed to the client.
    """

    def __init__(self, app: ASGIApp) -> None:
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        response.headers["Strict-Transport-Security"] = "max-age=63072000; includeSubDomains; preload"
        response.headers["Permissions-Policy"] = "geolocation=(), microphone=()"
        return response


class SimpleRateLimitMiddleware(BaseHTTPMiddleware):
    """A lightweight, in-memory rate limiter for early security scaffolding.

    This is not a production-quality distributed rate limiting solution.
    It is intended for version 2 scaffolding and should be replaced with
    Redis or an edge throttling service before horizontal scaling.
    """

    def __init__(self, app: ASGIApp, max_requests: int = 120, window_seconds: int = 60) -> None:
        super().__init__(app)
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self._requests: dict[str, list[float]] = defaultdict(list)
        self._lock = asyncio.Lock()

    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host if request.client else "unknown"
        now = time.time()

        async with self._lock:
            request_times = self._requests[client_ip]
            while request_times and request_times[0] + self.window_seconds <= now:
                request_times.pop(0)
            if len(request_times) >= self.max_requests:
                return JSONResponse(
                    {"detail": "Too many requests, please try again later."},
                    status_code=429,
                )
            request_times.append(now)

        return await call_next(request)
