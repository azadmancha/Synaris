# RAG Documentation

## Purpose

Retrieval-Augmented Generation (RAG) is the mechanism that gives Synaris knowledge grounded in educational resources, rather than relying solely on model hallucination.

## Pipeline overview

1. Document ingestion
2. Cleaning and normalization
3. Chunking and content segmentation
4. Embedding generation
5. Vector database indexing
6. Semantic retrieval
7. Reranking and relevance filtering
8. Context assembly and citation builder

## Document sources

Initial targets:
- Wikipedia
- OpenStax
- Wikibooks

Future sources:
- curated educational notes
- textbooks and curriculum-aligned content
- teacher-authored lesson plans

## Embeddings

Embeddings are the bridge between text and semantic similarity.

The architecture should keep embedding generation separate from retrieval and support provider changes without altering application logic.

## Vector search

The vector search layer should:
- perform fast semantic similarity lookups
- return document identifiers and metadata
- provide sufficient context for the AI prompt
- be replaceable with Qdrant, Pinecone, or another vector store

## Citations

Every retrieved section should preserve:
- source name
- source link
- confidence or relevance signal

The final prompt should include citation metadata so Synaris can explain where knowledge came from.
