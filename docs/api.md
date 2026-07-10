# API Documentation

## Overview

The Synaris API is the backend gateway for authentication, user profile management, learning interaction, and AI orchestration.

## Authentication

Authentication is handled through Google OAuth on the frontend and validated on the backend using signed session tokens. The API uses a secure cookie or bearer token to authenticate requests.

## Core route groups

- `GET /health` — service health and readiness check
- `GET /users/me` — current authenticated user profile
- `POST /users/sync` — synchronize the authenticated user profile to the backend
- `POST /chat` — future AI tutoring interaction endpoint
- `POST /quiz` — future quiz generation endpoint
- `GET /progress` — future learning progress endpoint
- `POST /evaluate` — future AI response evaluation endpoint

## Documentation strategy

This document will expand as the API surface grows. The first phase focuses on secure authentication and user profile scaffolding, while keeping endpoints consistent with the long-term learning platform.

## Data model contract

### User
- `id` — UUID
- `email` — string
- `full_name` — optional string
- `picture` — optional URL
- `google_sub` — Google subject identifier
- `is_active` — boolean
- `created_at` / `updated_at` — timestamps

## Notes

The API should always validate incoming payloads, return meaningful HTTP status codes, and keep error details safe for logs rather than clients.
