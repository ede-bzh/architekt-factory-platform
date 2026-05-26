# Architekt Factory Platform — Context

Agent orchestration platform for **Architekt** (AI-native digital product studio). Repository: [ede-bzh/architekt-factory-platform](https://github.com/ede-bzh/architekt-factory-platform).

## STRUCTURE

```
platform/            # Agent Platform — FastAPI web app
  server.py          # Port 8090 (prod) / 8099 (dev)
  web/routes/        # 10 sub-modules (helpers.py: _parse_body dual JSON/form)
  a2a/               # Agent-to-Agent: bus, negotiation, veto
  agents/            # Loop, executor, store (163 agents)
  patterns/          # 15 orchestration patterns (12 DB + 3 engine-only)
  missions/          # SAFe lifecycle + ProductBacklog
  workflows/         # 41 builtin workflows
  llm/               # Multi-provider client + observability
  tools/             # code, git, deploy, memory, security, browser, MCP bridge
  ops/               # Auto-heal, chaos, endurance, backup/restore
  services/          # Notification (Slack/Email/Webhook)
  mcps/              # MCP server manager (fetch, memory, playwright)
  deploy/            # Dockerfile + docker-compose (Azure VM)
cli/                 # sf <command> (platform client, SSE streaming)
dashboard/           # Lightweight monitoring dashboard (port 8080)
mcp_lrm/             # MCP LRM server (port 9500)
skills/              # Agent YAML definitions
projects/            # Per-project configs
data/                # SQLite DBs (platform.db)
tests/               # pytest + Playwright E2E
deploy/              # Helm charts
docs/                # wiki, architekt/, adr/
```

## REPOSITORY

```
ede-bzh/architekt-factory-platform   ← GitHub (this repo)
  origin → github.com/ede-bzh/architekt-factory-platform
  platform/  cli/  dashboard/  docs/  tests/  …
```

**Workflow** : develop in this repository → `git push origin main`.

Local data and secrets stay outside git (`data/`, `~/.config/factory/*.key`).

## ENVIRONMENTS (3 deployments)

```
┌────────────────┬─────────────────────────┬──────────────────────────────────┐
│ Environment    │ URL / Access            │ Details                          │
├────────────────┼─────────────────────────┼──────────────────────────────────┤
│ Azure Prod     │ http://<AZURE_VM_IP>    │ D4as_v5 4CPU/16GB, francecentral │
│                │ SSH: architekt@<VM>       │ LLM: azure-openai / gpt-5-mini  │
│                │ nginx basic auth        │ Container: deploy-platform-1     │
│                │                         │ Compose: deploy/docker-compose-  │
│                │                         │   vm.yml (context: /opt/architekt) │
│                │                         │ Module: architekt_platform (*)     │
│                │                         │ Patches: /opt/architekt/patches/   │
│                │                         │ OTEL → Jaeger :16686             │
├────────────────┼─────────────────────────┼──────────────────────────────────┤
│ OVH Demo       │ http://<OVH_IP>         │ VPS OVH, Debian                  │
│                │ SSH: debian@<OVH_IP>    │ LLM: demo (mock, no key)        │
│                │                         │ Container: software-factory-     │
│                │                         │   platform-1                     │
│                │                         │ Code: /opt/software-factory/     │
│                │                         │ Image: software-factory-         │
│                │                         │   platform:v2                    │
├────────────────┼─────────────────────────┼──────────────────────────────────┤
│ Local Dev      │ http://localhost:8099   │ Linux/macOS, Python 3.12+        │
│                │ Dashboard: :8080        │ LLM: minimax / MiniMax-M2.5     │
│                │                         │ Module: platform (source tree)   │
│                │                         │ DB: data/platform.db (SQLite)    │
│                │                         │ No Docker, direct uvicorn        │
└────────────────┴─────────────────────────┴──────────────────────────────────┘
```

Runtime prod : package `architekt_platform`, `/opt/architekt`, user Docker `architekt` (voir `docs/adr/001-rebrand-architekt.md`).

## DEPLOY

```
Docker: git clone → make setup → make run → http://localhost:8090
Demo:   PLATFORM_LLM_PROVIDER=demo (mock, no key)
```

## RUN

```bash
# Platform CLI
sf status | sf ideation "prompt" | sf missions list | sf projects chat ID "msg"

# Platform dev (NEVER --reload, ALWAYS --ws none)
python3 -m uvicorn platform.server:app --host 0.0.0.0 --port 8099 --ws none --log-level warning

# Dashboard (local monitoring)
python3 -m dashboard.server  # → http://localhost:8080

# Tests
python3 -m pytest tests/ -v                    # unit + doc gates
cd platform/tests/e2e && npx playwright test   # E2E (9 specs)
```

## LLM

```
Default: PLATFORM_LLM_PROVIDER=minimax  PLATFORM_LLM_MODEL=MiniMax-M2.5
Azure:   PLATFORM_LLM_PROVIDER=azure-openai  PLATFORM_LLM_MODEL=gpt-5-mini
```

Fallback: minimax → azure-openai → azure-ai. Cooldown 90s on 429.
Keys: `~/.config/factory/*.key` — NEVER `*_API_KEY=dummy`
MiniMax: <think> consume tokens (min 16K). GPT-5-mini: NO temperature, max_completion_tokens≥8K.

## AZURE

```
VM:  <AZURE_VM_IP> (D4as_v5 4CPU/16GB, francecentral) — SSH architekt@<VM>, nginx basic auth
     Container: deploy-platform-1, path /app/architekt_platform/ (*), volume deploy_platform-data at /app/data
     Active compose: /opt/architekt/platform/deploy/docker-compose-vm.yml (context: /opt/architekt) (*)
     Patches: /opt/architekt/patches/ → copied at container start via start-with-patches.sh (*)
     (*) wave E complete — source in repo is platform/; image maps platform/ → architekt_platform/.
PG:  architekt-platform-pg.postgres.database.azure.com (*) — B1ms PG17 32GB, pgvector, pg_trgm
     DB: architekt_platform, user: architekt, SSL required, dual adapter (adapter.py) (*)
LLM: ascii-ui-openai (francecentral) — gpt-5-mini, 100req/min, 100K tok/min
DR:  L3 full 14/14 — blob GRS (architektbackups), snapshots, PG PITR 7d
     RPO: PG 24h+PITR 7d, SQLite 24h, VM 7d, secrets 24h, code 0 (git)
     RTO: PG 15min, SQLite 5min, VM 30min
     Cron: daily 3h, weekly dimanche 2h. Runbook: ops/RUNBOOK.md
```

## DEPLOY WORKFLOW

```
rsync /tmp → sudo cp (perms). Ou: docker exec -i CID tee /app/architekt_platform/PATH (*)
After: clear __pycache__ → docker restart → wait 15s → health check
(*) wave E complete package name. Templates: no restart (Jinja2 re-reads).
Auto-resume: lifespan restarts running missions on container restart.
```

## SECURITY

```
Auth: AuthMiddleware bearer (ARCHITEKT_API_KEY), GET public, mutations require token
Headers: HSTS, X-Frame DENY, CSP, X-XSS, Referrer strict
XSS: Jinja2 autoescaping, CSP connect-src 'self'
SQL: parameterized queries (? placeholders, zero f-strings)
Prompt injection: L0+L1 adversarial guards
Docker: non-root `architekt` user in image
Secrets: externalized ~/.config/factory/*.key, chmod 600
Rate limit: PG-backed per-IP+token, survives restart
```

## PLATFORM ARCHITECTURE

```
FastAPI + HTMX + Jinja2 + SSE | Architekt theme | SQLite/PostgreSQL dual
AgentLoop ←→ MessageBus (per-agent queues) → SSE → Frontend
AgentExecutor → LLM → tool calls → route via bus
Dual SSE: _push_sse() → _sse_queues (runner) + bus._sse_listeners (broadcast)
```

### 163 AGENTS (store.py + skills/definitions/*.yaml)

```
Dev (35+):     brain, lead_dev, dev_backend/frontend, workers, mobile_ios/android
QA (18+):      testeur, test_automation, perf-tester, fixture-gen, mobile_qa
Security (14+): securite, devsecops, pentester-lead, exploit-dev, license-scanner
Product (10+): product_owner, metier, business_owner, ao-compliance
Architecture (7+): architecte, enterprise_architect, adr-writer, iac-engineer
DevOps (8+):   devops, sre, pipeline_engineer, backup-ops, monitoring-ops, canary-deployer, data-migrator
Doc (3):       doc-writer (tech writer lead), changelog-gen, tech_writer
RSE (8+):      rse-dpo, rse-ethique-ia, rse-eco, rse-a11y, rse-audit-social
SAFe (6):      rte, epic_owner, lean_portfolio_manager, solution_train_engineer
Architekt (10+): architekt-* studio skills (product, delivery, compliance, …)
```

### 41 WORKFLOWS (builtins.py)

```
Lifecycle:     product-lifecycle (11 phases), feature-sprint (5), feature-request (6)
DSI:           dsi-platform-features (9), dsi-platform-tma (6)
Security:      security-hacking (8), sast-continuous (4)
TMA:           tma-maintenance (4), tma-autoheal (4)
SAFe:          pi-planning (5), epic-decompose (5)
Mobile:        mobile-ios-epic (5), mobile-android-epic (5)
Quality:       documentation-pipeline (6), performance-testing (5), license-compliance (4)
Compliance:    rse-compliance (7), ao-compliance (5)
Ops:           cicd-pipeline (4), monitoring-setup (5), chaos-scheduled (5),
               canary-deployment (5), backup-restore (4)
Data:          data-migration (7), test-data-pipeline (4), i18n-validation (4)
Infra:         iac-pipeline (5)
Other:         tech-debt-reduction (5), review-cycle (2), sf-pipeline (3),
               migration-sharelook (8)
```

### 15 PATTERNS (12 in DB + 3 engine-only)

DB: solo-chat, sequential, parallel, hierarchical, router, aggregator,
human-in-the-loop, adversarial-pair, adversarial-cascade, debate, sf-tdd, wave
Engine-only: solo, loop, network

### ADVERSARIAL (Team of Rivals — arXiv:2601.14351)

```
L0: deterministic (test.skip, @ts-ignore, empty catch) → VETO ABSOLU
L1: LLM semantic (SLOP, hallucination, logic) → VETO ABSOLU
L2: architecture (RBAC, validation, API design) → VETO + ESCALATION
Multi-vendor: Brain=Opus, Worker=MiniMax, Security=GLM, Arch=Opus
Rule: "Code writers cannot declare their own success"
Retry: 5 attempts max → NodeStatus.FAILED
CoVe (arXiv:2309.11495): 4-stage anti-hallucination (Draft→Verify→Answer→Final)
```

### MISSION CONTROL (11 phases)

```
1.Idéation(network) 2.Comité(HITL) 3.Constitution(seq) 4.Archi(aggregator)
5.Sprints(hierarchical) 6.CI/CD(seq) 7.QA(loop) 8.Tests(parallel)
9.Deploy(HITL) 10.TMA Routage(router) 11.Correctif(loop)
Semaphore: 2 concurrent missions. Phase timeout: 600s. Reloop max 2x.
```

### SAFe (~7/10)

WSJF real calc, sprint auto-creation, feature pull PO, velocity tracking.
Gates GO/NOGO/PIVOT. Learning loop + I&A retrospective. Error reloop max 2x.

### PRODUCT MANAGEMENT

```
Hierarchy: Epic(mission) → Feature → UserStory
WSJF: 4 components → CoD/JD auto-compute. Slider UI.
Kanban: SortableJS drag-drop. Sprint planning: assign/unassign stories.
Dependencies: feature_deps table + visual 🔗 badges.
Charts: Chart.js velocity, burndown, cycle time histogram, Gantt.
```

### REST API (dual JSON + form via _parse_body)

```
POST /api/projects, /api/missions, /api/missions/{id}/start, /api/missions/{id}/run
POST /api/missions/{id}/wsjf, /api/missions/{id}/sprints, /api/missions/{id}/validate
POST /api/epics/{id}/features, /api/features/{id}/stories, /api/features/{id}/deps
PATCH /api/features/{id}, /api/stories/{id}, /api/tasks/{id}/status, /api/backlog/reorder
GET /api/sprints/{id}/available-stories, /api/features/{id}/deps, /api/releases/{pid}
GET /api/metrics/cycle-time, /api/llm/stats, /api/llm/traces, /api/health
GET /api/agents, /api/sessions, /api/mcps, /api/monitoring/live
DELETE /api/features/{id}/deps/{dep}, /api/sprints/{id}/stories/{id}
Swagger: /docs (FastAPI auto-generated)
```

### MCP

```
MCP LRM (port 9500): lrm_locate/read/conventions/task_*/build, confluence, jira
MCP Platform (port 9501): agents/missions/phases/messages/memory/git/code/metrics
MCP Servers: fetch (pip), memory-kg (npx), playwright (npx, Chrome :9222)
Agent tools: mcp_fetch_fetch, mcp_memory_*, mcp_playwright_* in tool_schemas.py
Dispatch: tool_runner.py _tool_mcp_dynamic() → parse mcp_<server>_<tool> → JSON-RPC
```

### MEMORY

4-layer: session → pattern → project → global (FTS5/tsvector)
Wiki `/memory`, confidence bars. Retrospectives → LLM → lessons → global.

### MONITORING

DORA: deploy freq, lead time, CFR, MTTR + velocity + sparklines.
LLM: per-call tracing (provider, model, tokens, cost). Live: `/monitoring` SSE.
OpenTelemetry: opt-in via `OTEL_ENABLED=1`. Exports to Jaeger/OTEL collector via OTLP/HTTP.
  Env vars: `OTEL_ENABLED=1`, `OTEL_SERVICE_NAME=architekt-prod` (or legacy `architekt-prod` on Azure),
  `OTEL_EXPORTER_OTLP_ENDPOINT=http://jaeger:4317`
  Jaeger UI: http://localhost:16686 (traces, spans, latency).
  Requires: `pip install opentelemetry-api opentelemetry-sdk opentelemetry-instrumentation-fastapi opentelemetry-exporter-otlp-proto-http`

### DASHBOARDS

DSI/CTO `/dsi`, Métier `/metier` (SAFe value stream), Portfolio `/`, Board `/projects/{id}/board`
Ideation `/ideation` → 5 agents network debate → "Créer Epic"
Analytics `/analytics` — Chart.js: skills, missions, agents leaderboard, system health

## KEY FILES (all under platform/)

```
server.py, models.py, config.py
llm/client.py, llm/observability.py
a2a/bus.py, a2a/negotiation.py, a2a/veto.py
agents/loop.py, agents/executor.py, agents/store.py, agents/tool_schemas.py
patterns/engine.py, patterns/store.py
missions/store.py, missions/product.py
sessions/store.py, sessions/runner.py
workflows/builtins.py, workflows/store.py
memory/manager.py, memory/vectors.py
db/adapter.py, db/migrations.py, db/schema_pg.sql
tools/tool_runner.py, tools/code_tools.py, tools/mcp_bridge.py
web/routes/{helpers,pages,missions,projects,agents,sessions,patterns,workflows,metrics,settings}.py
ops/auto_heal.py, ops/chaos_endurance.py, ops/run_backup.py
mcps/manager.py
cli/sf.py, cli/_api.py, cli/_db.py, cli/_output.py, cli/_stream.py
```

## DB

`data/platform.db` (repo `data/`). Dual: `DATABASE_URL` → PG, absent → SQLite.
⚠️ NEVER `rm -f data/platform.db`. ⚠️ NEVER `*_API_KEY=dummy`.

## CONVENTIONS

- ⛔ ZERO SKIP: NEVER test.skip/@ts-ignore/#[ignore] — FIX > SKIP
- Adversarial 100% LLM (never regex)
- HTMX: readyState check (not DOMContentLoaded). Enum: `_s(val)` helper.
- Process cleanup: start_new_session=True + os.killpg() on timeout

## EXTERNAL TOOLS WATCHLIST

| Outil | Repo | Pourquoi | Statut |
|-------|------|----------|--------|
| **rtk** (Rust Token Killer) | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | CLI proxy Rust, réduit 60-90% tokens LLM sur git/test/grep — intégrer dans `tool_runner.py` + wrappers agents | 🔭 watch |

### rtk — notes d'intégration
- **Approche hook** : `~/.claude/settings.json` `PreToolUse` → transparent pour Claude Code. Pas applicable server-side.
- **Approche plateforme** : wrapper dans `platform/tools/git_tools.py`, `test_tools.py`, `build_tools.py` — détecter si `rtk` est dans PATH, préfixer les commandes.
- **Patterns à récupérer** : logique de compression `cargo_cmd.rs`, `diff_cmd.rs`, `grep_cmd.rs` → portage Python dans `platform/tools/`.
- **Install local** : `curl -fsSL https://raw.githubusercontent.com/rtk-ai/rtk/refs/heads/master/install.sh | sh`
- **Version analysée** : v0.22.2 (fév 2026) — 1572 ⭐, 115 forks

## AUDIT COVERAGE (46/46 = 100%)

```
Stabilité:        chaos-scheduled, tma-autoheal, monitoring-setup, canary-deployment ✓
Maintenabilité:   tech-debt-reduction, review-cycle, adversarial cascade ✓
Lisibilité:       documentation-pipeline (API docs, ADR, changelog, onboarding) ✓
Légalité:         rse-compliance (RGPD, AI Act), license-compliance (SBOM), ao-compliance (CCTP/PV recette) ✓
Sécurité:         security-hacking (8 phases), sast-continuous, secrets scan, pentest ✓
Reproductibilité: cicd-pipeline, feature-sprint TDD, iac-pipeline, test-data-pipeline ✓
Déploiement:      canary-deployment (1%→10%→50%→100% + HITL), cicd-pipeline, mobile epics ✓
Documentation:    documentation-pipeline (6 phases: API→ADR→changelog→user→onboarding→review) ✓
Data:             backup-restore (RPO/RTO + DR runbook), data-migration (7 phases + HITL GO/NOGO) ✓
Performance:      performance-testing (k6 load→analysis→fix loop→report) ✓
i18n:             i18n-validation (hardcoded scan, translation check, RTL, format) ✓
Accessibilité:    rse-a11y agent + rse-compliance a11y-audit phase ✓
RSE/Green IT:     rse-compliance (eco + social + ethical AI audit) ✓
SAFe:             pi-planning + epic-decompose (ART, portfolio, WSJF) ✓
```

## DOC INDEX

Studio and rebrand docs: `docs/architekt/README.md`.
