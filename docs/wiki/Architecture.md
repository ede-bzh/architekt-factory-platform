# Architecture

## Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                        PLATFORM (FastAPI)                       │
│  ┌──────────┐  ┌───────────┐  ┌───────────┐  ┌──────────────┐ │
│  │  Web UI   │  │   REST    │  │    SSE    │  │     CLI      │ │
│  │  (HTMX)   │  │   API     │  │  Stream   │  │   (sf.py)    │ │
│  └─────┬─────┘  └─────┬─────┘  └─────┬─────┘  └──────┬───────┘ │
│        └──────────┬────┴────────┬─────┘              │         │
│              ┌────┴────┐  ┌────┴────┐                │         │
│              │  Routes  │  │ Helpers │                │         │
│              └────┬────┘  └─────────┘                │         │
│  ┌────────────────┴──────────────────────────────────┘         │
│  │                                                              │
│  │  ┌──────────────┐  ┌───────────────┐  ┌────────────────┐   │
│  │  │  AgentLoop    │  │  MessageBus   │  │  PatternEngine │   │
│  │  │  (executor)   │←→│  (pub/sub)    │←→│  (15 patterns) │   │
│  │  └──────┬───────┘  └───────────────┘  └────────────────┘   │
│  │         │                                                    │
│  │  ┌──────┴───────┐  ┌───────────────┐  ┌────────────────┐   │
│  │  │  LLM Client  │  │  Tool Runner  │  │  MCP Bridge    │   │
│  │  │  (multi-prov) │  │  (50+ tools)  │  │  (3 servers)   │   │
│  │  └──────────────┘  └───────────────┘  └────────────────┘   │
│  │                                                              │
│  │  ┌──────────────┐  ┌───────────────┐  ┌────────────────┐   │
│  │  │  Missions    │  │  Workflows    │  │  Memory        │   │
│  │  │  (SAFe)      │  │  (41 builtin) │  │  (4-layer)     │   │
│  │  └──────────────┘  └───────────────┘  └────────────────┘   │
│  └──────────────────────────────────────────────────────────────│
│                                                                 │
│  ┌──────────────┐  ┌───────────────┐  ┌────────────────────┐  │
│  │  SQLite/PG   │  │  OTEL/Jaeger  │  │  Ops (auto-heal)   │  │
│  │  (dual DB)   │  │  (tracing)    │  │  (chaos/endurance)  │  │
│  └──────────────┘  └───────────────┘  └────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.12, FastAPI, uvicorn |
| Frontend | HTMX, Jinja2, Chart.js, SortableJS |
| Database | SQLite (local) / PostgreSQL (prod), dual adapter |
| LLM | Multi-provider: MiniMax, Azure OpenAI, Azure AI |
| Streaming | SSE (Server-Sent Events), dual channel |
| Monitoring | OpenTelemetry → Jaeger, DORA metrics |
| CI/CD | GitHub Actions, Docker, Helm |
| MCP | 3 servers: fetch, memory-kg, playwright |

## Agent Architecture

160+ agents organized in multiple domains:

| Domain | Count | Key Agents |
|--------|-------|------------|
| Dev | 35+ | brain, lead_dev, dev_backend, dev_frontend, workers |
| QA | 18+ | testeur, test_automation, perf-tester |
| Security | 14+ | securite, devsecops, pentester-lead |
| Product | 10+ | product_owner, metier, business_owner |
| Architecture | 7+ | architecte, enterprise_architect, adr-writer |
| DevOps | 8+ | devops, sre, pipeline_engineer |
| Doc | 3 | doc-writer, changelog-gen, tech_writer |
| RSE | 8+ | rse-dpo, rse-ethique-ia, rse-eco, rse-a11y |
| SAFe | 6 | rte, epic_owner, lean_portfolio_manager |

## Adversarial Validation (Team of Rivals)

```
L0: deterministic checks (test.skip, @ts-ignore, empty catch) → VETO
L1: LLM semantic review (slop, hallucination, logic)         → VETO
L2: architecture review (RBAC, validation, API design)       → VETO + ESCALATION
Multi-vendor: Brain=Opus, Worker=MiniMax, Security=GLM, Arch=Opus
Rule: "Code writers cannot declare their own success"
```

## 🇫🇷 [Architecture (FR)](Architecture‐FR) · 🇪🇸 [ES](Architecture‐ES) · 🇩🇪 [DE](Architecture‐DE)
