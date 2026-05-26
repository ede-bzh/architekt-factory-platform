# Architekt — Roadmap produit

Plateforme multi-agents SAFe pour le cycle de vie logiciel. **UI et documentation wiki : EN / FR uniquement.**

> **Dépôt** : [ede-bzh/architekt-factory-platform](https://github.com/ede-bzh/architekt-factory-platform)  
> **Version `main`** : `2.3.0` (tag `v2.3.0`, PR #11)  
> **Dernière mise à jour roadmap** : 2026-05-25

---

## Vue d’ensemble

| Statut | Périmètre |
|--------|-----------|
| ✅ **Sur `main`** | Rebrand UI, CI sécu, v2.3.0, L0–L2 + `run_guard`, HITL deploy API, FinOps, rate limit, E2E smoke |
| 🟡 **PR ouvertes** | #12 (ops/doc wave 5–6), #13 (L2 LLM, mutation, CSP), #14 (cadrage audit doc), #15 (Wave 8 doc — **prête à merger**) |
| 🔴 **À faire** | Merger #12–#15, secrets deploy GitHub, vague E infra, DPA, mutation 50 %, OTEL, IDP Phase 5+ |

---

## Livré sur `main` (état actuel)

| Domaine | Détail |
|---------|--------|
| **Catalogue** | ~163 agents · 41 workflows builtin · 104 skills YAML · 15 patterns (12 DB + 3 engine) |
| **SAFe** | Portfolio, WSJF, PI, sprints, backlog Kanban |
| **Identité** | UI Architekt, `ARCHITEKT_API_KEY`, thème `architekt_theme`, CLI `architekt` (alias `sf`) |
| **i18n** | UI `en` / `fr` (`platform/i18n`) |
| **Qualité** | Adversarial L0, L1 fail-closed, L2 déterministe, `run_guard` L0→L2→L1 |
| **Sécu CI** | ruff, bandit, pip-audit bloquants, detect-secrets, SBOM CycloneDX |
| **Preuve** | `/proof`, `quality-report.pdf`, case study, audit logs IA |
| **FinOps** | `/finops`, marge studio, métriques `architekt_*` (+ alias `macaron_*`) |
| **Ops** | `/api/health` version+timestamp, rate limit PG/SQLite, monitoring live (cache 20s) |
| **Release** | `CHANGELOG.md`, `docs/architekt/RELEASE.md`, CI release sur tags `v*` |
| **Tests** | `test_architekt_branding`, `test_no_legacy_external_refs` (La Poste), gates API/budget |

**Non livré sur `main` (doc utilisateur complète)** : voir Wave 8 — contenu dans **PR #15** (pas encore mergé).

---

## Chronologie — vagues produit (A → 8)

### Vagues A–D — rebrand & hygiène ✅ (`main`)

| Vague | Contenu |
|-------|---------|
| **A** | Rebrand UI, code mort retiré, tests anti-Macaron UI |
| **B** | `docs/ROADMAP.md`, wiki EN/FR, screenshots README `en`+`fr`, `.env.example` |
| **C** | Compteurs alignés README/wiki ; pages Home hors EN/FR retirées du wiki actif |
| **D** | Sync externe legacy retiré ; GitLab CI sans trigger Macaron |

### Vague E — infra legacy ⏳ (planifié)

- Renommage Docker / import Python `macaron_platform` → `architekt_platform`
- Runbook prod (RTO/RPO) — **ne pas faire sans fenêtre ops**
- Helm / compose : chemins cibles documentés (partiellement dans wiki + `platform/CLAUDE.md` PR #15)

### Waves 0–4 — backlog plateforme ✅ (`main`, PR #2–#7)

| Wave | Livrables clés |
|------|----------------|
| **0** | `branding.py`, provider `demo`, CI init, alias API key, skills doctrine |
| **1** | Quality PDF, budget LLM pause, `/proof`, `LOCAL-DEV.md` |
| **2** | 14 skills Architekt, L0, SAST/SCA/secrets, SBOM, E2E smoke |
| **3** | Rate limit, health API, FinOps POC, CLI `architekt` |
| **4** | L2 déterministe, Prometheus `architekt_*`, case study, audit logs IA |

### Wave 5 — durcissement 🟡 (partiel)

| Item | État |
|------|------|
| `run_guard` L0→L2→L1 | ✅ `main` |
| HITL deploy API | ✅ `main` (`/api/missions/{id}/hitl/deploy`) |
| CI verte `main` | ✅ post-#10/#11 (surveiller régressions) |
| Adversarial **L2 LLM** (sémantique) | 🟡 **PR #13** |
| Mutation testing seuil 50 % | 🟡 **PR #13** (job optionnel / ADR-003) |
| 4 DPA régions (SG, UAE, EU, US) | 🟡 **PR #12** |
| Dashboard `:8080` rebrand | 🟡 **PR #13** |
| `MAX_ARCHITEKT_SKILLS` / injection 14 skills | ⏳ backlog P1 |
| i18n ZH (hors scope officiel) | ❌ refusé — EN/FR seulement |
| Wiki Darwin / Deployment enrichi | 🟡 **PR #12** |
| `monitoring.js`, Dependabot, E2E `gateE2E` | 🟡 **PR #12** |

### Wave 6 — fondations release ✅ (`main`, PR #11, `v2.3.0`)

- `platform/VERSION`, `CHANGELOG.md`, `docs/architekt/RELEASE.md`
- bandit + pip-audit **bloquants**
- Deploy demo/azure après CI (`workflow_run`) — ⚠️ secrets `OVH_*` / `AZURE_*` à renseigner dans GitHub
- Compteurs catalogue documentés (163 / 41 / 104)

### Wave 7 — parallèle ops & sécu 🟡 (PR #12 + #13)

| PR | Contenu |
|----|---------|
| **#12** | Backlog sync, wiki Darwin/Deployment, `monitoring.js`, 4 DPA, Dependabot, E2E gate, `docs/architekt/HITL.md` |
| **#13** | `check_l2_llm()`, mutation gate + ADR-003, dashboard legacy, CSP nonce / `ROADMAP-WAVE7` |

### Wave 8 — documentation & rebrand doc ✅ (PR #15, merge pending)

> Audit : [`docs/architekt/REBRAND-DOC-AUDIT.md`](architekt/REBRAND-DOC-AUDIT.md) · cadrage : PR #14

**Livré dans PR #15** (branche `cursor/rebrand-doc-wave8-exec-7576`) :

| Périmètre | Détail |
|-----------|--------|
| Wiki EN | Home, API, Security, Patterns, Deployment enrichis — Architekt, v2.3.0, `ede-bzh` |
| Wiki FR | 8 pages `*‐FR` + `Home‐FR`, sidebar bilingue, footers EN↔FR seulement |
| README | EN + FR — `demo.architekt.dev`, 163 agents, tests `test_readme_en_fr` |
| Dev | `CLAUDE.md` racine, `platform/CLAUDE.md` (GIT unique + deploy legacy vs demo) |
| Gates | `test_doc_no_macaron_user_facing`, `test_wiki_fr_pages` |
| Index | `docs/architekt/README.md` |

**Reste Wave 8 (P2 = vague E)** :

- [ ] Runbook renommage `macaron_platform` → `architekt_platform`
- [ ] Helm chart `deploy/helm/macaron/` → cible `architekt`
- [ ] Optionnel : `Darwin-Teams‐FR.md`

**Critères de done** : merger PR #15 → `rg` P0 user-facing clean → pytest doc gates verts.

---

## Pull requests — file d’attente

| PR | Branche | Statut | Action recommandée |
|----|---------|--------|-------------------|
| [#14](https://github.com/ede-bzh/architekt-factory-platform/pull/14) | `cursor/rebrand-doc-backlog-7576` | Cadrage audit Wave 8 | Merger avant ou avec #15 |
| [#15](https://github.com/ede-bzh/architekt-factory-platform/pull/15) | `cursor/rebrand-doc-wave8-exec-7576` | **Exécution Wave 8** | **Merger sur `main`** |
| [#12](https://github.com/ede-bzh/architekt-factory-platform/pull/12) | `cursor/roadmap-parallel-wave-7576` | Vague 7 partielle | Merger après #15, résoudre conflits backlog |
| [#13](https://github.com/ede-bzh/architekt-factory-platform/pull/13) | `cursor/roadmap-parallel-wave2-7576` | L2 LLM, mutation, CSP | Merger après #12 |

---

## Reste à faire (par priorité)

### P0 — avant pilot client (Phase 2–3)

- [ ] Merger **#15** puis **#12** / **#13**
- [ ] Configurer secrets GitHub **OVH_SSH_KEY**, **OVH_IP**, **AZURE_*** pour deploy CI
- [ ] Confirmer CI verte sur `main` après chaque merge
- [ ] Valider deploy demo OVH une fois secrets OK

### P1 — différenciation studio (Tier A)

- [ ] Adversarial L1 stable en prod (régressions / coût LLM)
- [ ] Mutation testing **50 %** modules critiques (bloquant CI, pas `continue-on-error`)
- [ ] 4 **DPA** templates régions (PR #12)
- [ ] `MAX_ARCHITEKT_SKILLS` — injection complète 14 skills par rôle
- [ ] README multilingues : **EN/FR seulement** (✅ doc) — pas de réouverture DE/ES/JA…
- [ ] Site vitrine Architekt (Astro) — **projet séparé**, hors runtime plateforme

### P2 — scale (après 3 clients payants)

- [ ] Mission manifest YAML, template registry, time-to-mission &lt; 10 min
- [ ] OTEL → Jaeger opt-in
- [ ] Backup/restore runbook testé, auto-heal, SLO par mission
- [ ] MCP LRM (9500), multi-vendor adversarial, data residency flags

### P3 — optionnel (10+ clients / SaaS)

- [ ] Multi-tenant, billing Stripe, marketplace skills
- [ ] E2E Playwright **82 specs** (smoke suffit jusqu’ici)
- [ ] Client portal read-only, pentest L3, packaging `architekt_platform` niveau 3

### Infra vague E (quand fenêtre ops)

- [ ] Renommage `macaron_platform` / utilisateur Docker / chemins `/opt/macaron`
- [ ] Retrait alias `MACARON_API_KEY` après période 6 mois (ADR-001)
- [ ] Retrait métriques `macaron_*` quand dashboards migrés

---

## Explicitement hors scope (ne pas construire tôt)

| Item | Raison |
|------|--------|
| Backstage / Port / Humanitec | Trop lourd ; Architekt Platform suffit |
| i18n UI ZH / wiki DE·ES·JA… | Scope officiel EN/FR |
| Projets L3 régulés (HIPAA, banque) | ADR-041 |
| E2E 82 specs en gate merge | Smoke suffit Phase 2–4 |

---

## Phases studio (rappel)

| Phase | Objectif | Gate |
|-------|----------|------|
| 0–2 | Outil interne stable, preuve qualité | CI verte, `/proof`, doc Architekt |
| 3 | Pilot client | Wave 5–7 mergées, deploy demo OK |
| 4+ | Clients payants | P2 IDP / ops |
| 6–7 | Portal / SaaS | P3 |

Détail par phase : `docs/architekt/phase-*.md`

---

## Références

| Document | Rôle |
|----------|------|
| [`docs/architekt/PLATFORM-BACKLOG.md`](architekt/PLATFORM-BACKLOG.md) | Checkboxes détaillées par wave |
| [`docs/architekt/REBRAND-DOC-AUDIT.md`](architekt/REBRAND-DOC-AUDIT.md) | Audit doc Macaron/La Poste |
| [`docs/AUDIT_REBRAND.md`](AUDIT_REBRAND.md) | Audit UI vagues A–E |
| [`docs/architekt/RELEASE.md`](architekt/RELEASE.md) | Process release semver |
| [`platform/SPECS.md`](../platform/SPECS.md) | Spécifications (racine repo) |
| [Issues GitHub](https://github.com/ede-bzh/architekt-factory-platform/issues) | Suivi tâches |
