# Backlog plateforme Architekt (hors projets clients)

Priorité actuelle : **outil interne studio** — rebrand, stabilité, CI, fonctionnalités manquantes.
Pas de site vitrine client en phase 0.

## Terminé (phase 0 merge)

- [x] `platform/branding.py` + globals Jinja
- [x] UI login / base / onboarding → Architekt
- [x] Provider LLM `demo` restauré (`_demo_response`)
- [x] `pytest.ini` + workflow `ci.yml` (CI basics)
- [x] `python-dotenv` dans `platform/requirements.txt`
- [x] `MACARON_API_KEY` → `ARCHITEKT_API_KEY` (alias 6 mois, `platform/auth/api_key.py`)
- [x] Skills Architekt compliance + i18n (`platform/skills/architekt/architekt-compliance.md`, `architekt-i18n.md`)
- [x] Quality gate CI : ruff + bandit sur `platform/` (`.github/workflows/ci.yml`)
- [x] Auth tests : `tests/test_api_key_alias.py` + gate `tests/test_platform_api.py` en CI
- [x] Route `/proof` — dashboard POC (health, quality, DORA)

## Prochain (ordre suggéré)

### Stabilité & qualité

- [ ] Réparer tests fractal / MCP ou les isoler derrière extras
- [ ] Mutation testing (ADR-003) — mutmut sur modules critiques
- [ ] E2E Playwright dans CI (smoke login + health)

### Rebrand niveau 2 (ADR-001)

- [ ] CLI `sf` → `architekt` (alias `sf`)
- [ ] README multilingues + wiki embarqué
- [ ] Métriques Prometheus : préfixe `architekt_*` (garder `macaron_*` en alias)

### Fonctionnalités manquantes / dette

- [ ] Dashboard `dashboard/` rebrand + health unifié
- [ ] Documenter run local : `PLATFORM_LLM_PROVIDER=demo make dev`

## Explicitement hors scope (pour l’instant)

- Site web commercial Architekt (Astro/Next)
- Packaging Docker `architekt_platform` (niveau 3 ADR)
- Premier client payant / démo GTM
