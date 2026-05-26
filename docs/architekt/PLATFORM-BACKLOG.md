# Backlog plateforme Architekt (hors projets clients)

Priorité actuelle : **outil interne studio** — rebrand, stabilité, CI, fonctionnalités manquantes.
Pas de site vitrine client en phase 0.

> **Alignement tiers** : P0 = Tier **S** · P1 = Tier **A** · P2 = Tier **B** · P3 = Tier **C**
> Catalogue complet : `docs/ROADMAP.md` § Catalogue features plateforme.
> **Wave en cours** : P2 scale (multi-tenant, mutation 50 % global) — voir `docs/ROADMAP.md`.

## Légende priorités

| Priorité | Tier | Phase cible | Règle |
|----------|------|-------------|-------|
| **P0** | S | 0–2 | Blocker — sans ça, pas de delivery ni de preuve client |
| **P1** | A | 2–4 | Différenciation — qualité, sécu, répétabilité |
| **P2** | B | 4–6 | Scale — après 3 clients payants |
| **P3** | C | 6–7+ | Optionnel — déclencheur explicite (10+ clients, SaaS) |

---

## Wave 0 — livré (Phase 0 rebrand)

> PR #2 — `cursor/architekt-roadmap-7576`.

- [x] Rebrand UI Architekt (`platform/branding.py`, templates Jinja)
- [x] Provider LLM `demo` restauré
- [x] Workflow CI initial + `pytest.ini`
- [x] Alias `ARCHITEKT_API_KEY` / `MACARON_API_KEY` (`platform/auth/api_key.py`)
- [x] Skills doctrine Lot 5–6 (compliance + i18n specs)

---

## Wave 1 — livré (P0 gates & preuve)

> PR #4 — CI gates, proof, quality PDF, LLM budget pause.

- [x] Quality gate CI : ruff + bandit sur `platform/`
- [x] **`quality-report.pdf` POC** (`platform/metrics/quality_pdf.py`)
- [x] Auto-pause budget LLM à 100 % (`platform/llm/budget.py`, ADR-011)
- [x] Mini dashboard `/proof` — health, quality, DORA
- [x] Run local documenté : `docs/architekt/LOCAL-DEV.md`

---

## Wave 2 — livré (skills, CI sécu, E2E smoke)

> PR #5 — `cursor/architekt-roadmap-wave2-7576`.

- [x] **14 skills Architekt** indexés (`platform/skills/architekt/`, `architekt_skills.py`)
- [x] Adversarial **L0** — veto test.skip / @ts-ignore / empty catch (`check_l0`, `tests/test_adversarial_l0.py`)
- [x] SAST + SCA + secret scan CI — bandit, pip-audit, detect-secrets (`scripts/ci/secret-scan.sh`)
- [x] SBOM CycloneDX par build CI (`cyclonedx-py` → artifact `sbom-platform.json`)
- [x] Tests `tests/test_platform_api.py` en gate CI
- [x] Workflow **E2E smoke** Playwright (`.github/workflows/e2e-smoke.yml` — login + health)
- [x] Tests gate : `test_api_key_alias`, `test_llm_budget`, `test_quality_pdf`

---

## Wave 3 — livré (rate limit, health, CLI)

> PR #6 — `cursor/architekt-roadmap-wave3-7576`.

- [x] Rate limiting PG/SQLite-backed sur mutations API (`platform/security/rate_limit.py`, `tests/test_rate_limit.py`)
- [x] Health check `/api/health` — `version` + `timestamp` (`tests/test_health_api.py`)
- [x] FinOps `/finops` — coût LLM par mission (top 20)
- [x] CLI **`architekt`** alias de `sf` (`cli/architekt.py`)

---

## Wave 4 — livré (observabilité & qualité)

> PR #7 — `cursor/architekt-roadmap-wave4-7576`.

- [x] Adversarial **L2 déterministe** (`check_l2` — secrets, eval, CORS, SQL f-string ; tests `test_adversarial_l2`)
- [x] Métriques Prometheus **`architekt_*`** (alias `macaron_*` + `architekt_finops_margin_pct`)
- [x] FinOps marge studio — `PLATFORM_FINOPS_MARGIN_TARGET_PCT` (défaut 50 %), alertes `/finops`
- [x] API `GET /api/finops/summary` + `GET /api/missions/{id}/case-study.md`
- [x] Journal audit IA append-only (`ai_audit_logs` + hook `trace_call`)
- [x] Tests : `test_finops_margin`, `test_prometheus_architekt`, `test_ai_audit_logs`, `test_case_study`

---

## Wave 5 — livré (audit & durcissement)

> PR #11 + #12 + #13 (merge `main`).

- [x] CI verte, `run_guard` L0→L2→L1, HITL deploy API + `docs/architekt/HITL.md`
- [x] `MAX_ARCHITEKT_SKILLS`, i18n EN/FR, 4 DPA (`docs/compliance/dpa/`)
- [x] `monitoring.js`, Dependabot, E2E `gateE2E`, wiki Darwin/Deployment
- [x] **Adversarial L2 LLM** (`check_l2_llm`, `tests/test_adversarial_l2_llm.py`)
- [x] **Mutation gate** pragmatique CI (ADR-003) — adversarial ≥15 %, api_key ≥10 %
- [x] **Dashboard :8080** rebrand minimal (`dashboard/` templates + landing)
- [ ] Mutation **50 % global** bloquant (reporté Wave 7)

## P0 — Tier S (Phase 0–2)

### Rebrand & stabilité (Phase 0)

- [x] `platform/branding.py` + globals Jinja
- [x] UI login / base / onboarding → Architekt
- [x] Provider LLM `demo` restauré (`_demo_response`)
- [x] `pytest.ini` + workflow `ci.yml`
- [x] `python-dotenv` dans `platform/requirements.txt`
- [x] Tests `tests/test_platform_api.py` en CI
- [x] Documenter run local : `PLATFORM_LLM_PROVIDER=demo make dev` → `docs/architekt/LOCAL-DEV.md`

### CI & quality gates (Phase 2)

- [x] CI verte 100 % sur `main` (gate merge) — **Wave 5 / PR #11**
- [x] Quality gate CI : ruff + bandit sur `platform/`
- [x] SAST + SCA + secret scan en CI (bandit, pip-audit, detect-secrets)
- [x] SBOM CycloneDX par release CI (cyclonedx-py)
- [x] Adversarial L0 — veto test.skip / @ts-ignore / empty catch
- [x] **`quality-report.pdf` POC** — export PDF mission (DORA, tests, SBOM)
- [x] Auto-pause budget LLM à 100 % (ADR-011)

### Auth & sécurité baseline

- [x] Auth fail-closed (`ARCHITEKT_API_KEY`) — alias `MACARON_API_KEY` 6 mois
- [x] Rate limiting PG-backed sur mutations

---

## P1 — Tier A (Phase 2–4)

### Rebrand niveau 2 (ADR-001)

- [x] `MACARON_API_KEY` → `ARCHITEKT_API_KEY` (alias 6 mois)
- [x] CLI `sf` → `architekt` (alias `sf`)
- [x] README EN/FR + wiki EN/FR embarqué (PR #15 ; pas d'autres locales)
- [x] Métriques Prometheus : préfixe `architekt_*` (garder `macaron_*` en alias)

### Skills & agents Architekt

- [x] Skills specs Architekt dans `platform/skills/architekt/` (14 skills — injections agents)
- [ ] Adversarial L1 (LLM semantic) en production stable
- [x] Adversarial L2 (architecture) + `run_guard` L0→L2→L1
- [x] HITL deploy API (`/api/missions/{id}/hitl/deploy`)
- [x] AI audit logs append-only

### Qualité & preuve client

- [x] Mutation testing (ADR-003) — mutmut 2.4 CI `scripts/ci/run_mutmut.sh` ; seuil global 50 % → **Wave 7**
- [x] E2E Playwright smoke en CI (login + health — pas les 82 specs)
- [x] Mini dashboard `/proof` (DORA, Lighthouse, a11y, SBOM)
- [x] Case study generator (template + métriques mission)
- [x] FinOps dashboard POC `/finops` — coût LLM par mission (top 20)
- [x] FinOps dashboard — marge > 50 % (alertes + `architekt_finops_margin_pct`)

### Global delivery

- [x] i18n UI **EN/FR** uniquement (ZH hors scope)
- [ ] 4 DPA templates par région (SG, UAE, EU, US)
- [ ] Dashboard rebrand complet (UI legacy port 8080)
- [x] Dashboard legacy documenté ; monitoring `/monitoring` + `/proof`

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
> Items multi-tenant / Stripe / pentest / docker rename / mutation 50 % sont **trackés en Wave 7** (P2) — voir `ROADMAP-WAVE7.md`.

- [ ] Multi-tenant + isolation tenant → **Wave 7**
- [ ] Billing Stripe / facturation auto → **Wave 7**
- [ ] Marketplace skills/templates public
- [ ] Canary deployment workflow prod (1%→100% + HITL)
- [ ] Darwin teams / Thompson scoring agents
- [ ] Pentest externe workflow (L3 regulated) → **Wave 7**
- [ ] Packaging Docker `architekt_platform` (niveau 3 ADR) → **Wave 7**

---


## Wave 6 — livré (doc + CI + releases + adaptive intelligence)

> PR #11 + contenu #12.

- [x] `platform/VERSION` 2.3.0 + `/api/health`
- [x] CI bandit + pip-audit bloquants ; release sur tags `v*`
- [x] Deploy demo/azure après CI (`workflow_run`)
- [x] `CHANGELOG.md` + `docs/architekt/RELEASE.md`
- [x] Monitoring live — `platform/metrics/live.py` (cache 20s)
- [x] GA scheduler LIVE + RL hook (`evolution_scheduler`, `rl_hooks`)
- [x] Compteurs : ~163 agents, 41 workflows, 104 skills

---

## Wave 7 — livré partiel (PR #12 mergé)

- [x] PR #12 — wiki Darwin/Deployment, monitoring.js, DPA, Dependabot, E2E gate, `HITL.md`
- [ ] PR #13 — L2 LLM, mutation gate (ADR-003), dashboard :8080, CSP

---

## Wave 8 — documentation & rebrand doc — **livré (`main`)**

> Audit : `docs/architekt/REBRAND-DOC-AUDIT.md` (PR #14/#15).

### P0 — Utilisateur (wiki + README)

- [x] Wiki Home EN/FR, README EN/FR, API/Security/Patterns/Deployment
- [x] 8 pages wiki `*‐FR` + navigation sidebar
- [x] Footers EN↔FR uniquement

### P1 — Développeur & gates

- [x] `CLAUDE.md` racine + `platform/CLAUDE.md` (deploy legacy vs demo)
- [x] `test_doc_no_macaron_user_facing`, `test_wiki_fr_pages`
- [x] `docs/architekt/README.md`

### P2 — Infra (vague E)

- [ ] Runbook `macaron_platform` → `architekt_platform`
- [ ] Helm chart cible Architekt

### Critères de done Wave 8

1. [x] P0 user-facing sans Macaron/La Poste
2. [x] pytest doc gates verts
3. [x] Pages sidebar « guide »
4. [x] `docs/ROADMAP.md` synchronisé


## Explicitement hors scope (ne pas construire tôt)

Cf. liste complète `docs/ROADMAP.md` § Ne pas construire tôt.

| Item | Priorité effective | Raison |
|------|-------------------|--------|
| Site web commercial Architekt (Astro) | P1 Phase 3 | Hors runtime plateforme — projet séparé |
| Backstage / Port / Humanitec | P3 / jamais | Trop lourd ; Architekt Platform suffit |
| Premier client payant / démo GTM | Business Phase 3–4 | Pas backlog plateforme |
| E2E Playwright complet (82 specs) | P3 | Smoke suffit Phase 2–4 |
| Projets L3 régulés (HIPAA, banque) | Refus | ADR-041, R24 |


## Wave 6 — livré (doc + CI + releases + adaptive intelligence)

> PR #11 — `cursor/architekt-enrichment-pr-a-7576` (merge `main`).

- [x] CI verte post-PR #10 (pytest, ruff, secret-scan, tests rebrand)
- [x] `platform/VERSION` semver (2.3.0) + `/api/health` version/timestamp
- [x] CI bandit + pip-audit **bloquants** (`bandit.yaml`, High-only gate)
- [x] Deploy demo/azure **après CI** (`workflow_run` → `conclusion == success`)
- [x] `CHANGELOG.md` + `docs/architekt/RELEASE.md`
- [x] Compteurs doc : ~163 agents, 41 workflows, 104 skills YAML (`platform/SPECS.md`)
- [x] Monitoring live refactor — `platform/metrics/live.py` (cache 20s, param `sections`)
- [x] **GA scheduler LIVE** — `evolution_scheduler.py` nightly 02:00 UTC (`server.py` lifespan)
- [x] **RL hook** — `platform/agents/rl_hooks.py` + `patterns/engine.py` (`apply_rl_pattern_override`)
- [x] Release job CI sur tags `v*` (SBOM artifact)
- [x] Compteurs : ~163 agents, 41 workflows, 104 skills YAML


---

## Wave 7 — scale P2 & security polish (doc + CSP)

> Détail : `docs/architekt/ROADMAP-WAVE7.md` · CSP : `docs/architekt/CSP.md`

- [x] **CSP** — politique documentée (default vs workspace), lien `security_headers` middleware
- [x] **`PLATFORM_CSP_NONCE=0|1`** — `ServerConfig.csp_nonce` + génération nonce optionnelle `script-src` (HTMX : `unsafe-inline` conservé)
- [ ] **Multi-tenant** + isolation tenant (gate 10+ clients)
- [ ] **Stripe** billing / usage LLM
- [ ] **Pentest externe** (L3 regulated workflow)
- [ ] **Docker rename** `architekt_platform` (alias `macaron_platform`)
- [ ] **Mutation testing** — seuil **50 %** modules critiques (mutmut CI)
- [x] **Adversarial L2 LLM** — *done (wave 2)* (autres agents)
- [x] **Dashboard `dashboard/`** rebrand — *done (wave 2)* (autres agents)
