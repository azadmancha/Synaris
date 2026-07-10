from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class AIProvider(ABC):
    """Base interface for AI providers in Synaris."""

    name: str

    @abstractmethod
    async def generate_text(self, prompt: str, **kwargs: Any) -> str:
        """Generate a text response for the given prompt."""
        raise NotImplementedError

    @abstractmethod
    async def health_check(self) -> bool:
        """Verify the provider is available and correctly configured."""
        raise NotImplementedError
