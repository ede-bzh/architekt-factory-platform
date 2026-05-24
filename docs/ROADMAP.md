# Architekt — Roadmap produit & business (révision globale)

> **Document maître.** Toute la planification Architekt (rebrand, technos, pratiques, GTM, scale) en une seule page.
> Version globale 2026-05-24 (revue exécutive multi-C-level + scope APAC + MENA + EMEA + USA).

## Doctrine fondatrice

> **Architekt does not sell code.**
> **Architekt sells globally-ready, AI-accelerated, security-conscious digital delivery.**
>
> Speed of AI + Rigor of senior engineering + Proof via automated quality reports + Global readiness

## Contexte

- **Architekt** = AI-native digital product studio à créer à **Singapour**, ambition **globale** (APAC base, expansion MENA, EMEA, USA).
- **Équipe** : 2 personnes (CPO + CTO).
- **Plateforme** = outil interne (anciennement *Software Factory*) qui orchestre des agents IA pour livrer des projets clients.
- **Repo** : `ede-bzh/architekt-factory-platform`.
- **État runtime aujourd'hui** : code sur GitHub (`main`, PR #7 mergé) — CI + tests locaux ; pas encore déployé prod.

## Principes directeurs (10)

1. **Studio d'abord, SaaS plus tard.** La plateforme reste un outil interne tant qu'on n'a pas 3 clients payants.
2. **Offers before stacks.** Le client achète un livrable (`docs/OFFERS.md`), pas un framework.
3. **Catalogue gouverné, pas spéculatif.** On n'équipe une nouvelle techno **que** quand un projet client la demande (`docs/CATALOG.md` tiers A/B/C).
4. **Modular monolith par défaut** (Shopify, Amazon Prime Video, Spring Modulith en 2026).
5. **TDD + mutation testing ciblé** sur le code critique uniquement (sinon = théâtre qualité).
6. **Design system standard** : shadcn/ui + Radix + Tailwind v4, **avec audit a11y réel**.
7. **Rien en prod sans CI verte + auth fail-closed + SBOM signé.**
8. **FinOps obligatoire** : marge brute > 50 %, budget LLM tracé par mission.
9. **Tier les technos** : Tier A maîtrisé / Tier B opportuniste / Tier C contrat signé.
10. **Global by design** : i18n + RTL + data residency + compliance régionale dès l'intake (cf. `docs/INTAKE.md`).

## Phases (vue d'ensemble)

| # | Nom | Durée | Gate de sortie | Statut | Note plateforme vs business |
|---|-----|-------|----------------|--------|----------------------------|
| **0** | Foundation & Rebrand | 1 semaine | Marque, licence, legal pack, positionnement écrits | **Partiel** | **Plateforme** : rebrand UI, auth, CI, demo LLM (waves 0–1). **Business** : legal pack, landing, licence formalisée ouverts. |
| **1** | Offer & Stack Catalogue | 1 semaine | 9 offres packagées + catalogue tierisé + 18 ADR | **Partiel** | **Docs** : 9 offres, catalogue A/B/C, INTAKE, ADR 029–045 écrits. **Business** : packaging commercial et validation terrain non faits. |
| **2** | Delivery Doctrine | 1 semaine | 14 skills Architekt + CI + SAST + SCA + SBOM | **En cours** | **Plateforme** : 14 skills, CI sécu/SBOM, L0, L2 déterministe, FinOps, audit logs, E2E smoke (waves 2–4). **Reste wave 5** : `docs/architekt/PLATFORM-BACKLOG.md` § Wave 5. |
| **3** | Public Pilot | 2 semaines | architekt.* live + Quality Report public + IMDA appli | À démarrer |
| **4** | First Paid Clients (APAC) | 1-3 mois | 3 clients payants, marge mesurée, 2 case studies | À démarrer |
| **5** | Internal Developer Platform + MENA/EMEA expansion | 1-3 mois | IDP fonctionnel + 1er client MENA ou EMEA | À démarrer |
| **6** | Client Portal | déclencheur 5 clients | Portail read-only | Conditionnel |
| **7** | SaaS Option | déclencheur 10+ clients | Multi-tenant + billing + marketplace (optionnel) | Conditionnel |

Détails par phase : voir `docs/architekt/phase-{0..7}.md`.

> **Livraisons plateforme (waves 0–4, PR #2→#7)** : backlog détaillé `docs/architekt/PLATFORM-BACKLOG.md`.
> **Wave 5 en cours** : câblage L2 dans `run_guard`, HITL deploy, `MAX_ARCHITEKT_SKILLS`, i18n/DPA, rebrand dashboard, L2 LLM, confirmation CI verte.

## Documents pivots (16)

| Document | Rôle |
|----------|------|
| **`ROADMAP.md`** (ce fichier) | Master plan + catalogue features |
| **`OFFERS.md`** | 9 offres packagées (Launch, MVP, Portal, Internal Tool, AI Workflow, Commerce, Modernize, Audit, Run) |
| **`CLIENTS.md`** | 9 typologies clients (scale-ups, SMEs, professional services, hospitality, industrial, education, healthcare wellness, e-commerce, government) |
| **`PROJECTS.md`** | 10 types de projets techniques |
| **`STACK-MATRIX.md`** | Mapping projet → stack (auth, DB, queue, monitoring, CMS, e-commerce) |
| **`ARCHITECTURES.md`** | 6 patterns référence (static-first, modular monolith, API-first, headless, AI workflow, multi-region) |
| **`SECURITY.md`** | Baseline + 4 niveaux (L0/L1/L2/L3) — NIST SSDF + OWASP ASVS + SBOM |
| **`COMPLIANCE.md`** | Matrice régionale (PDPA SG, UAE/Saudi PDPL, GDPR, US CCPA/SOC2/HIPAA) |
| **`I18N.md`** | Baseline international + RTL + locale + timezone + currency |
| **`UX-REGIONAL.md`** | UX par région (mobile-first APAC, premium MENA, a11y EMEA, conversion USA) |
| **`INTAKE.md`** | Global Project Readiness Checklist (à remplir avant devis) |
| **`METRICS.md`** | 7 catégories de KPIs (Market/Sales/Delivery/Security/Architecture/International/Finance/Platform) |
| **`GTM.md`** | Stratégie commerciale globale (APAC + MENA + EMEA + USA) |
| **`RISKS.md`** | 25 risques + 5 nouveaux globaux (R21-R25) |
| **`CATALOG.md`** | Catalogue technos tierisé |
| **`architekt/PLATFORM-BACKLOG.md`** | Backlog plateforme P0–P3 aligné Tier S/A/B/C |
| **`adr/`** | 36 ADR (001-020 + 029-045) |

## Phase 0 — Foundation & Rebrand (1 semaine)

**Objectif** : marque Architekt + cadre légal + positionnement clair, sans toucher au runtime prod.

Cf. `docs/architekt/phase-0-rebrand.md`.

**Gate de passage** :
- [ ] Marque Architekt appliquée partout
- [ ] Licence décidée (ADR-006)
- [ ] Templates commerciaux + legal prêts (NDA, MSA, SOW, DPA, IP, AI clauses, AUP)
- [ ] Positionnement global écrit
- [ ] Landing page placeholder live

## Phase 1 — Offer & Stack Catalogue (1 semaine)

**Objectif** : ce qu'on **vend** + avec quelles technos.

Cf. `docs/architekt/phase-1-offer-catalog.md`, `docs/OFFERS.md`, `docs/CATALOG.md`.

**Gate de passage** :
- [ ] 9 offres packagées
- [ ] Catalogue tierisé A/B/C
- [ ] Intake checklist écrite (`docs/INTAKE.md`)
- [ ] 5 ADR initiaux + 13 nouveaux ADR (008-020) + 8 ADR globaux (029-036) mergés

## Phase 2 — Delivery Doctrine (1 semaine)

**Objectif** : encoder pratiques Architekt en skills + CI sécurité + compliance régionale.

Cf. `docs/architekt/phase-2-practices.md`, `docs/skills-spec/`.

### 14 skills Architekt (12 + 2 globaux)

| Fichier | Sujet |
|---------|-------|
| `skills/architekt-archi.md` | Modular monolith (ADR-002), 6 reference architectures |
| `skills/architekt-tech.md` | TDD, mutation testing ciblé, 12-Factor |
| `skills/architekt-ux.md` | shadcn+Radix+Tailwind v4, WCAG 2.2 AA vérifié, UX régional |
| `skills/architekt-data.md` | PostgreSQL, migrations, RPO/RTO, isolation client |
| `skills/architekt-security.md` | Baseline + 4 niveaux, NIST SSDF, OWASP ASVS, SBOM |
| `skills/architekt-sre.md` | SLO, error budget, runbook, OTEL |
| `skills/architekt-delivery.md` | Phases delivery, DoD, scope rules, async-first |
| `skills/architekt-product.md` | Discovery, JTBD, project/client taxonomy |
| `skills/architekt-finops.md` | Budget LLM/mission, marges cibles, alertes |
| `skills/architekt-ai-governance.md` | HITL L0-L4, audit logs, transparence client |
| `skills/architekt-commercial.md` | BANT, devis <48h, négociation, pipeline |
| `skills/architekt-qa.md` | Mutation testing ciblé, a11y, perf, Quality Report |
| **`skills/architekt-compliance.md`** (NEW) | GDPR, PDPA SG, UAE/KSA PDPL, DPA, data transfer |
| **`skills/architekt-i18n.md`** (NEW) | locale abstraction, RTL, ICU, timezone/currency |

**Gate de passage** :
- [ ] 14 skills mergés
- [ ] CI verte + SAST + SCA + secret scanning + SBOM CycloneDX
- [ ] Mutation testing modules critiques (seuil 50 %)
- [ ] Badge CI README
- [ ] 4 DPA templates par région (SG, UAE, EU, US)

## Phase 3 — Public Pilot (2 semaines)

**Objectif** : `architekt.*` live + actif commercial complet.

Cf. `docs/architekt/phase-3-pilot.md`.

**Gate de passage** :
- [ ] `architekt.*` accessible (Lighthouse ≥ 95, WCAG AA)
- [ ] Démo vidéo + case study + Quality Report public
- [ ] Candidature IMDA SME Digital Solutions déposée

## Phase 4 — First Paid Clients APAC (1-3 mois)

**Objectif** : 3 clients payants APAC, marge mesurée, répétabilité.

Cf. `docs/architekt/phase-4-first-clients.md`.

**Gate de passage** :
- [ ] 3 clients payants signés et livrés
- [ ] 2 case studies réels publiés
- [ ] Marge brute > 50 % mesurée
- [ ] 1 client récurrent (Run)

## Phase 5 — IDP + MENA/EMEA expansion (1-3 mois)

**Objectif** :
1. Plateforme devient IDP interne (mission → repo → CI → report en < 10 min)
2. 1er client MENA (UAE/KSA) OU EMEA (FR/DE/UK)

Cf. `docs/architekt/phase-5-idp.md`.

**Gate de passage** :
- [ ] Mission créée en < 10 min
- [ ] 1er client hors APAC livré
- [ ] Compliance régionale validée sur ce projet

## Phase 6 — Client Portal (déclencheur 5 clients)

Cf. `docs/architekt/phase-6-client-portal.md`.

## Phase 7 — SaaS Option (déclencheur 10+ clients)

Cf. `docs/architekt/phase-7-saas.md`.


---

## Catalogue features plateforme

> **Objectif** : inventorier ce que la plateforme Architekt doit faire, prioriser sans sur-construire, et mapper chaque feature aux phases 0–7.
> Détail exécution : `docs/architekt/PLATFORM-BACKLOG.md`. Offres commerciales : `docs/OFFERS.md` (ne pas dupliquer ici).

### Vision produit

Architekt Platform = **GitHub** (code, PR, CI) + **Linear** (backlog, sprints, WSJF) + **Backstage** (catalogue services/templates) + **CI/CD** (gates qualité/sécu) + **agents IA** (156 skills orchestrés) + **quality gates** (adversarial L0–L2, SBOM, mutation testing).

```
┌─────────────┐   ┌──────────────┐   ┌─────────────────┐
│  Intake /   │   │   Mission    │   │  Repo + CI/CD   │
│  Offre      │──▶│  Control     │──▶│  (GitHub-like)  │
│  (OFFERS)   │   │  (Linear)    │   │                 │
└─────────────┘   └──────┬───────┘   └────────┬────────┘
                         │                      │
                         ▼                      ▼
                  ┌──────────────┐      ┌─────────────────┐
                  │ Agent Loop   │      │ Quality Gates   │
                  │ + Patterns   │      │ SAST/SCA/SBOM   │
                  │ + Workflows  │      │ Adversarial     │
                  └──────┬───────┘      └────────┬────────┘
                         │                      │
                         └──────────┬───────────┘
                                    ▼
                         ┌─────────────────────┐
                         │ quality-report.pdf  │  ← killer feature
                         │ (preuve client)     │
                         └─────────────────────┘
```

**Différenciation** : les concurrents vendent du code ou des heures ; Architekt vend une **preuve automatisée** de qualité, sécurité et architecture — exportable en PDF client-ready.

### Killer feature — `quality-report.pdf`

| Attribut | Détail |
|----------|--------|
| **Quoi** | Rapport PDF auto-généré à chaque release / fin de sprint / fin de mission |
| **Contenu** | DORA metrics, couverture tests, mutation score (modules critiques), Lighthouse, WCAG 2.2 AA, SAST/SCA résumé, SBOM CycloneDX signé, ADR architecture, threat model light, FinOps LLM/mission |
| **Format** | PDF brandé Architekt + JSON machine-readable (API `/api/missions/{id}/quality-report`) |
| **Public** | Version anonymisée sur `architekt.*/proof` (Phase 3) ; version complète en livrable client (Phase 4+) |
| **Tier** | **S** — différenciateur commercial (ADR-015) |
| **Phase** | POC Phase 2 → public Phase 3 → standard livrable Phase 4 |

Cf. `skills/architekt-qa.md`, `docs/METRICS.md`, Phase 3 livrable #8.

### 8 blocs fonctionnels

#### 1. CORE — Orchestration agents & missions

| Feature | Description | Tier | Phase |
|---------|-------------|------|-------|
| Agent loop + message bus | Exécution agents, SSE temps réel, négociation A2A | **S** | 0–2 |
| 156 agents + skills YAML | Registry, injection contexte Architekt | **S** | 2 |
| 15 patterns orchestration | solo, sequential, parallel, hierarchical, adversarial… | **S** | 2 |
| 36 workflows builtin | product-lifecycle, feature-sprint, security-hacking… | **A** | 2–4 |
| Mission control 11 phases | Idéation → déploiement → TMA | **S** | 2 |
| LLM multi-provider + FinOps | minimax/azure/demo, cooldown 429, coût/mission | **S** | 0–2 |
| Mémoire 4 couches | session → pattern → project → global (FTS5) | **A** | 3–5 |
| MCP bridge | fetch, memory-kg, playwright, LRM | **B** | 4–5 |

#### 2. Platform — IDP interne (Backstage-like, sans Backstage)

| Feature | Description | Tier | Phase |
|---------|-------------|------|-------|
| Mission manifest YAML | client, offre, stack, budget, équipe agents | **A** | 5 |
| Template registry | workflows par offre, stack kits Tier A, repo templates | **A** | 5 |
| Provisioning env (Terraform) | Cloudflare Pages, Hetzner, modules cloud client | **B** | 5 |
| Service catalog | Services, APIs, ownership (light catalog) | **B** | 5–6 |
| Time-to-new-mission < 10 min | mission → repo → CI → report | **A** | 5 |
| CLI `architekt` / `sf` | status, ideation, missions, streaming SSE | **S** | 0–2 |
| Dashboard monitoring | DORA, LLM traces, live SSE `/monitoring` | **A** | 3–4 |

#### 3. Security — NIST SSDF + adversarial

| Feature | Description | Tier | Phase |
|---------|-------------|------|-------|
| Auth fail-closed (`ARCHITEKT_API_KEY`) | Bearer, rate limit PG-backed | **S** | 0 |
| CI SAST + SCA + secret scan | Bandit, Semgrep, Safety, TruffleHog | **S** | 2 |
| SBOM CycloneDX signé | Syft, gate release | **S** | 2 |
| Adversarial L0 (deterministic) | test.skip, @ts-ignore, empty catch → VETO | **S** | 2 |
| Adversarial L1 (LLM semantic) | slop, hallucination, logic → VETO | **A** | 2–3 |
| Adversarial L2 (architecture) | RBAC, validation, API design → VETO + escalation | **A** | 3–4 |
| Threat model light + incident IR | 1 page STRIDE, playbook 7j post-mortem | **A** | 2–4 |
| Pentest externe workflow | L3 regulated only, Phase 6+ | **C** | 6+ |

Cf. `docs/SECURITY.md` (niveaux projet L0–L3, distinct des gates adversarial plateforme).

#### 4. Global delivery — i18n, compliance, régions

| Feature | Description | Tier | Phase |
|---------|-------------|------|-------|
| Intake checklist global | PDPA, GDPR, PDPL UAE/KSA, data residency | **S** | 1–2 |
| i18n EN/FR/ZH (+ RTL AR) | locale, timezone, currency (ICU) | **A** | 2–3 |
| Compliance matrix régionale | `docs/COMPLIANCE.md` templates DPA | **A** | 2–4 |
| UX régional par marché | mobile-first APAC, premium MENA, a11y EMEA | **A** | 3–5 |
| Data residency flags | SG, EU, UAE, US — choix hébergement | **B** | 5 |
| Regulated industry gate | Refus L3 HIPAA/banque/gouv (ADR-041) | **S** | 1 |

Cf. `docs/I18N.md`, `docs/UX-REGIONAL.md`, `docs/INTAKE.md`, `docs/CLIENTS.md`.

#### 5. Client-facing — preuve & portail

| Feature | Description | Tier | Phase |
|---------|-------------|------|-------|
| **`quality-report.pdf`** | Killer feature (voir ci-dessus) | **S** | 2–4 |
| Mini dashboard public `/proof` | Scores DORA, a11y, Lighthouse, SBOM | **S** | 3 |
| Case study generator | Template + métriques mission | **A** | 3–4 |
| Client portal read-only | statut, docs, factures, messages | **B** | 6 |
| Devis < 48h pipeline | BANT, offre packagée → SOW | **A** | 3–4 |
| Site commercial Astro | architekt.* (Phase 3, hors plateforme runtime) | **A** | 3 |

#### 6. Advanced AI — gouvernance & qualité LLM

| Feature | Description | Tier | Phase |
|---------|-------------|------|-------|
| HITL gates L0–L4 | human approval deploy, AI decisions sensibles | **A** | 2–4 |
| CoVe anti-hallucination | Draft→Verify→Answer→Final | **A** | 3–4 |
| Multi-vendor adversarial | Brain=Opus, Worker=MiniMax, Security=GLM | **B** | 4–5 |
| AI audit logs append-only | hash chain, transparence client | **A** | 2–4 |
| Auto-pause budget LLM 100% | ADR-011 FinOps | **S** | 2 |
| Darwin teams / Thompson scoring | Sélection agents optimale | **C** | 7 |

Cf. `skills/architekt-ai-governance.md`.

#### 7. SRE/Ops — fiabilité & observabilité

| Feature | Description | Tier | Phase |
|---------|-------------|------|-------|
| Health check `/api/health` | Liveness, DB, LLM provider | **S** | 0 |
| CI verte gate merge | 100% main (Phase 2+) | **S** | 2 |
| Backup/restore runbook | RPO 24h SQLite, snapshots VM | **A** | 3–4 |
| OTEL → Jaeger (opt-in) | Traces LLM + FastAPI | **B** | 4–5 |
| Auto-heal + chaos workflows | tma-autoheal, chaos-scheduled | **B** | 5 |
| Canary deployment workflow | 1%→10%→50%→100% + HITL | **C** | 6–7 |
| SLO + error budget | Par mission/client | **B** | 5 |

Cf. `skills/architekt-sre.md`, `docs/architekt/phase-5-idp.md`.

#### 8. Business — SAFe, FinOps, GTM

| Feature | Description | Tier | Phase |
|---------|-------------|------|-------|
| Product backlog WSJF | Epic→Feature→Story, Kanban | **A** | 4 |
| FinOps dashboard | Marge > 50%, coût LLM/mission | **S** | 2–4 |
| Pipeline commercial | Offres → devis → contrat | **A** | 3–4 |
| Velocity / burndown Chart.js | Métriques delivery | **B** | 4–5 |
| IMDA listing workflow | SME Digital Solutions | **A** | 3 |
| Multi-tenant + billing SaaS | Stripe, isolation tenant | **C** | 7 |
| Marketplace skills/templates | Communauté externe | **C** | 7 |

Cf. `docs/GTM.md`, `docs/METRICS.md`, `docs/OFFERS.md`.

### Priorisation Tier S / A / B / C

| Tier | Signification | Règle | Horizon |
|------|---------------|-------|---------|
| **S** | Survie studio — sans ça, pas de client ni de preuve | Build **maintenant** (Phase 0–3) | 0–6 mois |
| **A** | Différenciation — qualité, sécu, delivery répétable | Build **dès CI verte** (Phase 2–4) | 3–12 mois |
| **B** | Scale — IDP, portail, ops avancés | Build **après 3 clients payants** | 6–18 mois |
| **C** | Optionnel — SaaS, marketplace, pentest L3 | Build **sur déclencheur explicite** | 18+ mois |

**Tier S (14 features critiques)** : agent loop, mission control, LLM FinOps, auth fail-closed, CI SAST/SCA/SBOM, adversarial L0, **`quality-report.pdf`**, intake/compliance gate, regulated refusal, health check, CLI, rebrand Architekt, FinOps dashboard, auto-pause LLM.

**Tier A (20+ features)** : workflows, mémoire, HITL, i18n, DPA templates, template registry, time-to-mission, dashboard monitoring, WSJF backlog, pipeline commercial, CoVe, AI audit logs, backup runbook, case study generator, site `/proof`.

**Tier B** : MCP avancé, provisioning Terraform, service catalog, client portal, OTEL, auto-heal, SLO, data residency, multi-vendor adversarial.

**Tier C** : multi-tenant SaaS, billing, marketplace, canary deploy, pentest L3 workflow, Darwin teams.

### Ne pas construire tôt (liste explicite)

| Feature | Pourquoi attendre | Alternative Phase 0–4 |
|---------|-------------------|------------------------|
| Backstage / Port / Humanitec | Trop lourd pour 2 personnes ; besoin équipe plateforme | Étendre Architekt Platform (Phase 5) |
| Multi-tenant SaaS | Pas de product-market fit ; studio d'abord | Outil interne mono-tenant |
| Marketplace skills public | Pas de communauté | Skills privés `skills/` |
| Microservices par défaut | Complexité prématurée | Modular monolith (ADR-002) |
| Mobile natif iOS/Android | Hors catalogue Tier A initial | PWA / API-first si besoin |
| Projets L3 régulés (HIPAA, banque, gouv) | Capacité compliance insuffisante | Refus systématique (R24) |
| Pentest externe systématique | Coût 5–15k SGD/projet | SAST/SCA/SBOM + threat model light |
| E2E Playwright complet (82 specs) | Flaky, coût maintenance | Smoke login + health en CI |
| Custom CMS from scratch | Réinventer la roue | Astro, WordPress, Payload (Tier A stacks) |
| 10+ stacks simultanées | Dilution expertise | Catalogue Tier A/B/C strict |
| Darwin / auto-évolution agents | Recherche, pas delivery | Patterns fixes + HITL |
| Billing Stripe / facturation auto | Pas de clients récurrents massifs | Facturation manuelle Phase 4 |

### Typologies projet (A–G) & clients régionaux

> Types A–G = cœur delivery Phase 3–5. Types H–J (dashboard, modernisation, audit) : cf. `docs/PROJECTS.md`.

| Type | Projet | Stack défaut | Sécu | Régions prioritaires | Offre |
|------|--------|--------------|------|----------------------|-------|
| **A** | Corporate / marketing | Astro + Tailwind + shadcn | L0 | APAC, MENA, EMEA, USA | Launch |
| **B** | Product MVP | Next.js + FastAPI + PG | L1–L2 | APAC, EMEA, USA | MVP |
| **C** | Internal business tool | Next.js + FastAPI + RBAC | L1–L2 | Toutes | Internal Tool |
| **D** | AI workflow automation | Python/FastAPI + queue + vector DB | L1–L2 | Toutes | AI Workflow |
| **E** | E-commerce headless | Shopify + frontend | L1–L2 | APAC, MENA, EMEA | Commerce |
| **F** | CMS / content platform | WordPress ou Payload/Strapi | L0–L1 | Toutes | Launch / Internal |
| **G** | Client portal | Next.js + PG + object storage | **L2** | Toutes | Portal |

**Clients régionaux** (cf. `docs/CLIENTS.md`, `docs/GTM.md`) :

| Région | Phase | Typologies client prioritaires | Contraintes plateforme |
|--------|-------|-------------------------------|------------------------|
| **APAC** (base SG) | 3–4 | Scale-ups B2B, SMEs, professional services | PDPA, IMDA, mobile-first, EN/ZH |
| **MENA** | 5 | Hospitality/luxury, industrial, SMEs | PDPL UAE/KSA, **RTL AR**, premium UX |
| **EMEA** | 5 | Professional services, industrial | GDPR, WCAG 2.2 + EAA, FR/DE/EN |
| **USA** | 5+ | Scale-ups, professional services | CCPA, SOC2-ready, conversion UX |

### Arbre de décision architecture

```
Intake rempli (docs/INTAKE.md)
        │
        ▼
  Contenu statique, pas d'auth ?
    │ oui ──▶ A ou F ──▶ Pattern 1 Static-first (Astro)
    │ non
    ▼
  Besoin e-commerce ?
    │ oui ──▶ E ──▶ Pattern 4 Headless commerce (Shopify)
    │ non
    ▼
  Workflow IA / extraction docs ?
    │ oui ──▶ D ──▶ Pattern 5 AI workflow (+ HITL obligatoire)
    │ non
    ▼
  Portail client documents/factures ?
    │ oui ──▶ G ──▶ Pattern 3 API-first + RBAC L2
    │ non
    ▼
  App métier / MVP / internal tool ?
    │ oui ──▶ B ou C ──▶ Pattern 2 Modular monolith (défaut)
    │ non
    ▼
  Éditeurs non-techniques, contenu riche ?
         oui ──▶ F ──▶ WordPress vs headless (besoin éditeur)
```

Référence complète : `docs/ARCHITECTURES.md` (6 patterns), `docs/STACK-MATRIX.md`, ADR-037.

### Sécurité projet — niveaux L0 à L3

| Niveau | Exemples (types A–G) | Contrôles clés | Phase Architekt |
|--------|----------------------|----------------|-----------------|
| **L0** | A (marketing), F statique | Headers, SCA, anti-bot | Dès Phase 2 |
| **L1** | B MVP early, C internal, D AI light | + Auth, RBAC basique, audit logs, ASVS L1 | Phase 2–4 |
| **L2** | G portal, B B2B, C RH/finance | + Encryption at rest, RBAC fin, DPIA light | Phase 4–5 |
| **L3** | Secteur régulé (healthcare-adjacent, finance) | + ASVS L2/L3, pentest, data residency stricte | **Refus** jusqu'à maturité Phase 6+ |

Gate plateforme : **aucun deploy prod** sans CI verte + SBOM + niveau sécu documenté en ADR projet.
Détail : `docs/SECURITY.md`, ADR-031, ADR-041.

### Mapping features → phases 0–7

| Phase | Focus plateforme | Features Tier S/A clés |
|-------|------------------|------------------------|
| **0** | Rebrand, stabilité | Auth, health, CLI, demo LLM, branding Jinja |
| **1** | Catalogue offres/stacks | Intake, typologies A–G, regulated gate, ADR |
| **2** | Delivery doctrine | CI SAST/SCA/SBOM, adversarial L0–L1, skills, **`quality-report.pdf` POC**, FinOps |
| **3** | Pilot public | `/proof`, site Astro, case study, IMDA, i18n EN/FR/ZH |
| **4** | 3 clients APAC | WSJF backlog, pipeline commercial, quality report livrable, L2 portals |
| **5** | IDP + MENA/EMEA | Mission manifest, templates, time-to-mission < 10 min, OTEL |
| **6** | Client portal | Portail read-only, canary (Tier C), premier L3 pilote si mûr |
| **7** | SaaS option | Multi-tenant, billing, marketplace (déclencheur 10+ clients) |

### Backlog plateforme P0 / P1 / P2 / P3

Aligné sur Tier S/A/B/C — détail tickets : `docs/architekt/PLATFORM-BACKLOG.md`.

| Priorité | Tier | Horizon | Exemples |
|----------|------|---------|----------|
| **P0** | **S** | Phase 0–2 | Rebrand, auth, CI verte, SAST/SCA/SBOM, adversarial L0, quality-report POC, tests API |
| **P1** | **A** | Phase 2–4 | Skills Architekt injectés, HITL, i18n, `/proof`, WSJF, FinOps dashboard, mutation testing |
| **P2** | **B** | Phase 4–6 | Mission manifest, Terraform modules, client portal, OTEL, auto-heal, MCP LRM |
| **P3** | **C** | Phase 6–7+ | Multi-tenant, billing Stripe, marketplace, canary prod, Darwin teams, pentest L3 |

### Sources recherche (catalogue features)

| Source | Insight pour Architekt | Lien |
|--------|------------------------|------|
| **DORA 2025** | 90 % des orgs ont adopté le platform engineering ; plateforme interne = prérequis valeur IA | [Google Research](https://research.google/pubs/dora-2025-state-of-ai-assisted-software-development-report/) · [Google Cloud Blog](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report) |
| **NIST SSDF SP 800-218** | Secure Software Development Framework — baseline SAST/SCA/SBOM | [NIST SP 800-218](https://csrc.nist.gov/publications/detail/sp/800-218/final) · [v1.2 IPD déc. 2025](https://csrc.nist.gov/projects/ssdf) |
| **Modular monolith 2026** | Shopify, Prime Video, Spring Modulith 2.x — défaut avant microservices | ADR-002 · [Spring Modulith](https://spring.io/projects/spring-modulith) |
| **IMDA SGDE 2025** | Adoption IA PME SG : **4,2 % → 14,5 %** en 1 an ; opportunité SME Digital Solutions | [IMDA Digital Economy](https://www.imda.gov.sg/resources/press-releases-factsheets-and-speeches/press-releases/2025/singapore-digital-economy) · [SGDE Report PDF](https://www.imda.gov.sg/-/media/imda/files/about/resources/corporate-publications/annual-report/imda-sgde-report-fy2024-2025.pdf) |
| **Gartner MENA 2026** | Dépenses IT MENA **169 Mds USD** (+8,9 %), software +13,9 % — marché cible Phase 5 | [Gartner Press Release](https://www.gartner.com/en/newsroom/press-releases/2025-08-04-gartner-forecasts-mena-it-spending-to-reach-169-billion-us-dollars-in-2026) |
| **Astro (content sites)** | Static-first, i18n, Lighthouse ≥ 95 — stack Tier A types A/F + site Phase 3 | [Astro docs](https://docs.astro.build/) · `docs/architekt/phase-3-pilot.md` |


## ADR (Architecture Decision Records) — 36 total

| Série | Sujets | Phase |
|-------|--------|-------|
| 001-005 | Rebrand, modular monolith, mutation testing, design system, hosting | 0-1 |
| 006 | Licence (révisé : propriétaire interne) | 0 |
| 008-012 | Offers before stacks, IDP before SaaS, human approval, FinOps, SBOM | 1 |
| 013-015 | Client IP/AI, WCAG AA, Quality Report commercial | 2 |
| 016-020 | Pricing, cloud matrix, data retention, audit logs, multi-tenancy | 3-4 |
| **029-045** (17 nouveaux globaux) | Project/client taxonomy, security levels, regional compliance, i18n/RTL, data residency, AI workflow approval, architecture patterns, stack matrix, accept/reject, ISO27001 path, regulated industry, vendor mgmt, incident response, backup, security questionnaire | 1-2 |

## Risques (registre)

cf. `docs/RISKS.md` (25 risques). Synthèse P1 :

| Risque | Mitigation |
|--------|-----------|
| R1 Pas de pipeline commercial | Offres packagées + IMDA + 3 canaux |
| R2 Delivery non rentable | Marge > 50 % par projet, FinOps obligatoire |
| R3 Coût LLM invisible | ADR-011, alertes, auto-pause 100 % |
| R5 Trop de stacks trop tôt | Tier A/B/C strict |
| R8 Fondateurs surchargés | Scope strict, skills, embauche à 5 clients |
| **R24 (NEW)** Projet régulé sans capacité | Refus systématique HIPAA/banque/gouv jusqu'à maturité |

## Indicateurs principaux (cf. METRICS.md)

| Indicateur | P3 | P4 | P5 |
|------------|----|----|----|
| CI verte sur `main` | 100% | 100% | 100% |
| Marge brute projet | n/a | > 50% | > 55% |
| Coût LLM tracé / mission | partiel | 100% | 100% |
| SBOM par release | non | oui | oui |
| Time-to-new-mission | n/a | < 30 min | < 10 min |
| NPS client | n/a | > 8/10 | > 9/10 |
| Clients hors APAC | 0 | 0 | ≥ 1 |
| Listing IMDA | en cours | obtenu | maintenu |

## Sources externes (référence complète)

> Synthèse catalogue features : section **Catalogue features plateforme → Sources recherche** ci-dessus.


- **DORA 2025 Report — State of AI-assisted Software Development** (Google Cloud / Google Research, ~5 000 répondants) — l'IA comme amplificateur
- **NIST SP 800-218 SSDF v1.1** (févr. 2022) + **v1.2 IPD** (déc. 2025) — Secure Software Development Framework
- **OWASP ASVS v5** — Application Security Verification Standard
- **CycloneDX & SPDX** — formats SBOM
- **CISA / NTIA SBOM** Minimum Elements
- **Shopify / Amazon Prime Video 2023-2026** — retours modular monolith
- **Spring Modulith 2.x** (mars 2026)
- **Stryker / mutmut / PIT** — mutation testing
- **shadcn/ui + Radix + Tailwind v4** — consensus marché 2026
- **IMDA Singapore Digital Economy Report 2025** — SMEs IA 14.5 %, NAIIP 10 000 enterprises
- **UAE Federal Decree-Law 45/2021 PDPL**
- **Saudi PDPL (SDAIA)** 2021, révisé 2023
- **GDPR + EDPB guidelines**
- **CCPA + CPRA** (California)
- **W3C WCAG 2.2** (oct. 2023) + EAA EU 2025
- **EU AI Act, Singapore Model AI Governance Framework 2.0, ISO/IEC 42001**
- **IDP landscape 2026** : Backstage, Humanitec, Port, Fortem

## Liens

- `docs/OFFERS.md`, `docs/CLIENTS.md`, `docs/PROJECTS.md`
- `docs/STACK-MATRIX.md`, `docs/ARCHITECTURES.md`
- `docs/SECURITY.md`, `docs/COMPLIANCE.md`
- `docs/I18N.md`, `docs/UX-REGIONAL.md`
- `docs/INTAKE.md`, `docs/METRICS.md`
- `docs/GTM.md`, `docs/RISKS.md`, `docs/CATALOG.md`
- `docs/architekt/phase-{0..7}.md`
- `docs/adr/001..045`
- `docs/skills-spec/`
- `.github/labels.yml`
- `scripts/github/setup-project.sh`
