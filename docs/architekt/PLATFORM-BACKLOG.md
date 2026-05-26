# Backlog plateforme Architekt (hors projets clients)

Priorité actuelle : **outil interne studio** — rebrand, stabilité, CI, fonctionnalités manquantes.
Pas de site vitrine client en phase 0.

> **Alignement tiers** : P0 = Tier **S** · P1 = Tier **A** · P2 = Tier **B** · P3 = Tier **C**
> Catalogue complet : `docs/ROADMAP.md` § Catalogue features plateforme.
> **Wave en cours** : § **Wave 8** (doc & rebrand complet) — audit `docs/architekt/REBRAND-DOC-AUDIT.md`.

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

> Reste P1 avant pilot Phase 3 — voir aussi `docs/ROADMAP.md` § Phases 0–2.

- [ ] **CI verte 100 %** sur `main` (gate merge — confirmer dernier run vert post-PR #7)
- [ ] **`run_guard` → L2** : appeler `check_l2` dans le pipeline (fonction livrée wave 4, câblage `run_guard` incomplet)
- [ ] **HITL gates** deploy + décisions IA sensibles (workflow + UI)
- [ ] **`MAX_ARCHITEKT_SKILLS`** — relever le plafond d'injection (4 → 14 skills selon rôle)
- [ ] **i18n EN/FR/ZH** baseline plateforme (catalogue + routes, pas seulement skills)
- [ ] **4 DPA templates** par région (SG, UAE, EU, US)
- [ ] **Dashboard `dashboard/`** rebrand Architekt + health unifié avec `/api/health`
- [ ] **Adversarial L2 LLM** (revue architecture sémantique — distinct du L2 déterministe wave 4)
- [ ] **Mutation testing** seuil 50 % sur modules critiques (job CI mutmut optionnel seulement)

---

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

- [ ] CI verte 100 % sur `main` (gate merge) → **Wave 5**
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
- [ ] README multilingues + wiki embarqué
- [x] Métriques Prometheus : préfixe `architekt_*` (garder `macaron_*` en alias)

### Skills & agents Architekt

- [x] Skills specs Architekt dans `platform/skills/architekt/` (14 skills — injections agents)
- [ ] Adversarial L1 (LLM semantic) en production stable
- [x] Adversarial L2 (architecture) + `run_guard` L0→L2→L1
- [x] HITL deploy API (`/api/missions/{id}/hitl/deploy`)
- [x] AI audit logs append-only

### Qualité & preuve client

- [ ] Mutation testing (ADR-003) — mutmut sur modules critiques (seuil 50 %) → **Wave 5**
- [x] E2E Playwright smoke en CI (login + health — pas les 82 specs)
- [x] Mini dashboard `/proof` (DORA, Lighthouse, a11y, SBOM)
- [x] Case study generator (template + métriques mission)
- [x] FinOps dashboard POC `/finops` — coût LLM par mission (top 20)
- [x] FinOps dashboard — marge > 50 % (alertes + `architekt_finops_margin_pct`)

### Global delivery

- [x] i18n UI **EN/FR** uniquement (ZH hors scope)
- [ ] 4 DPA templates par région (SG, UAE, EU, US) → **Wave 5**
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


## Wave 6 — fondations (doc + CI + releases) — livré

> PR #11 — release `v2.3.0` sur `main`.

- [x] CI verte post-PR #10 (pytest, ruff, secret-scan, tests rebrand)
- [x] `platform/VERSION` semver + `/api/health` version/timestamp
- [x] CI bandit + pip-audit **bloquants**
- [x] Deploy demo/azure après CI `workflow_run` (secrets deploy à configurer côté GitHub)
- [x] `CHANGELOG.md` + `docs/architekt/RELEASE.md`
- [x] Compteurs : ~163 agents, 41 workflows, 104 skills YAML

---

## Wave 7 — roadmap parallèle (PR #12 / #13) — en review

> Ne pas dupliquer ici : merger puis cocher depuis les PR.

- [ ] PR #12 — wiki Darwin/Deployment, monitoring.js, DPA régions, Dependabot, E2E gate, `HITL.md`
- [ ] PR #13 — L2 LLM, mutation gate (ADR-003), dashboard :8080, CSP / Wave 7 doc

---

## Wave 8 — documentation & rebrand 100 % (P0–P1) — **à traiter en profondeur**

> **Audit** : `docs/architekt/REBRAND-DOC-AUDIT.md` (2026-05-25).  
> Objectif : doc/wiki/README **cohérents Architekt**, complétude des pages courtes, plus de Macaron/La Poste dans le périmètre utilisateur EN/FR.

### P0 — Utilisateur (wiki + README)

- [x] Wiki `Home.md` / `Home‐FR` — branding **Architekt Factory**, release **v2.3.0**, repo `ede-bzh/architekt-factory-platform`, retirer tableau GitLab La Poste
- [x] README EN + FR — URLs demo/issues/clone studio ; compteurs alignés (163 / 41 / 104)
- [x] `API-Reference.md` — documenter `ARCHITEKT_API_KEY` (+ alias `MACARON_API_KEY` 6 mois, ADR-001)
- [x] `Security.md` — auth Architekt, HITL, L0–L2, CSP (lien doc CSP post-#13)
- [x] `Deployment-Guide.md` — colonnes « demo Architekt » vs « prod legacy macaron_* »
- [x] Compléter **`Patterns.md`** (cas d'usage, lien missions / adversarial)
- [x] Archiver ou supprimer wiki **Home‐ES/DE/IT/PT/JA/ZH** (hors scope i18n EN/FR officiel)
- [x] Pages FR manquantes référencées (`Security‐FR`, `Patterns‐FR`, etc.) — créer ou retirer les liens morts

### P1 — Développeur & gates

- [x] Réécrire `CLAUDE.md` racine pour le dépôt **Architekt** (retirer `_LAPOSTE`, `sync-to-laposte`, chemins `~/_MACARON-SOFTWARE`)
- [x] Aligner `platform/CLAUDE.md` + `docs/AUDIT_REBRAND.md` avec cet audit
- [x] Test gate doc : interdire `macaron-software` / « Macaron Software Factory » dans `docs/wiki/Home*.md` + README EN/FR (exceptions Deployment encart legacy)
- [x] Index doc `docs/architekt/README.md` — liens phases, backlog, release, audit

### P2 — Infra (lié vague E ROADMAP, pas bloquant Wave 8 doc)

- [ ] Runbook renommage `macaron_platform` → `architekt_platform` (ADR-001 niveau 3)
- [ ] Helm chart / compose : chemins cibles documentés sans supprimer alias prod tant que non migré

### Critères de done Wave 8

1. `rg -i 'macaron|laposte' docs/wiki/Home.md docs/wiki/Home‐FR.md README.md README.fr.md` → **0** (hors encarts « legacy infra » nommés)
2. `pytest tests/test_no_legacy_external_refs.py tests/test_readme_en_fr.py tests/test_architekt_branding.py` → verts (+ nouveau test doc si ajouté)
3. Chaque page du `_Sidebar.md` ≥ contenu « guide » (pas seulement tableaux vides)
4. `docs/ROADMAP.md` pointe vers l'audit et marque Wave 8 **livré** quand checkboxes ci-dessus cochées
