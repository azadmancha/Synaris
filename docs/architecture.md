# Synaris Architecture



This document describes the architecture of **Synaris**, the reasoning behind each layer, and how every component works together to build a scalable, secure, and AI-native personalized learning platform.

Rather than focusing on individual technologies, this document explains the design decisions that make Synaris modular, maintainable, and extensible.

---

# Design Philosophy

Every architectural decision in Synaris follows six core principles:

* Modular Architecture
* AI Provider Independence
* Security by Design
* Adaptive Learning
* Explainability
* Scalability

Each component has a single responsibility and can evolve independently without requiring major changes to the rest of the system.

---

# Architecture

```text
                           Student
                              │
                              ▼
                     Next.js Frontend
                              │
                              ▼
                     FastAPI Backend
                              │
                              ▼
                    AI Orchestrator Layer
                              │
        ┌──────────────┬──────────────┬──────────────┬──────────────┐
        ▼              ▼              ▼              ▼
     Gemini         Groq         OpenRouter       Ollama
        └──────────────┴──────────────┬──────────────┘
                                      ▼
                         Adaptive Learning Engine
                                      │
          ┌───────────────────────────┼──────────────────────────┐
          ▼                           ▼                          ▼
     RAG Pipeline             Explainability Layer        Security Layer
          │                           │
          ▼                           ▼
 Vector Database               Learning Memory
          │                           │
          └──────────────┬────────────┘
                         ▼
                    PostgreSQL
                         │
                         ▼
            Learning Analytics & Dashboard
```

---

# System Layers

---

# 1. Presentation Layer

### Technologies

* Next.js
* React
* TypeScript
* Tailwind CSS

## Purpose

The Presentation Layer is responsible for the complete user experience.

Responsibilities include:

* User Interface
* Authentication
* Dashboard
* AI Chat
* Quiz Interface
* Progress Tracking
* Settings

This layer intentionally contains **no business logic**.

Its responsibility is to collect user input, display information, and communicate with the backend.

---

# 2. API Layer

### Technology

* FastAPI

## Purpose

The API Layer serves as the gateway to every backend service.

Responsibilities include:

* Authentication
* Authorization
* Validation
* Request Routing
* Rate Limiting
* Response Formatting
* Error Handling

No component communicates directly with AI providers or databases.

Every request passes through this layer.

---

# 3. AI Orchestrator Layer

The AI Orchestrator is the central decision-making component of Synaris.

Instead of communicating directly with Gemini or Groq, every request first enters the orchestrator.

Responsibilities:

* Model Selection
* Prompt Construction
* Context Management
* Provider Failover
* Cost Optimization
* Latency Optimization
* Conversation Management
* AI Evaluation
* Safety Checks
* Response Formatting

---

## Why an AI Orchestrator?

Every AI model has different strengths.

**Gemini**

* Long reasoning
* Complex explanations

**Groq**

* Extremely fast inference
* Low latency interactions

**OpenRouter**

* Access to multiple community models

**Ollama**

* Local execution
* Offline capability
* Privacy-focused deployment

The orchestrator dynamically selects the best provider for each task while keeping the rest of the system provider-independent.

This prevents vendor lock-in and simplifies future upgrades.

---

# 3.5. Security Layer

Security is a core architectural pillar for Synaris, not an optional feature. Every request passes through a shared security layer that:

* validates and normalizes user input
* protects against prompt injection and prompt leakage
* applies request throttling and abuse detection
* isolates AI prompts from sensitive metadata
* preserves audit trails for login and AI interactions

The security layer is intentionally decoupled from the AI provider layer so safety rules remain consistent even as models evolve.

---

# 4. Adaptive Learning Engine

The Adaptive Learning Engine is the heart of Synaris.

Unlike traditional AI chatbots, Synaris is designed to understand how each student learns and continuously adapt.

Responsibilities:

* Personalized Explanations
* Difficulty Adaptation
* Learning Path Selection
* Misconception Detection
* Concept Reinforcement
* Quiz Personalization
* Study Planning

Every learning interaction contributes to improving future interactions.

---

# 5. Retrieval-Augmented Generation (RAG)

Large Language Models are powerful but cannot always guarantee factual accuracy.

Rather than relying solely on model knowledge, Synaris retrieves educational resources before generating responses.

Pipeline

```text
Question
    │
    ▼
Retrieve Documents
    │
    ▼
Chunking
    │
    ▼
Embeddings
    │
    ▼
Vector Database
    │
    ▼
Retrieval
    │
    ▼
Reranking
    │
    ▼
Context Builder
    │
    ▼
Large Language Model
    │
    ▼
Answer
```

---

## Planned Knowledge Sources

* Wikipedia
* OpenStax
* Wikibooks
* Future Educational Datasets

---

## Why RAG?

Benefits include:

* Reduced Hallucinations
* Better Accuracy
* Source Citations
* Up-to-Date Knowledge
* Transparent Learning

Students should learn from reliable educational sources rather than blindly trusting AI-generated answers.

---

# 6. Explainability Layer

Instead of exposing internal model reasoning, Synaris focuses on **educational explainability**.

Responsibilities:

* Confidence Scoring
* Source Attribution
* Citation Generation
* Alternative Explanations
* Learning Feedback

The objective is to help students understand *why* a particular explanation was chosen while keeping the interface simple and intuitive.

---

# 7. Data Layer

Different types of information require different storage systems.

## PostgreSQL

Stores structured application data.

Examples:

* Users
* Authentication
* Profiles
* Conversations
* Progress
* Learning Plans
* Quiz Results

---

## Vector Database

Stores semantic embeddings.

Used for:

* RAG
* Semantic Search
* Similar Question Retrieval
* Knowledge Retrieval

---

## Redis (Planned)

High-speed temporary storage.

Used for:

* Session Storage
* Caching
* Rate Limiting
* Temporary Memory

---

# 8. Security Layer

Security is implemented as a cross-cutting concern across every layer of Synaris.

Every request follows the same security pipeline.

```text
Request
    │
    ▼
Authentication
    │
    ▼
Authorization
    │
    ▼
Validation
    │
    ▼
Prompt Protection
    │
    ▼
AI Processing
    │
    ▼
Output Safety
    │
    ▼
Response
```

---

## Security Features

* Google OAuth
* JWT Authentication
* Role-Based Authorization
* Prompt Injection Protection
* Prompt Leak Prevention
* Jailbreak Detection
* Input Validation
* Output Filtering
* Secure API Key Management
* Rate Limiting
* Audit Logging

Security is treated as a foundational requirement rather than an optional feature.

---

# 9. Learning Memory

Synaris models learning behavior rather than storing personal information.

Examples include:

* Strengths
* Weaknesses
* Preferred Learning Style
* Learning Pace
* Topic Mastery
* Revision History

This enables increasingly personalized learning experiences over time.

---

# Continuous Learning Loop

Every interaction contributes to improving future learning.

```text
Student Interaction
        │
        ▼
Adaptive Explanation
        │
        ▼
Learning Feedback
        │
        ▼
Progress Update
        │
        ▼
Learning Memory
        │
        ▼
Future Personalization
```

Unlike traditional chatbots, Synaris continuously evolves alongside the learner.

---

# Scalability

The architecture is intentionally modular.

New components can be introduced independently.

Examples include:

* New AI Models
* Additional AI Agents
* New Retrieval Systems
* New Databases
* New Educational Resources
* Future Frontends

This minimizes architectural rewrites and supports long-term maintainability.

---

# Future Architecture

Planned future capabilities include:

### AI

* Multi-Agent Systems
* Long-Term Memory
* Multimodal Learning

### Learning

* Knowledge Graphs
* Educational Benchmarking
* Research Frameworks

### Platform

* Teacher Dashboard
* Classroom Support
* Community Learning
* LMS Integrations

These additions build upon the existing architecture without requiring fundamental redesign.

---

# Conclusion

Synaris is designed as an AI-native educational platform rather than a traditional chatbot.

Every architectural decision is evaluated against one guiding question:

> **Does this help students learn more effectively while keeping high-quality education freely accessible?**

The architecture prioritizes:

* Personalization
* Reliability
* Security
* Explainability
* Scalability
* Maintainability

Technology will continue to evolve.

Models will change.

New AI techniques will emerge.

The architecture is designed so that Synaris can evolve with them—without ever losing sight of its mission:

> **Making high-quality, personalized education freely accessible through trustworthy AI.**
