# LocalPilot AI — Hacktoberfest Week 2: Side Hustle

**Local-first restaurant business copilot powered by Ollama and an open-weight Qwen model.**

## Quick start on macOS

1. Install Python 3.10+ (`python3 --version`). No pip or npm packages are needed.
2. Unzip the project. Open Terminal in the extracted `localpilot-ai` folder.
3. Run `python3 server.py` (or double-click `run.command`).
4. Open **http://127.0.0.1:8765**.
5. Sign in with **demo@localpilot.ai** / **demo12345**.

The dashboard, menu editing, sale recording and analytics work immediately, even without Ollama.

## Enable real open-weight AI

Install Ollama from https://ollama.com/download or via `brew install ollama`.

In terminal A:

```bash
ollama serve
```

In terminal B:

```bash
ollama pull qwen3:4b-instruct
```

Restart LocalPilot. Marketing Studio and AI Copilot now call the **actual local model** through `http://127.0.0.1:11434/api/chat`. If your Ollama build does not support this tag, run `ollama list` and set `OLLAMA_MODEL` to an installed compatible model before starting LocalPilot.

To change the model:

```bash
OLLAMA_MODEL=qwen3:4b-instruct python3 server.py
```

## Features

- Login and isolated single-business demo session
- Responsive dashboard with KPI cards and sales trend
- Editable menu variants and estimated ingredient contribution
- Multi-item sale recording with sale-time price and cost snapshots
- Analytics over 7/30/90 days
- Real Ollama-powered English/Hindi/Hinglish marketing generation
- Grounded AI copilot receiving precomputed business metrics
- Clear model availability and error states

## Demo walkthrough

1. Sign in and review synthetic sales dashboard.
2. Visit **Menu Studio**, edit Chicken Soup's cost, save.
3. Visit **Record Sales**, add Punjabi Chicken and Chicken Soup, complete sale.
4. Visit **Overview** and verify KPIs updated.
5. Visit **Marketing Studio**, select Chicken Tikka Juicy and Hindi, generate copy.
6. Visit **AI Copilot**, ask 'Which dishes made the most revenue?' and see grounded metrics.
7. Visit **Settings** to confirm local Ollama connectivity.

## Privacy and architecture

The browser talks to a Python standard-library HTTP server bound to **127.0.0.1**, which stores data in local SQLite. The server connects to Ollama locally. No cloud AI API is required. Fonts are loaded from Google Fonts when online; offline fallback fonts work without internet. There is no external telemetry.

Business metrics are calculated deterministically from SQLite; AI only writes marketing copy or interprets a bounded metrics snapshot. It does not execute arbitrary SQL or change records. The demo seed uses *illustrative, fictional* order and ingredient-cost data; these are not real Super Zaika sales.

**Security scope:** This is a local demo, **not** a production multi-tenant SaaS. Sessions are held in memory, and the demo password is public. Do not expose the server to the internet, put real sensitive data in the demo, or treat this as production authentication. For deployment, add persistent secure sessions, HTTPS, CSRF protection, audit logging, per-business permissions, rate limits and hardened infrastructure.

## Project layout

```
server.py             HTTP API, SQLite schema, seeded data, Ollama adapter
static/index.html     App shell and login
static/style.css      Responsive design system
static/app.js         Dashboard, menu, sales, marketing, copilot UI
run.command           macOS launch shortcut
tests/test_app.py     Automated server/API checks
docs/                 Architecture, agent prompt, submission outline
```

## Run tests

```bash
python3 -m unittest discover -s tests -v
```

## Troubleshooting

- **Ollama offline**: Run `ollama serve` and check `http://127.0.0.1:11434/api/tags`.
- **Model not pulled**: Run `ollama pull qwen3:4b-instruct` and `ollama list`.
- **Port occupied**: Run `PORT=8766 python3 server.py`.
- **Reset demo**: Stop server, delete `localpilot.db`, restart (deletes local edits and sales).
- **Slow first generation**: The first inference loads the model into memory. Smaller models may run faster on low-memory Macs.

## License and acknowledgments

Application source: MIT (see LICENSE). Ollama and the selected Qwen model have their own licenses; review the exact model tag/license before redistribution. No claim is made that the model weights are part of this ZIP.
