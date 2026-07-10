# Engineering Decisions


This document records the major architectural and engineering decisions made during the development of Synaris.

Rather than choosing technologies because they are popular, every decision attempts to balance scalability, maintainability, performance, learning value, and long-term flexibility.

---

# Why Next.js?

## Decision

Use **Next.js** as the primary frontend framework.

## Why?

Synaris requires:

* Modern routing
* Component-based architecture
* Excellent developer experience
* Strong TypeScript support
* Scalability

Next.js provides these while remaining one of the most mature React frameworks.

## Alternatives Considered

* React + Vite
* Angular
* Vue
* SvelteKit

## Why Next.js Won

It offers the best long-term ecosystem and integrates naturally with modern web development.

---

# Why FastAPI?

## Decision

Use **FastAPI** for the backend.

## Why?

Synaris is an AI platform.

Most backend operations involve:

* AI requests
* asynchronous processing
* API communication
* authentication
* database interaction

FastAPI excels in exactly these scenarios.

## Alternatives Considered

* Flask
* Django
* Express.js

## Why FastAPI Won

* Async support
* Automatic OpenAPI documentation
* Excellent performance
* Strong typing
* Easy scalability

---

# Why PostgreSQL?

## Decision

Use PostgreSQL as the primary relational database.

## Why?

Synaris stores structured information:

* Users
* Authentication
* Learning History
* Progress
* Conversations
* Study Plans
* Quiz Results

PostgreSQL is reliable, scalable, and well-suited for relational data.

## Alternatives Considered

* SQLite
* MySQL
* MongoDB

## Why PostgreSQL Won

SQLite powered the early prototype (StudyForge), but PostgreSQL is significantly better for production systems with multiple users and complex relationships.

---

# Why a Vector Database?

## Decision

Store semantic embeddings separately from relational data.

## Why?

Educational retrieval requires semantic similarity rather than keyword search.

A vector database enables:

* RAG
* Semantic Search
* Similar Question Retrieval
* Knowledge Retrieval

## Alternatives Considered

* PostgreSQL only
* Elasticsearch

## Why a Vector Database Won

Embedding search is a fundamentally different problem from relational storage.

Separating both systems keeps the architecture cleaner and more scalable.

---

# Why Retrieval-Augmented Generation (RAG)?

## Decision

Do not rely solely on Large Language Models.

## Why?

LLMs can hallucinate.

Education requires trustworthy information.

RAG allows Synaris to retrieve reliable educational resources before generating responses.

Benefits include:

* Better accuracy
* Source citations
* Up-to-date knowledge
* Reduced hallucinations

---

# Why Gemini?

## Decision

Use Gemini as one of the primary reasoning models.

## Why?

Gemini performs well for:

* Long explanations
* Educational reasoning
* Multi-step thinking
* Complex concept breakdowns

It serves as the primary "deep reasoning" model inside Synaris.

---

# Why Groq?

## Decision

Use Groq for low-latency inference.

## Why?

Not every question requires long reasoning.

Simple questions benefit from extremely fast responses.

Groq provides excellent speed while maintaining good quality.

---

# Why OpenRouter?

## Decision

Integrate OpenRouter as a provider layer.

## Why?

The AI ecosystem changes rapidly.

OpenRouter provides access to multiple models through a single interface, making experimentation easier without changing the overall architecture.

---

# Why Ollama?

## Decision

Support local models in the future.

## Why?

Some users may prefer:

* Offline usage
* Greater privacy
* Self-hosted deployments

Ollama makes these scenarios possible without redesigning Synaris.

---

# Why Multiple AI Providers?

## Decision

Never depend on a single model provider.

## Why?

Different models excel at different tasks.

Examples:

Gemini

* Long reasoning

Groq

* Fast responses

OpenRouter

* Model flexibility

Ollama

* Local execution

Using an AI Orchestrator allows Synaris to dynamically choose the most appropriate provider.

---

# Why an AI Orchestrator?

## Decision

Separate application logic from AI providers.

## Why?

Without an orchestrator, every part of the application would need to know which model to call.

The orchestrator centralizes:

* Model Selection
* Prompt Construction
* Context Management
* Provider Failover
* AI Evaluation
* Safety Checks

This keeps the architecture modular and prevents vendor lock-in.

---

# Why an Adaptive Learning Engine?

## Decision

Separate learning logic from AI responses.

## Why?

The objective of Synaris is not generating answers.

The objective is improving learning.

The Adaptive Learning Engine is responsible for:

* Personalized explanations
* Difficulty adaptation
* Learning path selection
* Misconception detection
* Study planning

Keeping this logic separate makes future improvements significantly easier.

---

# Why AI Agents?

## Decision

Adopt a multi-agent architecture in future versions.

## Why?

As Synaris grows, a single AI model should not perform every task.

Instead, specialized agents can focus on different responsibilities.

Examples include:

* Tutor Agent
* Planner Agent
* Quiz Agent
* Research Agent
* Evaluation Agent

This improves modularity and makes the system easier to extend.

---

# Why Docker?

## Decision

Containerize the entire application.

## Why?

Docker ensures that Synaris behaves consistently across development, testing, and production environments.

Benefits include:

* Reproducibility
* Easier deployment
* Dependency isolation
* Better scalability

---

# Why Security First?

## Decision

Treat AI security as a core architectural requirement.

## Why?

Educational AI systems are vulnerable to:

* Prompt Injection
* Prompt Leakage
* Jailbreak Attempts
* Malicious Inputs

Security should never be added later.

It should exist from the first version.

---

# Why Explainability Instead of Traditional XAI?

## Decision

Focus on educational explainability.

## Why?

Traditional Explainable AI (XAI) techniques are designed for classical machine learning models and are not directly applicable to large language models.

For students, what matters is understanding the answer—not the model's internal mechanics.

Synaris therefore emphasizes:

* Confidence scoring
* Source attribution
* Citations
* Alternative explanations
* Learning feedback

This makes the system more trustworthy without overwhelming learners.

---

# Why Synaris?

This is perhaps the most important design decision.

Synaris is not being built to demonstrate AI.

It is being built to improve learning.

Every architectural decision, every technology choice, and every future feature ultimately answers one question:

> **Does this genuinely help students learn better?**

If the answer is no, it doesn't belong in Synaris.
