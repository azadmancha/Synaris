"""AI services package.

This package contains the logical scaffolding for the Synaris AI orchestrator,
provider adapters, prompt templates, memory, evaluation, and safety systems.
"""

from services.ai.orchestrator import AIOrchestrator

__all__ = ["AIOrchestrator"]
