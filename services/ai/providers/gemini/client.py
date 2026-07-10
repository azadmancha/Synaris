from __future__ import annotations

import os
from typing import Any

import httpx

from services.ai.providers.base import AIProvider


def _build_gemini_url(model: str, api_key: str) -> str:
    return f"https://gemini.googleapis.com/v1/models/{model}:generate?key={api_key}"


class GeminiProvider(AIProvider):
    name = "gemini"

    def __init__(self, api_key: str | None = None, model: str | None = None):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY", "")
        if not self.api_key:
            raise ValueError("Gemini API key is required")

        self.model = model or os.getenv("GEMINI_MODEL", "gemini-1.5-mini")

    async def generate_text(self, prompt: str, **kwargs: Any) -> str:
        payload = {
            "prompt": {"text": prompt},
            "temperature": kwargs.get("temperature", 0.3),
            "maxOutputTokens": kwargs.get("max_tokens", 512),
        }

        url = _build_gemini_url(self.model, self.api_key)
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(url, json=payload)
            response.raise_for_status()
            result = response.json()

        candidates = result.get("candidates", [])
        if not candidates:
            raise RuntimeError("Gemini did not return any candidates")

        return candidates[0].get("output", "")

    async def health_check(self) -> bool:
        try:
            url = _build_gemini_url(self.model, self.api_key)
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.options(url)
                return response.status_code == 200
        except Exception:
            return False
