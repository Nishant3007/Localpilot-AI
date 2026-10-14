# Codex continuation prompt

You are a senior full-stack engineer and AI architect. Inspect this complete LocalPilot AI repository first. It is a runnable local-first Hacktoberfest Week 2 MVP, with Python stdlib + SQLite + HTML/CSS/JS + Ollama.

**Do not overwrite or discard working features.** First run `python3 -m unittest discover -s tests -v`, start `python3 server.py`, and manually verify login, dashboard, menu edits, sales, analytics, marketing and copilot. Review the README and ARCHITECTURE.md.

Prioritize: (1) fix reproducible defects; (2) add comprehensive HTTP integration and browser E2E tests; (3) add secure persistent auth, CSRF protection, rate limiting and tenant isolation; (4) improve Ollama response validation and prompt-injection resistance; (5) add proper ingredient/recipe CRUD, CSV import and PDF export; (6) optionally migrate the UI/API to Next.js + TypeScript + PostgreSQL/Prisma without feature regressions; (7) deploy a public demo with an authenticated remote inference host and clearly labeled synthetic data. Never expose Ollama publicly. Keep local/offline mode working.

Acceptance criteria: real Ollama generation, no fake AI output, accurate server-side revenue math, working sale-to-dashboard flow, polished mobile UI, all tests passing, clear README, and an honest DEV challenge submission. Record changes and actual test outcomes; never claim unverified deployment or first-user feedback.
