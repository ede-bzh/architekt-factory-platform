# Architekt Agent Platform — Wiki

**Architekt Agent Platform** est une plateforme d'orchestration d'agents IA pour les équipes de développement logiciel. Elle coordonne 163 agents spécialisés à travers 41 workflows en méthodologie SAFe.

> **Dernière release : [v2.3.0](https://github.com/macaron-software/software-factory/releases/tag/v2.3.0)** — gates CI, monitoring refactor, intelligence adaptive (GA + RL LIVE)

## Intelligence adaptive (LIVE)

Trois couches optimisent la performance agents/workflows — voir [`platform/CLAUDE.md` § Adaptive Intelligence](../../platform/CLAUDE.md#adaptive-intelligence--thompson-sampling--ga--rl) :

| Couche | Statut | Mécanisme |
|--------|--------|-----------|
| Thompson Sampling | **LIVE** | Sélection runtime par slot agent (`platform/agents/selection.py`) |
| Algorithme génétique (GA) | **LIVE** | Évolution nocturne des workflows à 02:00 UTC (`evolution_scheduler.py`) |
| Reinforcement Learning (RL) | **LIVE** | Adaptation mid-mission via `rl_hooks` dans `patterns/engine.py` |

## Navigation

| Section | Description |
|---------|-------------|
| [Architecture](Architecture) | Architecture de la plateforme, composants, flux de données |
| [Guide de déploiement](Deployment-Guide) | 3 environnements : Azure, OVH, Local |
| [Référence API](API-Reference) | Endpoints REST, authentification |
| [Agents](Agents) | 163 agents répartis en 9 domaines |
| [Workflows](Workflows) | 41 workflows intégrés |
| [Patterns](Patterns) | 15 patterns d'orchestration |
| [Sécurité](Security) | Auth, validation adversariale, secrets |
| [Configuration LLM](LLM-Configuration) | Configuration multi-fournisseur LLM |
| [Darwin Teams](Darwin-Teams) | Sélection évolutive + intelligence adaptive GA/RL |

## Traductions

🇬�� [English](Home) · 🇪🇸 [Español](Home‐ES) · 🇩🇪 [Deutsch](Home‐DE) · 🇮🇹 [Italiano](Home‐IT) · 🇧🇷 [Português](Home‐PT) · ��🇳 [中文](Home‐ZH) · 🇯🇵 [日本語](Home‐JA)

## Démarrage rapide

```bash
git clone https://github.com/macaron-software/software-factory.git
cd software-factory
make setup
make run
# → http://localhost:8090
```

## Dépôts

| Dépôt | Usage | Contenu |
|-------|-------|---------|
| **GitHub** (macaron-software/software-factory) | Public, plateforme complète | Tout le code, agents, workflows. Assaini : 0 donnée projet, 0 info personnelle |
| **GitLab La Poste** (gitlab.azure.innovation-laposte.io) | Squelette interne | Structure plateforme, pas de missions, pas de skills agent, intégration CI/CD |

## Licence

AGPL-3.0 — Voir [LICENSE](https://github.com/macaron-software/software-factory/blob/main/LICENSE)
