# Architekt Factory Platform — Wiki

**Architekt Factory Platform** orchestrates specialized AI agents for software delivery teams. It coordinates **160+ agents** through **41 built-in workflows** using SAFe methodology.

> Product roadmap: [docs/ROADMAP.md](../ROADMAP.md)

## Navigation

| Section | Description |
|---------|-------------|
| [Architecture](Architecture) | Platform architecture, components, data flow |
| [Deployment Guide](Deployment-Guide) | Local, OVH demo, Azure prod (Docker package `macaron_platform`) |
| [API Reference](API-Reference) | REST API endpoints, authentication |
| [Agents](Agents) | Agent catalog and domains |
| [Workflows](Workflows) | Built-in workflow templates |
| [Patterns](Patterns) | Orchestration patterns |
| [Security](Security) | Auth, adversarial validation, secrets |
| [LLM Configuration](LLM-Configuration) | Multi-model routing, providers |
| [Darwin Teams](Darwin-Teams) | Evolutionary team selection |

## Languages (UI)

🇬🇧 English (default) · 🇫🇷 [Français](Home‐FR)

## Quick Start

```bash
git clone https://github.com/ede-bzh/architekt-factory-platform.git
cd architekt-factory-platform
make setup
make run
# http://localhost:8090 — use "Skip (Demo)" or PLATFORM_LLM_PROVIDER=demo
```
