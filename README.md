# SovereignAI Worker

Phase 1 — PDF → local RAG → cited answer.

## FarmPlug AI — SIH 2026

**FarmPlug AI — “Your Farm's Plug to Every Market.”**

Smart India Hackathon 2026 · **Problem Statement 26033** · Software · Agriculture, FoodTech & Rural Development

FarmPlug AI is an AI-powered agricultural market intelligence and supply-chain platform connecting Farmers and FPOs with Buyers, Processors and Exporters. It adds a predictive intelligence layer between agricultural supply and market demand.

### SIH Idea Presentation

The official 6-slide competition presentation is prepared as a local artifact. Add the files to the repository using these paths when uploading binaries is available:

- `docs/FarmPlug_AI_SIH_2026_Idea_Presentation.pptx`
- `docs/FarmPlug_AI_SIH_2026_Idea_Presentation.pdf`

**Presentation:** [FarmPlug AI — SIH 2026 Idea Presentation](docs/FarmPlug_AI_SIH_2026_Idea_Presentation.pptx)

**PDF version:** [FarmPlug AI — SIH 2026 Idea Presentation (PDF)](docs/FarmPlug_AI_SIH_2026_Idea_Presentation.pdf)

> The links above are repository-relative placeholders until the binary presentation files are uploaded to `docs/`.

### MVP focus

- Demand Forecasting
- AI-assisted Production / Crop Recommendation
- FreshLife AI — Shelf-Life / Selling-Window Prediction
- Smart Buyer Matching
- Supply Aggregation
- Basic Route Optimization
- Farmer/FPO and Admin Dashboard

### Positioning

FarmPlug AI **complements, not replaces, existing agricultural market infrastructure**. It focuses on predictive intelligence: demand forecasting, production decision support, selling-window intelligence, smart matching, supply aggregation and route optimization.

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
