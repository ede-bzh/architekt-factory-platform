# Phase 2 — Doctrine bonnes pratiques Architekt

> Durée cible : **1 semaine**
> Dépend de : Phase 1 (ADR écrits)
> Sortie : 6 skills + CI plateforme

## Objectif

Encoder les pratiques Architekt en **skills** chargés par les agents IA + mettre la **CI plateforme** au vert.

## Livrables — 6 skills doctrine

| Fichier | Sujet | Contenu clé |
|---------|-------|-------------|
| `skills/architekt-archi.md` | Architecture | Modular monolith (ADR-002), ADR obligatoire, C4 |
| `skills/architekt-tech.md` | Engineering | TDD, mutation testing (ADR-003), 12-Factor |
| `skills/architekt-ux.md` | UX/UI | shadcn+Radix+Tailwind v4 (ADR-004), WCAG 2.2 AA |
| `skills/architekt-data.md` | Données | PostgreSQL, migrations, RPO/RTO, FTS |
| `skills/architekt-security.md` | Sécurité | SAST, OWASP, secrets vault, fail-closed |
| `skills/architekt-sre.md` | SRE | SLO, error budget, runbook, OTEL |

Format identique à `skills/tdd.md` existant (front-matter YAML + corps Markdown).

## Livrables — CI plateforme (bloquant Phase 3)

- [ ] `.github/workflows/ci.yml` : pytest + ruff + bandit sur chaque PR
- [ ] `Makefile test` corrigé (fichiers réels)
- [ ] Badge CI vert sur README
- [ ] Mutation testing Python sur plateforme elle-même (mutmut, seuil 50% au départ)

## Squelette CI (`.github/workflows/ci.yml`)

```yaml
name: CI
on:
  pull_request:
    branches: [main]
  push:
    branches: [main]

jobs:
  python-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.12' }
      - run: pip install -e '.[dev]' pytest pytest-asyncio httpx fastapi uvicorn pyyaml ruff bandit
      - run: ruff check .
      - run: bandit -r platform/ skills_injection/ --severity-level medium
      - run: PYTHONPATH=$PWD pytest tests/ -q --tb=short
```

(à affiner selon ce qui passe vraiment vs ce qu'on ignore)

## Pré-requis

- Phase 1 mergée

## Gate de passage

- [ ] 6 skills mergés
- [ ] CI verte sur `main`
- [ ] Badge ajouté README
- [ ] Mutation testing Python lancé une fois, score baseline noté dans `docs/quality-baseline.md`
