# AI Documentation

## Purpose

The AI documentation describes the architecture and responsibilities of Synaris' artificial intelligence layer. Version 2 focuses on building a provider-agnostic orchestrator that can route requests to Gemini, Groq, OpenRouter, and local models in the future.

## AI Orchestrator

The orchestrator is the central decision point for every AI request.

Responsibilities:
- Route requests to the right provider based on experience and intent
- Manage prompt templates and prompt composition
- Apply safety and validation rules before sending requests to the model
- Normalize provider responses for downstream learning logic
- Track provider metadata for later evaluation

## Model router

The model router separates business logic from provider implementation.

Planned providers:
- Gemini — deep reasoning and pedagogical explanations
- Groq — low-latency responses for quick tutoring and direct answers
- OpenRouter — flexible access to community models
- Ollama — optional local model execution for offline or private usage

## Prompt templates

Prompt templates are the canonical source of how Synaris asks questions.

They should:
- preserve educational context
- include source attribution requirements
- enforce safety and guardrails
- support mode-specific behavior (explain, quiz, review)

## Evaluation

AI evaluation is a future phase, but the architecture should enable:
- response quality signals
- correctness checks
- confidence scoring
- educational suitability metrics
- hallucination detection

## Safety

Safety is part of the architecture, not an afterthought.

The AI layer must support:
- prompt injection protection
- prompt leakage prevention
- input validation and sanitization
- output filtering and moderation
- audit logging

## Memory and context

Memory is a future extension, but the orchestrator should be designed so:
- request context is explicit and bounded
- user learning history can be added without API rewrites
- source citations can be attached to every response
