from __future__ import annotations

import os
from typing import Any

import httpx

from services.ai.providers.base import AIProvider

OPENROUTER_API_URL = "https://openrouter.ai/v1/chat/completions"


class OpenRouterProvider(AIProvider):
    name = "openrouter"

    def __init__(self, api_key: str | None = None, model: str | None = None):
        self.api_key = api_key or os.getenv("OPENROUTER_API_KEY", "")
        if not self.api_key:
            raise ValueError("OpenRouter API key is required")

        self.model = model or os.getenv("OPENROUTER_MODEL", "gpt-4o-mini")

    async def generate_text(self, prompt: str, **kwargs: Any) -> str:
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": kwargs.get("max_tokens", 512),
            "temperature": kwargs.get("temperature", 0.3),
        }

        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                OPENROUTER_API_URL,
                json=payload,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self.api_key}",
                },
            )
            response.raise_for_status()
            payload = response.json()

        choices = payload.get("choices", [])
        if not choices:
            raise RuntimeError("OpenRouter response did not include any choices")

        message = choices[0].get("message", {})
        return message.get("content", "")

    async def health_check(self) -> bool:
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.get(
                    "https://openrouter.ai/v1/health",
                    headers={"Authorization": f"Bearer {self.api_key}"},
                )
                return response.status_code == 200
        except Exception:
            return False
