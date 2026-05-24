# Backlog plateforme Architekt (hors projets clients)

Priorité actuelle : **outil interne studio** — rebrand, stabilité, CI, fonctionnalités manquantes.
Pas de site vitrine client en phase 0.

> **Alignement tiers** : P0 = Tier **S** · P1 = Tier **A** · P2 = Tier **B** · P3 = Tier **C**
> Catalogue complet : `docs/ROADMAP.md` § Catalogue features plateforme.

## Légende priorités

| Priorité | Tier | Phase cible | Règle |
|----------|------|-------------|-------|
| **P0** | S | 0–2 | Blocker — sans ça, pas de delivery ni de preuve client |
| **P1** | A | 2–4 | Différenciation — qualité, sécu, répétabilité |
| **P2** | B | 4–6 | Scale — après 3 clients payants |
| **P3** | C | 6–7+ | Optionnel — déclencheur explicite (10+ clients, SaaS) |

---

## Wave 2 — livré (P0 Tier S)

> Branche `cursor/architekt-roadmap-wave2-7576` — merge features + delivery P0.

- [x] Quality gate CI : ruff + bandit sur `platform/` (`.github/workflows/ci.yml`)
- [x] **`quality-report.pdf` POC** — export PDF mission (`platform/metrics/quality_pdf.py`, reportlab)
- [x] Auto-pause budget LLM à 100 % (`platform/llm/budget.py`, ADR-011)
- [x] Mini dashboard `/proof` — health, quality, DORA (`platform/web/templates/proof.html`)
- [x] Auth fail-closed `ARCHITEKT_API_KEY` + alias `MACARON_API_KEY` 6 mois (`platform/auth/api_key.py`)
- [x] Tests gate : `test_api_key_alias`, `test_llm_budget`, `test_quality_pdf`, `test_platform_api` en CI
- [x] Run local documenté : `docs/architekt/LOCAL-DEV.md` (`PLATFORM_LLM_PROVIDER=demo make dev`)
- [x] Skills Architekt compliance + i18n (`platform/skills/architekt/`)

---


---

## Wave 4 — livré (P1 observabilité & qualité)

> Branche `cursor/architekt-roadmap-wave4-7576`.

- [x] Adversarial **L2** déterministe (`check_l2` — secrets, eval, CORS, SQL f-string)
- [x] Métriques Prometheus **`architekt_*`** (alias `macaron_*` + `architekt_finops_margin_pct`)
- [x] FinOps marge studio — `PLATFORM_FINOPS_MARGIN_TARGET_PCT` (défaut 50 %), alertes `/finops`
- [x] API `GET /api/finops/summary` + `GET /api/missions/{id}/case-study.md`
- [x] Journal audit IA append-only (`ai_audit_logs` + hook `trace_call`)
- [x] Tests : `test_adversarial_l2`, `test_finops_margin`, `test_prometheus_architekt`, `test_ai_audit_logs`, `test_case_study`

## Wave 3 — livré (P1 Tier A)

> Branche `cursor/architekt-roadmap-wave3-7576` — FinOps mission costs + health probe.

- [x] FinOps `/finops` — per-mission cost table (GROUP BY `mission_id`, top 20 from `llm_traces`)
- [x] Health check `/api/health` — `version` + `timestamp` fields (`platform/web/routes/api/health.py`)
- [x] Tests health API : `tests/test_health_api.py` (200, status ok, version/timestamp)
- [x] Health section : `docs/architekt/LOCAL-DEV.md` § Health check

---

## Wave 2 — en cours

- [ ] CI verte 100 % sur `main` (gate merge)
- [ ] SAST + SCA + secret scan en CI (Safety, TruffleHog — Bandit déjà actif)
- [ ] SBOM CycloneDX par release (Syft)
- [ ] Adversarial L0 — veto test.skip / @ts-ignore / empty catch
- [ ] Faire passer **tous** les tests `tests/test_platform_api.py` (auth fixture, DB temp)
- [ ] Rate limiting PG-backed sur mutations

---

## P0 — Tier S (Phase 0–2)

### Rebrand & stabilité (Phase 0)

- [x] `platform/branding.py` + globals Jinja
- [x] UI login / base / onboarding → Architekt
- [x] Provider LLM `demo` restauré (`_demo_response`)
- [x] `pytest.ini` + workflow `ci.yml`
- [x] `python-dotenv` dans `platform/requirements.txt`
- [ ] Faire passer **tous** les tests `tests/test_platform_api.py` (auth fixture, DB temp)
- [x] Documenter run local : `PLATFORM_LLM_PROVIDER=demo make dev` → `docs/architekt/LOCAL-DEV.md`

### CI & quality gates (Phase 2)

- [ ] CI verte 100 % sur `main` (gate merge)
- [x] Quality gate CI : ruff + bandit sur `platform/`
- [ ] SAST + SCA + secret scan en CI (Bandit, Safety, TruffleHog)
- [ ] SBOM CycloneDX par release (Syft)
- [ ] Adversarial L0 — veto test.skip / @ts-ignore / empty catch
- [x] **`quality-report.pdf` POC** — export PDF mission (DORA, tests, SBOM)
- [x] Auto-pause budget LLM à 100 % (ADR-011)

### Auth & sécurité baseline

- [x] Auth fail-closed (`ARCHITEKT_API_KEY`) — alias `MACARON_API_KEY` 6 mois
- [ ] Rate limiting PG-backed sur mutations

---

## P1 — Tier A (Phase 2–4)

### Rebrand niveau 2 (ADR-001)

- [x] `MACARON_API_KEY` → `ARCHITEKT_API_KEY` (alias 6 mois)
- [ ] CLI `sf` → `architekt` (alias `sf`)
- [ ] README multilingues + wiki embarqué
- [ ] Métriques Prometheus : préfixe `architekt_*` (garder `macaron_*` en alias)

### Skills & agents Architekt

- [ ] Skills specs Architekt dans `skills/` (14 skills — injections agents)
- [ ] Adversarial L1 (LLM semantic) + L2 (architecture)
- [ ] HITL gates deploy + décisions IA sensibles
- [ ] AI audit logs append-only

### Qualité & preuve client

- [ ] Mutation testing (ADR-003) — mutmut sur modules critiques (seuil 50 %)
- [ ] E2E Playwright smoke en CI (login + health — pas les 82 specs)
- [x] Mini dashboard `/proof` (DORA, Lighthouse, a11y, SBOM)
- [ ] Case study generator (template + métriques mission)
- [x] FinOps dashboard POC `/finops` — coût LLM par mission (top 20)
- [ ] FinOps dashboard — marge > 50 %

### Global delivery

- [ ] i18n EN/FR/ZH baseline plateforme
- [ ] 4 DPA templates par région (SG, UAE, EU, US)
- [ ] Dashboard `dashboard/` rebrand + health unifié

---

## P2 — Tier B (Phase 4–6)

> **Gate** : ne démarrer qu'après 3 clients payants livrés (Phase 4 gate).

### IDP interne (Phase 5)

- [ ] Mission manifest YAML formalisé
- [ ] Template registry (workflows par offre, stack kits Tier A)
- [ ] Time-to-new-mission < 10 min (mission → repo → CI → report)
- [ ] Provisioning Terraform modules (Cloudflare Pages, Hetzner)
- [ ] Service catalog light (services, APIs, ownership)

### Ops & observabilité

- [ ] OTEL → Jaeger (opt-in, traces LLM + FastAPI)
- [ ] Backup/restore runbook testé (RPO 24h)
- [ ] Auto-heal workflow (tma-autoheal)
- [ ] SLO + error budget par mission

### Intégrations avancées

- [ ] MCP LRM server (port 9500) — locate, conventions, task_*
- [ ] Réparer tests fractal / MCP ou les isoler derrière extras
- [ ] Multi-vendor adversarial (Brain/Worker/Security split)
- [ ] Data residency flags (SG, EU, UAE, US)

### Client-facing (Phase 6)

- [ ] Client portal read-only (statut, docs, factures)

---

## P3 — Tier C (Phase 6–7+)

> **Gate** : multi-tenant après 10+ clients ; SaaS = optionnel (Phase 7).

- [ ] Multi-tenant + isolation tenant
- [ ] Billing Stripe / facturation auto
- [ ] Marketplace skills/templates public
- [ ] Canary deployment workflow prod (1%→100% + HITL)
- [ ] Darwin teams / Thompson scoring agents
- [ ] Pentest externe workflow (L3 regulated)
- [ ] Packaging Docker `architekt_platform` (niveau 3 ADR)

---

## Explicitement hors scope (ne pas construire tôt)

Cf. liste complète `docs/ROADMAP.md` § Ne pas construire tôt.

| Item | Priorité effective | Raison |
|------|-------------------|--------|
| Site web commercial Architekt (Astro) | P1 Phase 3 | Hors runtime plateforme — projet séparé |
| Backstage / Port / Humanitec | P3 / jamais | Trop lourd ; Architekt Platform suffit |
| Premier client payant / démo GTM | Business Phase 3–4 | Pas backlog plateforme |
| E2E Playwright complet (82 specs) | P3 | Smoke suffit Phase 2–4 |
| Projets L3 régulés (HIPAA, banque) | Refus | ADR-041, R24 |
