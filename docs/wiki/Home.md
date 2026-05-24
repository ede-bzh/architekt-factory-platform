# 🏭 Software Factory — Wiki

**Macaron Software Factory** is an AI-powered agent orchestration platform for software engineering teams. It coordinates 156 specialized agents through 36 workflows using SAFe methodology.

> **Latest release: [v2.2.0](https://github.com/macaron-software/software-factory/releases/tag/v2.2.0)** — Multi-Model LLM Routing + Darwin LLM Thompson Sampling

## Navigation

| Section | Description |
|---------|-------------|
| [Architecture](Architecture) | Platform architecture, components, data flow |
| [Deployment Guide](Deployment-Guide) | 3 environments: Azure, OVH, Local |
| [API Reference](API-Reference) | REST API endpoints, authentication |
| [Agents](Agents) | 156 agents across 9 domains |
| [Workflows](Workflows) | 36 built-in workflows |
| [Patterns](Patterns) | 15 orchestration patterns |
| [Security](Security) | Auth, adversarial validation, secrets |
| [LLM Configuration](LLM-Configuration) | Multi-model routing, Darwin LLM A/B, providers |
| [Darwin Teams](Darwin-Teams) | Evolutionary team selection + LLM Thompson Sampling |

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
| **GitHub** ([ede-bzh/architekt-factory-platform](https://github.com/ede-bzh/architekt-factory-platform)) | Public platform | All code, agents, workflows. Sanitized: 0 project data, 0 personal info |

## License

AGPL-3.0 — See [LICENSE](https://github.com/macaron-software/software-factory/blob/main/LICENSE)
