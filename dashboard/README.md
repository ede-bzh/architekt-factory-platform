# Architekt Factory Monitor (legacy)

**Legacy local monitor** on port **8080**. The **primary UI** is the Architekt platform on port **8099** (`python3 -m uvicorn platform.server:app --host 0.0.0.0 --port 8099 --ws none`).

| Surface | URL |
|---------|-----|
| Platform (primary) | `http://localhost:8099` — missions, projects, DSI, analytics |
| Live monitoring | `{PLATFORM_URL}/monitoring` |
| Proof / audit | `{PLATFORM_URL}/proof` |
| This legacy dashboard | `http://localhost:8080` — SQLite factory tasks, daemons, Team of Rivals metrics |

Set `PLATFORM_URL` (default `http://localhost:8099`) so the landing page and nav links point at your platform instance.

## Run

```bash
# From repo root
python3 -m dashboard.server

# Or with env
PORT=8080 PLATFORM_URL=http://localhost:8099 python3 -m dashboard.server
```

Opens at http://localhost:8080 — `/` is a short doc page with platform links; `/legacy` is the factory task monitor.

## Health

- `GET /health` — dashboard status + link to `{PLATFORM_URL}/api/health`

## Scope

This package is **not** the platform web app under `platform/`. Do not restore a nested `dashboard/platform/` tree; use the platform server for product UI.
