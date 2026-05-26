# API Reference

REST API for the **Architekt** agent platform (Software Factory). Base URL: `http://<host>:<port>` (default local: `8099`, Docker: `8090`).

**Swagger UI:** `/docs` (FastAPI auto-generated OpenAPI).

## Authentication

Per **ADR-001** (platform rebrand), use the canonical API key environment variable:

| Variable | Status | Notes |
|----------|--------|-------|
| `ARCHITEKT_API_KEY` | **Required (production)** | Set on all deployed hosts and in CI secrets |

When `ARCHITEKT_API_KEY` is set, `AuthMiddleware` protects API mutations. If unset, auth is disabled (development only).

### Bearer token

Send the key on every protected request:

```http
Authorization: Bearer architekt_live_xxxxxxxxxxxxxxxx
```

Example with `curl`:

```bash
export ARCHITEKT_API_KEY="architekt_live_xxxxxxxxxxxxxxxx"

curl -s -X POST "http://localhost:8099/api/missions" \
  -H "Authorization: Bearer ${ARCHITEKT_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"name":"My Epic","workflow_id":"product-lifecycle"}'
```

### Access rules

| Request type | Auth required |
|--------------|---------------|
| `GET` on listed public paths (projects, missions, agents, metrics, health, etc.) | No |
| `POST`, `PATCH`, `DELETE` on `/api/*` | Yes (Bearer) |
| HTML pages, `/static`, `/docs`, SSE streams | No (pages); SSE follows stream endpoint rules |
| Query fallback `?token=<key>` | Supported for scripts (prefer `Authorization` header) |

JWT session cookies (`access_token`) are used by the web UI; API automation should use the Bearer API key.

## Request format

Endpoints accept **dual JSON + form-data** via `_parse_body` (auto-detected). Prefer `Content-Type: application/json` for integrations.

## Projects

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/projects` | Create project |
| GET | `/api/projects` | List projects |

## Missions

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/missions` | Create mission (epic) |
| POST | `/api/missions/{id}/start` | Start mission run |
| POST | `/api/missions/{id}/run` | Run current phase |
| POST | `/api/missions/{id}/wsjf` | Set WSJF scores |
| POST | `/api/missions/{id}/sprints` | Create sprint |
| POST | `/api/missions/{id}/validate` | Validate phase (HITL checkpoint) |
| GET | `/api/missions/{id}` | Mission details |

## Epics / Features / Stories

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/epics/{id}/features` | Create feature under epic |
| POST | `/api/features/{id}/stories` | Create story under feature |
| POST | `/api/features/{id}/deps` | Add dependency |
| PATCH | `/api/features/{id}` | Update feature |
| PATCH | `/api/stories/{id}` | Update story |
| PATCH | `/api/tasks/{id}/status` | Update task status |
| PATCH | `/api/backlog/reorder` | Reorder backlog |
| DELETE | `/api/features/{id}/deps/{dep}` | Remove dependency |
| DELETE | `/api/sprints/{id}/stories/{id}` | Remove story from sprint |
| GET | `/api/sprints/{id}/available-stories` | List unassigned stories |
| GET | `/api/features/{id}/deps` | Get dependencies |

## Metrics & Monitoring

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/metrics/cycle-time` | Cycle time metrics |
| GET | `/api/releases/{project_id}` | Release history |
| GET | `/api/llm/stats` | LLM usage statistics |
| GET | `/api/llm/traces` | LLM call traces |
| GET | `/api/monitoring/live` | Live monitoring (SSE) |

## System

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/health` | Health check |
| GET | `/api/agents` | List agents |
| GET | `/api/sessions` | List sessions |
| GET | `/api/mcps` | List MCP servers |
| GET | `/docs` | Swagger UI |

## SSE streams

| Endpoint | Description |
|----------|-------------|
| `/api/missions/{id}/stream` | Mission execution events |
| `/api/monitoring/live` | System monitoring events |

SSE clients do not send the API key on the EventSource connection; mission control mutations still require Bearer auth.

## CLI (`sf`)

The `sf` CLI uses the same Bearer token from `ARCHITEKT_API_KEY`:

```bash
export ARCHITEKT_API_KEY="architekt_live_xxxxxxxxxxxxxxxx"
sf status
sf missions list
```

## Related docs

- [Security](Security) — headers, rate limits, adversarial gates
- [Deployment Guide](Deployment-Guide) — environment URLs and keys
- [Patterns](Patterns) — orchestration used by mission phases

## 🇫🇷 [Référence API (FR)](API-Reference‐FR)
