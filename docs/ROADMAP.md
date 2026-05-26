# Architekt — Roadmap produit

Plateforme multi-agents SAFe pour le cycle de vie logiciel. **UI et documentation wiki : EN / FR uniquement.**

> **Dépôt** : [ede-bzh/architekt-factory-platform](https://github.com/ede-bzh/architekt-factory-platform)  
> **Version `main`** : `2.3.0` (tag `v2.3.0`)  
> **Dernière mise à jour roadmap** : 2026-05-25 — PR #12, #13, #15 mergées sur `main`

---

## Vue d’ensemble

| Statut | Périmètre |
|--------|-----------|
| ✅ **Livré sur `main`** | Waves 0–8 (doc), 5–7 (ops/sécu), vagues A–D, release v2.3.0 |
| 🔴 **À faire (P0)** | Secrets GitHub deploy (`OVH_*`, `AZURE_*`), valider CI + deploy demo |
| 🔴 **À faire (P1+)** | Mutation 50 % global bloquant, vague E infra, OTEL, IDP Phase 5 |

---

## Livré sur `main` (état actuel)

| Domaine | Détail |
|---------|--------|
| **Catalogue** | ~163 agents · 41 workflows · 104 skills YAML · 15 patterns |
| **Identité** | UI Architekt, `ARCHITEKT_API_KEY`, CLI `architekt`, thème `architekt_theme` |
| **Documentation** | Wiki EN + 8 pages `*‐FR`, README EN/FR, `CLAUDE.md`, gates doc |
| **Qualité** | L0, L1 fail-closed, L2 déterministe + **L2 LLM**, `run_guard` L0→L2→L1 |
| **Sécu** | bandit/pip-audit bloquants, DPA 4 régions, CSP doc + `PLATFORM_CSP_NONCE` |
| **Compliance** | `docs/compliance/dpa/` (EU, US, SG, UAE) |
| **Ops** | HITL deploy API, `monitoring.js`, live metrics, GA + RL LIVE |
| **CI** | E2E smoke + `gateE2E`, mutation gate pragmatique (15 % / 10 %), Dependabot |
| **FinOps** | `/finops`, `/proof`, quality PDF, case study |
| **Dashboard** | `:8080` rebrand minimal (landing + liens plateforme) |
| **Release** | `CHANGELOG.md`, CI sur tags `v*`, deploy après CI vert |

---

## Chronologie — vagues produit

### Vagues A–D ✅

| Vague | Contenu |
|-------|---------|
| **A** | Rebrand UI, tests anti-Macaron UI |
| **B** | Roadmap, wiki, screenshots EN/FR |
| **C** | Compteurs catalogue alignés |
| **D** | Sync legacy retiré |

### Vague E — infra legacy ⏳

- [ ] `macaron_platform` → `architekt_platform` (runbook RTO)
- [ ] Retrait alias `MACARON_API_KEY` / métriques `macaron_*` (post-migration)
- [x] Chemins legacy documentés (wiki Deployment, `platform/CLAUDE.md`)

### Waves 0–4 ✅ (PR #2–#7)

Rebrand, CI, skills, L0, rate limit, FinOps, L2 déterministe, Prometheus `architekt_*`.

### Wave 5 ✅ (PR #11–#13)

- CI verte, `run_guard`, HITL + `docs/architekt/HITL.md`
- `MAX_ARCHITEKT_SKILLS`, i18n EN/FR, 4 DPA
- `monitoring.js`, Dependabot, E2E gate, wiki Darwin/Deployment
- L2 LLM, mutation gate CI, dashboard :8080

### Wave 6 ✅ (PR #11–#12)

- `v2.3.0`, bandit/pip-audit bloquants, deploy `workflow_run`
- Monitoring live, GA scheduler, RL hooks, release job SBOM

### Wave 7 ✅ partiel (PR #13)

- [x] `docs/architekt/CSP.md`, `ROADMAP-WAVE7.md`, nonce CSP
- [x] L2 LLM, mutation gate pragmatique, dashboard legacy
- [ ] Mutation **50 % global** bloquant
- [ ] Multi-tenant, Stripe, pentest L3 (P3)

### Wave 8 ✅ (PR #14–#15)

- [x] Wiki Home EN/FR, 8 pages techniques FR, README, API/Security/Patterns/Deployment
- [x] `test_doc_no_macaron_user_facing`, `test_wiki_fr_pages`, index `docs/architekt/README.md`
- [x] `REBRAND-DOC-AUDIT.md`, backlog synchronisé

---

## Pull requests — statut

| PR | Statut |
|----|--------|
| #11 | ✅ Mergée — v2.3.0 |
| #12 | ✅ Mergée sur `main` |
| #13 | ✅ Mergée sur `main` |
| #14–#15 | ✅ Contenu sur `main` (doc Wave 8) |

---

## Reste à faire

### P0 — ops & pilot

- [ ] Secrets GitHub : `OVH_SSH_KEY`, `OVH_IP`, variables Azure
- [ ] Vérifier workflow Deploy OVH après CI verte
- [ ] Surveiller CI `main` post-merge (régression)

### P1 — qualité & scale

- [ ] Mutation testing **50 %** modules critiques (CI bloquant, ADR-003)
- [ ] Adversarial L1 stabilisation prod (coût / régressions)
- [ ] Site vitrine Architekt (Astro) — projet séparé

### P2 — après 3 clients payants

- [ ] Mission manifest YAML, template registry, OTEL/Jaeger
- [ ] Backup/restore testé, auto-heal, SLO mission
- [ ] MCP LRM, multi-vendor adversarial, data residency

### P3 — optionnel

- [ ] Multi-tenant, billing, marketplace, E2E 82 specs, client portal

### Vague E — infra

- [ ] Renommage package Docker / Helm `macaron` → `architekt`

---

## Hors scope

i18n ZH · wiki DE/ES/JA… · Backstage · L3 régulé (HIPAA) · E2E 82 specs en gate merge

---

## Références

| Document | Rôle |
|----------|------|
| [`docs/architekt/PLATFORM-BACKLOG.md`](architekt/PLATFORM-BACKLOG.md) | Checkboxes détaillées |
| [`docs/architekt/REBRAND-DOC-AUDIT.md`](architekt/REBRAND-DOC-AUDIT.md) | Audit doc |
| [`docs/architekt/ROADMAP-WAVE7.md`](architekt/ROADMAP-WAVE7.md) | Wave 7 P2/P3 |
| [`docs/architekt/CSP.md`](architekt/CSP.md) | Content-Security-Policy |
| [`docs/AUDIT_REBRAND.md`](AUDIT_REBRAND.md) | Audit UI |
| [`docs/architekt/RELEASE.md`](architekt/RELEASE.md) | Release semver |
| [Issues](https://github.com/ede-bzh/architekt-factory-platform/issues) | Suivi |
