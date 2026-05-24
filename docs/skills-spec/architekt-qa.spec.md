# Spec : architekt-qa

> Skill cible : `skills/architekt-qa.md`
> ADR référents : ADR-003, ADR-014, ADR-015

## Objectif

Encoder la **stratégie QA Architekt** : tests, mutation testing ciblé, a11y, performance, sécurité — tout ce qui finit dans le **Quality Report**.

## Quand utiliser

- Phase Hardening de chaque mission
- À chaque PR (CI automatique)
- Avant chaque go-live
- Lors d'incident en production

## Périmètre QA

| Domaine | Outil | Cible |
|---------|-------|-------|
| Tests unitaires | Vitest / pytest / JUnit | Coverage > 70 % |
| Tests E2E | Playwright | Parcours critiques OK |
| Mutation testing | Stryker / mutmut / PIT | **Modules critiques** seulement (cf. ADR-003) |
| A11y | axe-core + Pa11y + manuel | WCAG 2.2 AA (ADR-014) |
| Performance | Lighthouse + k6 | Lighthouse perf ≥ 95, p95 < 800ms |
| Sécurité | Bandit + Safety + trufflehog + ZAP | 0 finding critique |
| SBOM | Syft + CycloneDX | Généré à chaque release |

## Mutation testing : politique nuancée (ADR-003)

| Périmètre | Mutation testing |
|-----------|------------------|
| Moteurs critiques (paiement, auth, calcul métier) | **Obligatoire**, seuil 60 → 70 → 80 % |
| Logique métier standard | Recommandé, seuil progressif |
| UI / templates | Optionnel |
| Glue / utilities | Exclu |

→ Évite le théâtre qualité.

## Process Hardening (1-2 semaines avant livraison)

| Jour | Action |
|------|--------|
| H1 | Audit dépendances (SAST + SCA) |
| H2 | Audit a11y (axe-core + manuel) |
| H3 | Tests perf (Lighthouse + k6 sur parcours critiques) |
| H4 | Pentest interne (sast-continuous workflow) |
| H5 | SBOM + signature + doc release |
| H6 | Bug fixing + retry |
| H7 | Validation client (UAT) |
| H8 | Quality Report généré + revu |
| H9-10 | Buffer / hotfix |

## Quality Report (cf. ADR-015)

Généré à la fin de chaque mission :
- 10 dimensions scorecard
- DORA metrics
- SBOM annexe
- Recommandations roadmap 3/6/12 mois
- Format : PDF + Markdown + JSON

## Gates de qualité (bloquants merge / deploy)

| Niveau | Gate |
|--------|------|
| PR merge | CI verte (lint + tests + SAST + secret scan) |
| Pre-staging | Coverage > 70 %, mutation score critiques > 60 % |
| Pre-prod | Lighthouse ≥ 95, a11y AA, SBOM signed, pentest OK |
| Post-prod | Monitoring 24h sans P1/P2 |

## Anti-patterns

- ❌ Skipper les tests "pour aller vite" (interdit par règle workspace existante)
- ❌ Mutation testing partout (théâtre)
- ❌ Présumer shadcn = a11y conforme (ADR-014)
- ❌ Pas de SBOM = pas de release
- ❌ Quality Report bidon (ne pas tricher sur les scores)

## Sources

- ADR-003 (Mutation testing)
- ADR-014 (A11y WCAG 2.2 AA)
- ADR-015 (Quality Report)
- DORA 2025 (foundation matters)
