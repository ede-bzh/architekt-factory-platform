---
name: Architekt Tech
description: Doctrine technique Architekt — TDD, mutation testing ciblé, 12-Factor, CI (ADR-003)
tags: [tech, architekt, tdd, mutation-testing, ci]
metadata:
  category: tech
  triggers: [build, test, tdd, mutation, ci, refactor]
---

# Architekt Tech

## Objectif

Encoder la **doctrine technique Architekt** : TDD, tests réels (pas coverage théâtre), mutation testing ciblé, 12-Factor — pour livrer du code maintenable et prouvable.

## Quand utiliser

- Phase Build (développement features)
- Revue PR / CI
- Refactoring ou dette technique
- Setup repo nouveau projet client

## TDD — règles

- **Red → Green → Refactor** sur toute logique métier
- Tests avant ou avec le code (jamais "on testera après")
- **ZERO SKIP** : pas de `test.skip`, `@ts-ignore`, `#[ignore]` — corriger
- CI verte = merge bloquant

## Mutation testing (ADR-003) — politique nuancée

| Périmètre | Politique | Outil | Seuil CI |
|-----------|-----------|-------|----------|
| Moteurs critiques (auth, paiement, calcul métier) | **Obligatoire** | Stryker / mutmut / PIT | 60% → 70% → 80% |
| Logique métier standard | Recommandé | Idem | Progressif |
| UI / templates / glue | Optionnel | — | — |
| Code généré / utilitaires triviaux | **Exclu** | — | — |

**Mode** : PR = `--incremental` (fichiers changés) ; nightly = run complet.

## Outils par stack

| Stack | Tests | Mutation | Lint |
|-------|-------|----------|------|
| JS/TS | Vitest | Stryker | ESLint |
| Python | pytest | mutmut | ruff |
| Java | JUnit | PIT | Checkstyle |
| Rust | cargo test | cargo-mutants | clippy |

## 12-Factor (baseline)

- Config via env vars (pas hardcodé)
- Logs stdout (agrégés en prod)
- Processes stateless ; état en DB/cache
- Dev/prod parity (Docker)
- Dependencies explicites (lockfiles pin exact)
- Disposability (graceful shutdown)

## Intégration plateforme

- Phase QA workflow : `test` puis `mutation_test` sur modules critiques
- Gate adversarial L2 : score mutation < seuil → veto
- Agent dev : explorer (`list_files`, `deep_search`) avant `code_write`

## Anti-patterns

- ❌ Coverage 100% avec assertions vides
- ❌ Mutation testing partout (théâtre qualité)
- ❌ Fake build scripts / BUILD SUCCESS hardcodé
- ❌ Seuil 80% dès le mois 1 (frustration)
- ❌ Ignorer mutants survivants sur auth/paiement

## Sources

- ADR-003 Mutation testing
- Heroku 12-Factor App
- Stryker Mutator, mutmut, PIT documentation
