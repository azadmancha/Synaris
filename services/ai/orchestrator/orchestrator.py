from __future__ import annotations

import os
from typing import Any

from services.ai.providers.gemini.client import GeminiProvider
from services.ai.providers.groq.client import GroqProvider
from services.ai.providers.openrouter.client import OpenRouterProvider


class AIOrchestrator:
    """Central AI orchestration layer for Synaris."""

    def __init__(self, default_provider: str | None = None) -> None:
        self.providers: dict[str, Any] = {}

        if os.getenv("OPENROUTER_API_KEY"):
            self.providers["openrouter"] = OpenRouterProvider()

        try:
            self.providers["gemini"] = GeminiProvider()
        except ValueError:
            pass

        try:
            self.providers["groq"] = GroqProvider()
        except ValueError:
            pass

        self.default_provider = default_provider or next(iter(self.providers), "openrouter")

    def _select_provider(self, provider_name: str | None = None):
        if provider_name and provider_name in self.providers:
            return self.providers[provider_name]
        if self.default_provider in self.providers:
            return self.providers[self.default_provider]
        raise ValueError("No AI provider is configured")

    async def generate_text(self, prompt: str, provider: str | None = None, **kwargs: Any) -> str:
        """Generate a response using the selected AI provider."""
        provider_client = self._select_provider(provider)
        return await provider_client.generate_text(prompt, **kwargs)

    async def explain(self, prompt: str, provider: str | None = None, **kwargs: Any) -> str:
        """Generate an educational explanation for a prompt."""
        return await self.generate_text(prompt, provider=provider, **kwargs)

    async def health(self) -> dict[str, bool]:
        return {name: await client.health_check() for name, client in self.providers.items()}
