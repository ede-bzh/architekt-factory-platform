# Security

Security model for the **Architekt** agent platform: API authentication, HTTP hardening, adversarial quality gates, and container isolation.

## Authentication

### API key (ADR-001)

| Variable | Role |
|----------|------|
| `ARCHITEKT_API_KEY` | **Primary** — use for all new deployments |
| `ARCHITEKT_API_KEY` | **6-month alias** — same secret; supported for backward compatibility |

`AuthMiddleware` (`platform/security.py`) validates Bearer tokens with SHA-256 comparison. Mutations (`POST`, `PATCH`, `DELETE` on `/api/*`) require a valid key when either variable is set.

```http
Authorization: Bearer <your-api-key>
```

**Rules:**

- Public `GET` endpoints (projects, missions list, agents, metrics, health) remain readable without a key
- HTML UI can use JWT cookies; automation should use Bearer + `ARCHITEKT_API_KEY`
- If no key is configured and `ENVIRONMENT=dev`, auth is disabled (never use in production)
- Production Azure stacks may add **nginx basic auth** in front of the app

### Session auth (web UI)

`platform/auth/middleware.py` supports JWT via `access_token` cookie or long Bearer JWT. API keys map to an admin-equivalent user for scripted access.

## Human-in-the-loop (HITL) deploy gate

Production rollout is not fully autonomous. The **`human-in-the-loop`** pattern pauses the workflow until a human approves a checkpoint.

Typical gates (see `product-lifecycle` workflow):

| Phase | Pattern | Gate | Human decision |
|-------|---------|------|----------------|
| Strategic committee | `human-in-the-loop` | `all_approved` | GO / NOGO / PIVOT |
| Deploy production | `human-in-the-loop` | `all_approved` | Approve canary → 100% after metrics review |
| Data migration | `human-in-the-loop` | checkpoint | GO/NOGO before cutover |
| Canary deployment | `human-in-the-loop` | checkpoint | Promote or rollback |

The deploy phase (`deploy-prod`) runs DevOps/SRE agents for canary (1%), then blocks on **`POST /api/missions/{id}/validate`** until a project manager confirms full promotion. This is the **HITL deploy gate** — agents prepare evidence; humans hold veto on production traffic.

Related workflows: `canary-deployment`, `data-migration`, `ao-compliance`.

## Adversarial validation (L0 / L1 / L2)

Inspired by *Team of Rivals* (arXiv:2601.14351). **Code writers cannot declare their own success** — critics run on separate model/vendor slots where configured.

### L0 — Deterministic (absolute veto)

Zero LLM cost; runs on every agent output in execution patterns:

- Forbidden shortcuts: `test.skip`, `@ts-ignore`, `#[ignore]`, empty `catch`
- SLOP: lorem ipsum, `TBD`, `XXX`, placeholder text
- MOCK: `NotImplementedError`, fake build scripts, hardcoded `BUILD SUCCESS`
- Hallucination: claims file changes without matching tool-call evidence
- Stack mismatch: wrong language for target platform

**Result:** absolute **VETO** — phase cannot pass on hard failures.

### L1 — LLM semantic (absolute veto)

Separate LLM reviews slop, logic errors, and hallucinated reasoning. Skipped for **discussion** patterns (`network`, `debate`, `aggregator`, `human-in-the-loop`) to avoid blocking ideation.

**Result:** absolute **VETO** on reject.

### L2 — Architecture (veto + escalation)

`arch-critic` / security critics evaluate RBAC, validation boundaries, API design, and threat model fit.

**Result:** **VETO** with optional escalation to human committee.

### Orchestration patterns

| Pattern | Role |
|---------|------|
| `adversarial-pair` | Writer ↔ reviewer loop (max 5 iterations) |
| `adversarial-cascade` | Swiss-cheese: code → L1 code → L1 security → L2 arch |
| `sf-tdd` | Brain → TDD worker → critics → DevOps |

Retries: pattern config up to **5 attempts**; guard may soft-pass warnings vs hard reject (score ≥ 7).

## Rate limiting

Two layers:

### HTTP API (`RateLimitMiddleware`)

- Default: **60 requests / 60 seconds** per client key
- Client key = **IP + Bearer token prefix** (hashed)
- PostgreSQL table `rate_limit_hits` persists counts across container restarts when `DATABASE_URL` points to PG
- Response: `429 Rate limit exceeded`

### LLM provider (`llm/client.py`)

- `LLM_RATE_LIMIT_RPM` (default **15** RPM) with token budget per window
- Cooldown **90s** on HTTP 429 from providers
- Mission orchestrator retries phases up to `MAX_LLM_RETRIES` on rate limit

Configure stricter limits at the reverse proxy (nginx) for public demos.

## HTTP security headers

Set in `platform/server.py` for every response:

| Header | Value |
|--------|-------|
| `Strict-Transport-Security` | `max-age=31536000` (HTTPS only) |
| `X-Frame-Options` | `DENY` (except workspace preview routes) |
| `X-Content-Type-Options` | `nosniff` |
| `X-XSS-Protection` | `1; mode=block` |
| `Referrer-Policy` | `strict-origin-when-cross-origin` |

### Content-Security-Policy (CSP)

CSP is applied globally. Important directives:

- **`connect-src 'self'`** — HTMX/fetch/SSE only to same origin (mitigates data exfiltration from injected scripts)
- `script-src` allows `'unsafe-inline'` for HTMX + Chart.js CDN on standard pages
- Workspace routes (`/projects/{id}/workspace`) relax `frame-src` for embedded dev tools (preview, DB admin)

Jinja2 templates use **autoescaping** for XSS defense; CSP is a second layer.

## Code and data security

| Topic | Mitigation |
|-------|------------|
| **SQL injection** | Parameterized queries (`?` placeholders); no SQL f-strings |
| **XSS** | Jinja2 autoescape + CSP `connect-src 'self'` |
| **Prompt injection** | L0 + L1 adversarial guards on tool outputs |
| **Secrets** | `~/.config/factory/*.key`, chmod `600`; never commit `*_API_KEY=dummy` |
| **Docker** | Container runs as a dedicated **non-root user** (minimal image, no root PID 1) |

## A2A veto levels

Agent-to-agent messages support veto strength: `ABSOLUTE`, `STRONG`, `ADVISORY` (`platform/a2a/veto.py`). Adversarial L0/L1 map to absolute blocks; L2 may surface as STRONG + human escalation.

## Related docs

- [API Reference](API-Reference) — Bearer auth examples
- [Patterns](Patterns) — HITL and adversarial patterns
- [Deployment Guide](Deployment-Guide) — production hardening

## 🇫🇷 [Sécurité (FR)](Security‐FR)
