# Architekt Factory Platform — Wiki

**Architekt Factory Platform** orchestre des agents IA spécialisés pour les équipes de livraison logicielle. Elle coordonne **160+ agents** via **41 workflows intégrés** en méthodologie SAFe.

> Feuille de route : [docs/ROADMAP.md](../ROADMAP.md)

## Navigation

| Section | Description |
|---------|-------------|
| [Architecture](Architecture) | Architecture, composants, flux |
| [Guide de déploiement](Deployment-Guide) | Local, démo OVH, prod Azure |
| [Référence API](API-Reference) | Endpoints REST, authentification |
| [Agents](Agents) | Catalogue d'agents |
| [Workflows](Workflows) | Modèles de workflows |
| [Patterns](Patterns) | Patterns d'orchestration |
| [Sécurité](Security) | Auth, garde adversarial, secrets |
| [Configuration LLM](LLM-Configuration) | Fournisseurs et routage |
| [Darwin Teams](Darwin-Teams) | Sélection évolutive d'équipes |

## Langues (interface)

🇬🇧 [English](Home) · 🇫🇷 Français

## Démarrage rapide

```bash
git clone https://github.com/ede-bzh/architekt-factory-platform.git
cd architekt-factory-platform
make setup
make run
# http://localhost:8090 — bouton "Skip (Demo)" ou PLATFORM_LLM_PROVIDER=demo
```
