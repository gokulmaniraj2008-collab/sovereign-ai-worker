# SovereignAI Worker

Phase 1 — PDF → local RAG → cited answer.

## Local stack

- Next.js + TypeScript
- FastAPI + Python
- PostgreSQL + pgvector
- PyMuPDF + Tesseract
- Sentence Transformers (`all-MiniLM-L6-v2`, 384 dimensions)
- Ollama-compatible local LLM
- Local filesystem storage

## Run

```bash
docker compose up --build
```

Then pull a local Ollama model once while connected:

```bash
docker compose exec ollama ollama pull llama3.2:3b
```

Open `http://localhost:3000` and upload a PDF.

## API

- `GET /health`
- `POST /documents/upload`
- `POST /documents/{id}/ingest`
- `GET /documents`
- `POST /rag/query`
- `GET /security/status`
- `GET /docs`

## Offline acceptance test

1. Download all required model files and container images before isolation.
2. Confirm upload → ingest → query works.
3. Disable the host network.
4. Repeat the exact query.
5. Verify the answer and citations still work.

A local model does not by itself prove an air-gapped deployment; the actual runtime must be network-isolated and have no external dependency.
