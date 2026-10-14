# LocalPilot architecture

Browser (HTML/CSS/JS) → Python ThreadingHTTPServer (127.0.0.1:8765) → SQLite

Python HTTP API → Ollama local HTTP endpoint (127.0.0.1:11434) → Qwen3 open-weight model

The AI receives only validated menu context or precomputed sales metrics. It cannot run SQL. All currency values are stored as integer paise and sale lines snapshot unit selling price and estimated ingredient cost. SQLite business IDs scope queries; production requires additional tenant and auth hardening.

## API routes

- POST /api/login, POST /api/logout, GET /api/me
- GET /api/metrics?days=7
- GET /api/menu, POST /api/menu, PUT /api/menu
- POST /api/sales
- GET /api/ai/health
- POST /api/marketing
- POST /api/copilot

## Important limitations

No public deployment or cloud inference is included. No actual Super Zaika sales or recipe costs were supplied, so seeded values are synthetic. AI calls require Ollama running with the selected model. Browser interactions are functional without any JavaScript framework. Authentication is for local demo use only. Marketing responses are plain text and may require human review before publishing.
