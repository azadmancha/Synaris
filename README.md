# Synaris

AI-powered personalized learning platform built to help students understand concepts deeply, not just memorize answers.

## Status

- Architecture: Complete ✅
- Backend: Initial API scaffold, authentication and security foundation
- Frontend: Next.js scaffold with Google OAuth sign-in flow
- Docs: Foundation for API, AI, RAG, and research planning established

## Vision

Synaris brings together strong educational design, secure AI orchestration, and an extensible architecture so long-term learning software can evolve without rewrites.

## Core principles

- Security by design
- Modular, maintainable architecture
- Clear separation between frontend, backend, AI orchestration, and retrieval
- Educational explainability over marketing-driven XAI
- Production-ready scaffolding with Docker and CI

## Tech stack

- FastAPI backend
- Next.js frontend
- PostgreSQL database
- Docker / Docker Compose
- GitHub Actions CI
- AI orchestration-ready architecture

## Repository structure

- `apps/api` — FastAPI backend service and SQLAlchemy models
- `apps/web` — Next.js frontend scaffold and authentication routes
- `services` — Domain architecture packages for future AI, RAG, security, and authorization services
- `docs` — Design, roadmap, API, AI, RAG, and research documentation

## Local development

1. Copy `.env.example` to `.env`
2. Fill in `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`, `AUTH_SECRET`, and `DATABASE_URL`
3. Start the development stack:
   ```bash
   docker compose up --build
   ```
4. Open the frontend at `http://localhost:3000`
5. Open the API docs at `http://localhost:8000/docs`

## Current milestone

This scaffold establishes the core infrastructure for Synaris:

- Secure backend foundations with JWT and OAuth-aware session validation
- Next.js landing/dashboard scaffold
- Security middleware and organized feature packages
- Foundational documentation for API, AI orchestration, RAG, and research planning

## Contributing

Please follow the architectural direction in `docs/architecture.md`, `docs/roadmap.md`, `docs/decisions.md`, and `README.md` before adding new features.

## License

This project is licensed under the terms of the MIT License.
