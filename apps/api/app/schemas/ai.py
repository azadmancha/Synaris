from __future__ import annotations

from pydantic import BaseModel
from typing import Literal


class AIRequest(BaseModel):
    prompt: str
    provider: Literal["gemini", "groq", "openrouter"] | None = None
    max_tokens: int | None = 512
    temperature: float | None = 0.3


class AIResponse(BaseModel):
    provider: str
    text: str
