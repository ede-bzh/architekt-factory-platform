---
name: Architekt QA
description: Stratégie QA Architekt — tests, mutation ciblé, a11y, perf, Quality Report (ADR-003, ADR-014, ADR-015)
tags: [qa, architekt, testing, quality-report, hardening]
metadata:
  category: qa
  triggers: [hardening, quality-report, e2e, lighthouse, mutation]
---

# Architekt QA

## Objectif

Encoder la **stratégie QA Architekt** : tests, mutation ciblé, a11y, perf, sécurité — livrable **Quality Report** en fin de mission.

## Quand utiliser

- Phase Hardening
- Chaque PR (CI)
- Avant go-live
- Incident production post-livraison

## Périmètre QA

| Domaine | Outil | Cible |
|---------|-------|-------|
| Unitaires | Vitest / pytest / JUnit | Coverage > 70% |
| E2E | Playwright | Parcours critiques OK |
| Mutation | Stryker / mutmut / PIT | **Modules critiques** seulement |
| A11y | axe-core + Pa11y + manuel | WCAG 2.2 AA |
| Performance | Lighthouse + k6 | Perf ≥ 95, p95 < 800ms |
| Sécurité | Bandit + Safety + trufflehog + ZAP | 0 critique |
| SBOM | Syft + CycloneDX | Chaque release |

## Mutation testing nuancé (ADR-003)

| Périmètre | Politique |
|-----------|-----------|
| Auth, paiement, calcul métier | **Obligatoire** 60→70→80% |
| Logique métier standard | Recommandé |
| UI / templates | Optionnel |
| Glue / utilities | Exclu |

## Process Hardening (1-2 semaines)

| Jour | Action |
|------|--------|
| H1 | SAST + SCA dépendances |
| H2 | Audit a11y |
| H3 | Perf Lighthouse + k6 |
| H4 | Pentest interne |
| H5 | SBOM + doc release |
| H6 | Bug fixing |
| H7 | UAT client |
| H8 | Quality Report |
| H9-10 | Buffer / hotfix |

## Quality Report (ADR-015)

Fin de mission : scorecard 10 dimensions, DORA metrics, SBOM annexe, recommandations 3/6/12 mois — PDF + Markdown + JSON.

## Gates bloquants

| Niveau | Gate |
|--------|------|
| PR merge | CI verte (lint + tests + SAST + secrets) |
| Pre-staging | Coverage > 70%, mutation critiques > 60% |
| Pre-prod | Lighthouse ≥ 95, a11y AA, SBOM, pentest OK |
| Post-prod | Monitoring 24h sans P1/P2 |

## Anti-patterns

- ❌ Skip tests "pour aller vite" (interdit workspace)
- ❌ Mutation partout (théâtre)
- ❌ Présumer shadcn = a11y OK
- ❌ Release sans SBOM
- ❌ Quality Report avec scores truqués

## Sources

- ADR-003 Mutation testing
- ADR-014 A11y WCAG 2.2 AA
- ADR-015 Quality Report
- DORA 2025
