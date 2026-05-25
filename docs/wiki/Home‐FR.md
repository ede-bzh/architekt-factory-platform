# 🏭 Architekt Factory — Wiki

**Architekt Factory** est une plateforme d'orchestration d'agents IA pour les équipes de développement logiciel. Elle coordonne ~163 agents spécialisés à travers 41 workflows et 104 skills en méthodologie SAFe.

> **Dernière version : [v2.3.0](https://github.com/ede-bzh/architekt-factory-platform/releases/tag/v2.3.0)** — Navigation Home + Dashboard restructurée, conseiller stratégique CTO Jarvis

## Navigation

| Section | Description |
|---------|-------------|
| [Architecture](Architecture) | Architecture de la plateforme, composants, flux de données |
| [Guide de déploiement](Deployment-Guide) | 3 environnements : Azure, OVH, Local |
| [Référence API](API-Reference) | Endpoints REST, authentification |
| [Agents](Agents) | ~163 agents répartis en 9 domaines |
| [Workflows](Workflows) | 41 workflows intégrés |
| [Patterns](Patterns) | 15 patterns d'orchestration |
| [Sécurité](Security) | Auth, validation adversariale, secrets |
| [Configuration LLM](LLM-Configuration) | Configuration multi-fournisseur LLM |
| [Darwin Teams](Darwin-Teams) | Sélection évolutive d'équipes + Thompson Sampling LLM |

## Langues

La documentation est disponible en **anglais** et **français** uniquement.

## Démarrage rapide

```bash
git clone https://github.com/ede-bzh/architekt-factory-platform.git
cd architekt-factory-platform
make setup
make run
# → http://localhost:8090
```

## Licence

AGPL-3.0 — Voir [LICENSE](https://github.com/ede-bzh/architekt-factory-platform/blob/main/LICENSE)
