# Architekt Agent Platform — Wiki

**Architekt Agent Platform** is an AI-powered agent orchestration platform for software engineering teams. It coordinates 163 specialized agents through 41 workflows using SAFe methodology.

> **Latest release: [v2.3.0](https://github.com/macaron-software/software-factory/releases/tag/v2.3.0)** — CI gates, monitoring refactor, adaptive intelligence (GA + RL LIVE)

## Adaptive intelligence (LIVE)

Three layers optimize agent and workflow performance — see [`platform/CLAUDE.md` § Adaptive Intelligence](../../platform/CLAUDE.md#adaptive-intelligence--thompson-sampling--ga--rl):

| Layer | Status | Mechanism |
|-------|--------|-----------|
| Thompson Sampling | **LIVE** | Per-agent-slot runtime selection (`platform/agents/selection.py`) |
| Genetic Algorithm | **LIVE** | Nightly workflow evolution at 02:00 UTC (`evolution_scheduler.py`) |
| Reinforcement Learning | **LIVE** | Mid-mission pattern adaptation via `rl_hooks` in `patterns/engine.py` |

## Navigation

| Section | Description |
|---------|-------------|
| [Architecture](Architecture) | Platform architecture, components, data flow |
| [Deployment Guide](Deployment-Guide) | 3 environments: Azure, OVH, Local |
| [API Reference](API-Reference) | REST API endpoints, authentication |
| [Agents](Agents) | 163 agents across 9 domains |
| [Workflows](Workflows) | 41 built-in workflows |
| [Patterns](Patterns) | 15 orchestration patterns |
| [Security](Security) | Auth, adversarial validation, secrets |
| [LLM Configuration](LLM-Configuration) | Multi-model routing, Darwin LLM A/B, providers |
| [Darwin Teams](Darwin-Teams) | Evolutionary team selection + GA/RL adaptive intelligence |

## Translations

🇫🇷 [Français](Home‐FR) · 🇪🇸 [Español](Home‐ES) · 🇩🇪 [Deutsch](Home‐DE) · 🇮🇹 [Italiano](Home‐IT) · 🇧🇷 [Português](Home‐PT) · 🇨🇳 [中文](Home‐ZH) · 🇯🇵 [日本語](Home‐JA)

## Quick Start

```bash
git clone https://github.com/macaron-software/software-factory.git
cd software-factory
make setup
make run
# → http://localhost:8090
```

## Repositories

| Repo | Purpose | Content |
|------|---------|---------|
| **GitHub** (macaron-software/software-factory) | Public, full platform | All code, agents, workflows. Sanitized: 0 project data, 0 personal info |
| **GitLab La Poste** (gitlab.azure.<gitlab-laposte>) | Internal skeleton | Platform structure, no missions, no agent skills, CI/CD integration |

## License

AGPL-3.0 — See [LICENSE](https://github.com/macaron-software/software-factory/blob/main/LICENSE)
