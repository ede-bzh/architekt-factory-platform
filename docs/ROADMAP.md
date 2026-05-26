# Architekt — Roadmap produit & studio

> **Document maître** — vision business (phases 0–7) + exécution plateforme (waves 0–8).  
> **Dépôt** : [ede-bzh/architekt-factory-platform](https://github.com/ede-bzh/architekt-factory-platform) · **Version runtime** : `2.3.0`  
> **Mise à jour** : 2026-05-25 — PR #11–#15 mergées sur `main`

**Sommaire** : [Vue d’ensemble](#vue-densemble-exécutive) · [Phases studio](#phases-studio-07) · [Documents pivots](#documents-pivots) · [Plateforme livrée](#livré-sur-main) · [Waves 0–8](#exécution-plateforme--waves-0–8) · [Catalogue features](#catalogue-features-plateforme) · [Reste à faire](#reste-à-faire) · [Hors scope](#ne-pas-construire-tôt)

---

## Doctrine (rappel)

> **Architekt does not sell code.** Architekt sells globally-ready, AI-accelerated, security-conscious digital delivery.

- Studio d’abord (Singapour / APAC), **SaaS après 10+ clients**
- **Offers before stacks** → [`docs/OFFERS.md`](OFFERS.md)
- Plateforme = outil interne multi-agents (ex–Software Factory), repo public ci-dessus
- UI & wiki doc : **EN / FR** uniquement

---

## Vue d’ensemble exécutive

| Axe | État `main` | Prochain focus |
|-----|-------------|----------------|
| **Studio phases 0–2** | Rebrand, skills, CI sécu largement livrés | Phase 3 pilot (`architekt.*`, case studies) |
| **Plateforme waves 0–8** | Livré (doc, HITL, L2 LLM, DPA, CSP) | Secrets deploy, mutation 50 % global |
| **Business Phase 4+** | Non démarré (clients payants) | 3 clients APAC, marge > 50 % |

---

## Phases studio (0–7)

| # | Nom | Objectif | Gate | Statut |
|---|-----|----------|------|--------|
| **0** | Foundation & Rebrand | Marque, licence, legal | Architekt partout, ADR-006 | ✅ **Largement livré** (UI, doc, gates) |
| **1** | Offer & Stack Catalogue | Offres + technos tierisées | OFFERS + CATALOG + intake | 🟡 Docs OK · packaging commercial à finaliser |
| **2** | Delivery Doctrine | 14 skills + CI sécu | CI verte, SBOM, adversarial | ✅ **Largement livré** sur `main` |
| **3** | Public Pilot | `architekt.*` + preuve publique | Lighthouse, IMDA, démo | 🔴 À faire |
| **4** | First paid clients (APAC) | 3 clients, marge, case studies | 3 signés livrés | 🔴 À faire |
| **5** | IDP + expansion | Mission manifest, templates, OTEL | IDP &lt; 10 min nouvelle mission | 🔴 Après gate Phase 4 |
| **6** | Client portal | Portail read-only | 5 clients | ⏳ Conditionnel |
| **7** | SaaS (optionnel) | Multi-tenant, billing | 10+ clients | ⏳ Conditionnel |

Détail : [`docs/architekt/phase-0-rebrand.md`](architekt/phase-0-rebrand.md) … [`phase-7-saas.md`](architekt/phase-7-saas.md) · index [`docs/architekt/README.md`](architekt/README.md)

---

## Documents pivots

| Document | Rôle |
|----------|------|
| **`ROADMAP.md`** (ce fichier) | Master plan studio + catalogue features + waves |
| [`OFFERS.md`](OFFERS.md) | 7 offres packagées (Launch, MVP, Portal, …) |
| [`CLIENTS.md`](CLIENTS.md) | Typologies clients |
| [`PROJECTS.md`](PROJECTS.md) | 10 types de projets techniques |
| [`CATALOG.md`](CATALOG.md) | Catalogue technos tierisé A/B/C |
| [`STACK-MATRIX.md`](STACK-MATRIX.md) | Projet → stack |
| [`ARCHITECTURES.md`](ARCHITECTURES.md) | 6 patterns référence |
| [`SECURITY.md`](SECURITY.md) | Niveaux L0–L3 projet |
| [`COMPLIANCE.md`](COMPLIANCE.md) | Matrice régionale |
| [`I18N.md`](I18N.md) · [`UX-REGIONAL.md`](UX-REGIONAL.md) | Global delivery |
| [`INTAKE.md`](INTAKE.md) | Checklist avant devis |
| [`METRICS.md`](METRICS.md) · [`GTM.md`](GTM.md) · [`RISKS.md`](RISKS.md) | KPIs, GTM, risques |
| [`architekt/PLATFORM-BACKLOG.md`](architekt/PLATFORM-BACKLOG.md) | Checkboxes waves P0–P3 |
| [`adr/`](adr/) | Décisions architecture (001+, 029+) |

---

## Livré sur `main`

| Domaine | Détail |
|---------|--------|
| **Catalogue** | ~163 agents · 41 workflows · 104 skills YAML · 15 patterns |
| **Identité** | UI Architekt, `ARCHITEKT_API_KEY`, CLI `architekt`, thème `architekt_theme` |
| **Documentation** | Wiki EN + 8 pages `*‐FR`, README EN/FR, `CLAUDE.md`, gates doc |
| **Qualité** | L0, L1 fail-closed, L2 déterministe + **L2 LLM**, `run_guard` L0→L2→L1 |
| **Sécu** | bandit/pip-audit bloquants, DPA 4 régions, CSP + `PLATFORM_CSP_NONCE` |
| **Ops** | HITL deploy, `monitoring.js`, live metrics, GA + RL LIVE |
| **CI** | E2E smoke, `gateE2E`, mutation gate pragmatique (15 % / 10 %), Dependabot |
| **FinOps** | `/finops`, `/proof`, quality PDF, case study, audit logs IA |
| **Release** | `CHANGELOG.md`, CI tags `v*`, deploy après CI (`workflow_run`*) |

\* Secrets GitHub `OVH_*` / `AZURE_*` encore à configurer.

---

## Exécution plateforme — Waves 0–8

### Vagues A–D ✅ (rebrand & hygiène)

| Vague | Contenu |
|-------|---------|
| **A** | Rebrand UI, tests anti-Macaron |
| **B** | Roadmap, wiki EN/FR, screenshots |
| **C** | Compteurs catalogue |
| **D** | Sync legacy retiré |

### Vague E 🔄 (infra legacy — engagé)

- [x] `platform/runtime.py` + image Docker `architekt_platform` (symlink `macaron_platform` 6 mois)
- [x] Runbook [`architekt/WAVE-E-RUNBOOK.md`](architekt/WAVE-E-RUNBOOK.md) + Helm `deploy/helm/architekt/`
- [x] Wiki Deployment EN/FR — cible `architekt_platform` + encart infra legacy
- [ ] Rebuild prod Azure + validation OTEL / hotpatch CI
- [ ] Fin de vie alias `macaron_platform` (+6 mois)
- [x] Chemins legacy documentés (wiki, `platform/CLAUDE.md`)

### Waves 0–4 ✅

| Wave | Livrables |
|------|-----------|
| 0 | branding, demo LLM, CI init, alias API |
| 1 | quality PDF, budget pause, `/proof` |
| 2 | 14 skills, L0, SAST/SCA, SBOM, E2E smoke |
| 3 | rate limit, health API, FinOps, CLI `architekt` |
| 4 | L2 déterministe, Prometheus `architekt_*`, audit logs |

### Wave 5 ✅ (PR #11–#13)

CI verte, `run_guard`, HITL, `MAX_ARCHITEKT_SKILLS`, i18n EN/FR, **4 DPA**, monitoring.js, Dependabot, L2 LLM, mutation gate, dashboard :8080.

### Wave 6 ✅

`v2.3.0`, CI bloquante, deploy post-CI, monitoring live, GA/RL, release SBOM.

### Wave 7 ✅ partiel

CSP doc, L2 LLM, mutation pragmatique, dashboard legacy — voir [`architekt/ROADMAP-WAVE7.md`](architekt/ROADMAP-WAVE7.md) pour P2/P3 (multi-tenant, Stripe, pentest, mutation 50 %).

### Wave 8 ✅

Wiki/README/CLAUDE rebrand, pages FR, `test_doc_no_macaron_user_facing`, [`REBRAND-DOC-AUDIT.md`](architekt/REBRAND-DOC-AUDIT.md).

### PR mergées

| PR | Contenu |
|----|---------|
| #11 | v2.3.0, enrichissement core |
| #12 | DPA, monitoring, HITL doc, Darwin wiki |
| #13 | L2 LLM, mutation, CSP, dashboard |
| #14–#15 | Audit + exécution doc Wave 8 |

---

## Catalogue features plateforme

> Inventaire **fonctionnel** (quoi la plateforme doit faire). Exécution détaillée : [`PLATFORM-BACKLOG.md`](architekt/PLATFORM-BACKLOG.md).  
> Offres commerciales : [`OFFERS.md`](OFFERS.md) — ne pas dupliquer ici.

### Vision

Architekt Platform ≈ orchestration **agents + missions SAFe** + **quality gates** (adversarial, SBOM, mutation) + **preuve client** (`quality-report.pdf`).

**Killer feature** : `quality-report.pdf` (DORA, tests, mutation, Lighthouse, WCAG, SAST/SCA, SBOM) — Tier **S**, ADR-015. POC livré (`platform/metrics/quality_pdf.py`).

### Priorisation Tier S / A / B / C

| Tier | Règle | Horizon |
|------|-------|---------|
| **S** | Sans ça, pas de client ni preuve | Phase 0–3 |
| **A** | Différenciation qualité/sécu | Phase 2–4 |
| **B** | Scale après **3 clients payants** | Phase 5–6 |
| **C** | SaaS, marketplace, L3 | 10+ clients |

### Blocs fonctionnels (synthèse)

| Bloc | Exemples Tier S/A | État `main` |
|------|-------------------|-------------|
| **1. Core** | Agent loop, missions 11 phases, LLM FinOps, patterns, workflows | ✅ Core livré |
| **2. IDP** | Mission manifest YAML, template registry, time-to-mission &lt; 10 min | 🔴 Phase 5 |
| **3. Security** | Auth, SAST/SCA, SBOM, L0–L2 + L2 LLM, rate limit | ✅ Sauf pentest L3 |
| **4. Global** | Intake, i18n EN/FR, DPA régions, compliance matrix | 🟡 DPA ✅ · ZH/RTL reporté |
| **5. Client-facing** | `/proof`, case study, quality PDF, portal, site Astro | 🟡 PDF/proof ✅ · portal Phase 6 |
| **6. AI governance** | HITL, audit logs, budget pause, Darwin/GA/RL | ✅ HITL + GA/RL LIVE |
| **7. SRE/Ops** | Health, CI gate, backup, OTEL, auto-heal, canary | 🟡 Health/CI ✅ · OTEL Phase 5 |
| **8. Business** | WSJF backlog, FinOps dashboard, pipeline commercial | 🟡 FinOps ✅ · GTM Phase 3–4 |

Tables détaillées feature-par-feature : voir commit historique `15094297` ou enrichir progressivement dans `PLATFORM-BACKLOG.md` § P0–P3.

### Typologies projet (rappel)

| Type | Projet | Offre |
|------|--------|-------|
| A | Corporate / marketing | Launch |
| B | Product MVP | MVP |
| C | Internal tool | Internal Tool |
| D | AI workflow | AI Workflow |
| E | E-commerce | Commerce |
| F | CMS / content | Launch / Internal |
| G | Client portal | Portal |

Cf. [`PROJECTS.md`](PROJECTS.md), [`STACK-MATRIX.md`](STACK-MATRIX.md).

---

## Reste à faire

### P0 — ops & pilot

- [ ] Secrets GitHub deploy (`OVH_SSH_KEY`, `OVH_IP`, Azure)
- [ ] CI `main` stable post-merge
- [ ] Phase 3 : site `architekt.*`, case study publique

### P1 — plateforme & qualité

- [ ] Mutation testing **50 %** global (CI bloquant)
- [ ] Adversarial L1 stable en prod
- [ ] Phase 4 : 3 clients payants APAC

### P2 — scale (gate 3 clients)

- [ ] IDP : manifest YAML, template registry, OTEL
- [ ] MCP LRM, multi-vendor adversarial, data residency

### P3 — optionnel

- [ ] Multi-tenant, Stripe, marketplace, E2E 82 specs, client portal

### Vague E infra

- [ ] Renommage `macaron_platform` / Helm / alias API fin de vie

---

## Ne pas construire tôt

| Item | Raison |
|------|--------|
| Backstage / Port / Humanitec | Trop lourd ; Architekt Platform suffit |
| Multi-tenant SaaS | Après 10+ clients |
| Marketplace skills public | Pas de communauté |
| Microservices par défaut | Modular monolith (ADR-002) |
| Projets L3 (HIPAA, banque) | Refus ADR-041 / R24 |
| E2E 82 specs en gate merge | Smoke suffit Phase 2–4 |
| i18n ZH / wiki DE·ES·JA | Scope officiel EN/FR |
| Darwin auto-évolution seul | Patterns + HITL d’abord |

Liste alignée [`PLATFORM-BACKLOG.md`](architekt/PLATFORM-BACKLOG.md) § hors scope.

---

## Références techniques

| Document | Rôle |
|----------|------|
| [`architekt/PLATFORM-BACKLOG.md`](architekt/PLATFORM-BACKLOG.md) | Waves + checkboxes |
| [`architekt/REBRAND-DOC-AUDIT.md`](architekt/REBRAND-DOC-AUDIT.md) | Audit doc Macaron/La Poste |
| [`architekt/CSP.md`](architekt/CSP.md) | CSP |
| [`architekt/ROADMAP-WAVE7.md`](architekt/ROADMAP-WAVE7.md) | Wave 7 P2/P3 |
| [`architekt/HITL.md`](architekt/HITL.md) | Gates humains |
| [`architekt/RELEASE.md`](architekt/RELEASE.md) | Semver & tags |
| [`AUDIT_REBRAND.md`](AUDIT_REBRAND.md) | Audit UI |
| [`platform/SPECS.md`](../platform/SPECS.md) | Spécifications |
| [Issues GitHub](https://github.com/ede-bzh/architekt-factory-platform/issues) | Suivi |
