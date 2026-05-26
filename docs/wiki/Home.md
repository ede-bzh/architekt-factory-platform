# 🏭 Architekt Factory — Wiki

**Architekt Factory** is an AI-powered agent orchestration platform for software engineering teams. It coordinates ~163 specialized agents through 41 workflows and 104 skills using SAFe methodology.

> **Latest release: [v2.3.0](https://github.com/ede-bzh/architekt-factory-platform/releases/tag/v2.3.0)** — Restructured Home + Dashboard navigation, CTO Jarvis strategic advisor

## Navigation

| Section | Description |
|---------|-------------|
| [Architecture](Architecture) | Platform architecture, components, data flow |
| [Deployment Guide](Deployment-Guide) | Architekt demo (OVH/local) and legacy Azure production |
| [API Reference](API-Reference) | REST API endpoints, authentication |
| [Agents](Agents) | ~163 agents across 9 domains |
| [Workflows](Workflows) | 41 built-in workflows |
| [Patterns](Patterns) | 15 orchestration patterns |
| [Security](Security) | Auth, adversarial validation, secrets |
| [LLM Configuration](LLM-Configuration) | Multi-model routing, Darwin LLM A/B, providers |
| [Darwin Teams](Darwin-Teams) | Evolutionary team selection + LLM Thompson Sampling |

## Languages

Documentation is available in **English** and **French** only.

## Quick Start

```bash
git clone https://github.com/ede-bzh/architekt-factory-platform.git
cd architekt-factory-platform
make setup
make run
# → http://localhost:8090
```

## License

AGPL-3.0 — See [LICENSE](https://github.com/ede-bzh/architekt-factory-platform/blob/main/LICENSE)
