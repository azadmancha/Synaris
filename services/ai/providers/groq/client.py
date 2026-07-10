from __future__ import annotations

import os
from typing import Any

import httpx

from services.ai.providers.base import AIProvider

GROQ_API_BASE = "https://api.groq.com/v1"


class GroqProvider(AIProvider):
    name = "groq"

    def __init__(self, api_key: str | None = None, model: str | None = None):
        self.api_key = api_key or os.getenv("GROQ_API_KEY", "")
        if not self.api_key:
            raise ValueError("Groq API key is required")

        self.model = model or os.getenv("GROQ_MODEL", "groq-1.5-mini")

    def _build_url(self) -> str:
        return f"{GROQ_API_BASE}/models/{self.model}/completions"

    async def generate_text(self, prompt: str, **kwargs: Any) -> str:
        payload = {
            "prompt": prompt,
            "max_output_tokens": kwargs.get("max_tokens", 512),
            "temperature": kwargs.get("temperature", 0.3),
        }

        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                self._build_url(),
                json=payload,
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json",
                },
            )
            response.raise_for_status()
            result = response.json()

        choices = result.get("choices", [])
        if not choices:
            raise RuntimeError("Groq did not return any choices")

        return choices[0].get("text", "") or choices[0].get("message", "")

    async def health_check(self) -> bool:
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.get(
                    self._build_url(),
                    headers={"Authorization": f"Bearer {self.api_key}"},
                )
                return response.status_code == 200
        except Exception:
            return False
