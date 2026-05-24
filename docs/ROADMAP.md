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
- **État runtime aujourd'hui** : code sur GitHub uniquement, rien n'est déployé.

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

| # | Nom | Durée | Gate de sortie | Statut |
|---|-----|-------|----------------|--------|
| **0** | Foundation & Rebrand | 1 semaine | Marque, licence, legal pack, positionnement écrits | À démarrer |
| **1** | Offer & Stack Catalogue | 1 semaine | 9 offres packagées + catalogue tierisé + 18 ADR | À démarrer |
| **2** | Delivery Doctrine | 1 semaine | 14 skills Architekt + CI + SAST + SCA + SBOM | À démarrer |
| **3** | Public Pilot | 2 semaines | architekt.* live + Quality Report public + IMDA appli | À démarrer |
| **4** | First Paid Clients (APAC) | 1-3 mois | 3 clients payants, marge mesurée, 2 case studies | À démarrer |
| **5** | Internal Developer Platform + MENA/EMEA expansion | 1-3 mois | IDP fonctionnel + 1er client MENA ou EMEA | À démarrer |
| **6** | Client Portal | déclencheur 5 clients | Portail read-only | Conditionnel |
| **7** | SaaS Option | déclencheur 10+ clients | Multi-tenant + billing + marketplace (optionnel) | Conditionnel |

Détails par phase : voir `docs/architekt/phase-{0..7}.md`.

## Documents pivots (16)

| Document | Rôle |
|----------|------|
| **`ROADMAP.md`** (ce fichier) | Master plan |
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

## Sources externes (ce sur quoi cette roadmap s'appuie)

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
