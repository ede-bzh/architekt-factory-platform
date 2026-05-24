# Backlog plateforme Architekt (hors projets clients)

Priorité actuelle : **outil interne studio** — rebrand, stabilité, CI, fonctionnalités manquantes.
Pas de site vitrine client en phase 0.

## En cours (PR phase 0)

- [x] `platform/branding.py` + globals Jinja
- [x] UI login / base / onboarding → Architekt
- [x] Provider LLM `demo` restauré (`_demo_response`)
- [x] `pytest.ini` + workflow `ci.yml`
- [x] `python-dotenv` dans `platform/requirements.txt`

## Prochain (ordre suggéré)

### Stabilité & qualité

- [ ] Faire passer **tous** les tests `tests/test_platform_api.py` (auth fixture, DB temp)
- [ ] Réparer tests fractal / MCP ou les isoler derrière extras
- [ ] Mutation testing (ADR-003) — mutmut sur modules critiques
- [ ] E2E Playwright dans CI (smoke login + health)

### Rebrand niveau 2 (ADR-001)

- [ ] `MACARON_API_KEY` → `ARCHITEKT_API_KEY` (alias 6 mois)
- [ ] CLI `sf` → `architekt` (alias `sf`)
- [ ] README multilingues + wiki embarqué
- [ ] Métriques Prometheus : préfixe `architekt_*` (garder `macaron_*` en alias)

### Fonctionnalités manquantes / dette

- [ ] Skills specs Architekt dans `skills/` (injections agents)
- [ ] Quality gate CI : ruff + bandit sur `platform/`
- [ ] Dashboard `dashboard/` rebrand + health unifié
- [ ] Documenter run local : `PLATFORM_LLM_PROVIDER=demo make dev`

## Explicitement hors scope (pour l’instant)

- Site web commercial Architekt (Astro/Next)
- Packaging Docker `architekt_platform` (niveau 3 ADR)
- Premier client payant / démo GTM
