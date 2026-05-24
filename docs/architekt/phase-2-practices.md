# Phase 2 — Delivery Doctrine

> Durée cible : **1 semaine**
> Dépend de : Phase 1 (offres + catalogue OK)
> Sortie : **12 skills Architekt** + CI sécurité industrialisée

## Objectif

Encoder la doctrine Architekt en **skills chargés automatiquement** par les agents IA, et mettre la **CI plateforme** au vert avec **sécurité supply-chain** (NIST SSDF, OWASP ASVS, SBOM).

## Livrables — 12 skills doctrine

### Skills existants à enrichir

| Fichier | Sujet | Source clé |
|---------|-------|-----------|
| `skills/architekt-archi.md` | Modular monolith (ADR-002), ADR obligatoire, C4 | Shopify / Spring Modulith |
| `skills/architekt-tech.md` | TDD, mutation testing ciblé (ADR-003), 12-Factor | Heroku 12-factor |
| `skills/architekt-ux.md` | shadcn+Radix+Tailwind v4 (ADR-004), **WCAG 2.2 AA vérifié** | W3C WCAG 2.2 |
| `skills/architekt-data.md` | PostgreSQL, migrations, RPO/RTO, FTS, isolation client | NIST SP 800-53 RA |
| `skills/architekt-security.md` | **OWASP ASVS L1 par défaut, L2 données sensibles** + **NIST SSDF** + SBOM | OWASP / NIST 800-218 |
| `skills/architekt-sre.md` | SLO, error budget, runbook, OTEL | Google SRE book |

### Skills nouveaux (6 ajouts révision exécutive)

| Fichier | Sujet |
|---------|-------|
| `skills/architekt-delivery.md` | Phases discovery/build/hardening/handover, definition of done, scope rules, budget temps |
| `skills/architekt-product.md` | Discovery, jobs-to-be-done, hypothèses, métriques produit |
| `skills/architekt-finops.md` | Budget LLM/mission, coût infra max/client, marge cible 50 %, alertes |
| `skills/architekt-ai-governance.md` | Human approval (sécu/factu/infra/données client), agent audit logs, version logging |
| `skills/architekt-commercial.md` | Cycle commercial, qualification, devis, suivi opportunités |
| `skills/architekt-qa.md` | Mutation testing ciblé, a11y audit, perf, security scan |

Spécifications dans `docs/skills-spec/` (rédigées Phase 1, implémentées Phase 2).

## Livrables — CI sécurité

### CI baseline (bloquant Phase 3)

`.github/workflows/ci.yml` :

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
      - run: pip install -e '.[dev]' pytest pytest-asyncio httpx fastapi \
             uvicorn pyyaml ruff bandit safety mutmut
      - run: ruff check .
      - run: bandit -r platform/ skills_injection/ --severity-level medium
      - run: safety check  # SCA dependencies
      - run: PYTHONPATH=$PWD pytest tests/ -q --tb=short

  sbom:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Generate CycloneDX SBOM
        uses: anchore/sbom-action@v0
        with:
          format: cyclonedx-json
          output-file: sbom-cyclonedx.json
      - uses: actions/upload-artifact@v4
        with: { name: sbom, path: sbom-cyclonedx.json }

  secret-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with: { fetch-depth: 0 }
      - uses: trufflesecurity/trufflehog@main
        with: { extra_args: --only-verified }
```

### Mutation testing — politique nuancée (ADR-003 révisé)

| Périmètre | Politique |
|-----------|-----------|
| Moteurs critiques (paiement, auth, calcul métier) | **Obligatoire** (Stryker / mutmut / PIT) |
| Logique métier standard | **Recommandé**, seuil progressif |
| UI / templates / glue | **Optionnel** |
| Code généré / utilitaires triviaux | **Exclu** |

→ Évite le théâtre qualité (cf. R19).

Seuils progressifs (sur modules critiques uniquement) :

- Mois 1 : 50 %
- Mois 3 : 70 %
- Mois 6 : 80 %

## Plan en 5 jours

| Jour | Action |
|------|--------|
| J1 | 6 skills existants enrichis (rédaction selon spec) |
| J2 | 6 skills nouveaux rédigés |
| J3 | CI baseline (`.github/workflows/ci.yml`) + corrections tests |
| J4 | SAST (bandit) + SCA (safety) + secret scan (trufflehog) actifs |
| J5 | SBOM CycloneDX + mutation testing modules critiques + badge README |

## Pré-requis

- Phase 1 mergée
- Spécifications skills (`docs/skills-spec/`) écrites Phase 1

## Gate de passage

- [ ] 12 skills mergés
- [ ] CI verte sur `main`
- [ ] SAST + SCA + secret scanning actifs sur PR
- [ ] SBOM CycloneDX généré au build (artefact)
- [ ] Mutation testing actif sur modules critiques (seuil 50 %)
- [ ] Badge CI ajouté README
- [ ] Baseline qualité documentée dans `docs/quality-baseline.md`

## Sources

- DORA 2025 : "AI is an amplifier, foundation matters"
- NIST SP 800-218 SSDF v1.1 (févr. 2022), v1.2 IPD (déc. 2025)
- OWASP ASVS v5 (niveaux 1/2/3)
- CycloneDX & SPDX formats SBOM
- Stryker Mutator, mutmut, PIT
