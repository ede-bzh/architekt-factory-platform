# Architekt — Roadmap produit & business

> **Document maître.** Toute la planification Architekt (rebrand, technos, pratiques, GTM, scale) en une seule page.
> Version enrichie 2026-05-24 (revue exécutive multi-C-level intégrée).

## Contexte

- **Architekt** = AI-native digital product studio à créer à **Singapour**, ambition **APAC** (ASEAN).
- **Équipe** : 2 personnes (CPO + CTO).
- **Plateforme** = outil interne (anciennement *Software Factory*) qui orchestre des agents IA pour livrer des projets clients.
- **Repo** : `ede-bzh/architekt-factory-platform` (renommé 2026-05-24).
- **État runtime aujourd'hui** : code sur GitHub uniquement, rien n'est déployé.

## Doctrine fondatrice

> **Studio IA premium d'abord. Plateforme interne ensuite. SaaS éventuellement.**

```
Speed of AI  +  Rigor of senior engineering  +  Proof via automated quality reports  +  APAC focus
```

Cette doctrine résout la tension entre vitesse IA et stabilité delivery identifiée par le rapport **DORA 2025** : l'IA est un **amplificateur**, elle accélère les organisations bien outillées et empire celles qui ne le sont pas. Architekt doit vendre une **méthode industrialisée**, pas seulement « des agents qui codent ».

## Principes directeurs

1. **Studio d'abord, SaaS plus tard.** La plateforme reste un outil interne tant qu'on n'a pas 3 clients payants.
2. **Catalogue gouverné, pas catalogue spéculatif.** On n'équipe une nouvelle techno **que** quand un projet client la demande.
3. **Offres avant stacks.** Le client achète un livrable (site, MVP, outil interne), pas un framework.
4. **Modular monolith par défaut** (Shopify, Amazon Prime Video, Spring Modulith en 2026).
5. **TDD + mutation testing** sur le code critique uniquement (sinon = théâtre qualité).
6. **Design system standard** : shadcn/ui + Radix + Tailwind v4, **avec audit a11y réel** (Radix donne les bases, pas le top niveau).
7. **Rien en prod sans CI verte + auth fail-closed + SBOM signé.**
8. **FinOps obligatoire** : marge brute > 50 %, budget LLM tracé par mission.
9. **Tier les technos** : Tier A maîtrisé / Tier B opportuniste / Tier C contrat signé seulement.
10. **APAC wedge** : SMEs Singapour éligibles **IMDA NAIIP / DEB / SME AI Impact Awards 2026** = pool de leads.

## Phases (vue d'ensemble)

| # | Nom | Durée | Gate de sortie | Statut |
|---|-----|-------|----------------|--------|
| **0** | Foundation & Rebrand | 1 semaine | Marque, licence, legal pack, positionnement écrits | À démarrer |
| **1** | Offer & Stack Catalogue | 1 semaine | 5 offres packagées + catalogue tierisé (A/B/C) + 5 ADR | À démarrer |
| **2** | Delivery Doctrine | 1 semaine | 12 skills Architekt + CI + SAST + SCA + SBOM + mutation testing modules critiques | À démarrer |
| **3** | Public Pilot | 2 semaines | architekt.* live + Lighthouse ≥ 95 + WCAG AA + démo vidéo + case study | À démarrer |
| **4** | First Paid Clients | 1-3 mois | 3 clients payants, marge mesurée, 2 offres répétables | À démarrer |
| **5** | Internal Developer Platform | 1-2 mois | Mission/repo/CI/report générés en < 10 min | À démarrer |
| **6** | Client Portal | déclencheur 5 clients | Portail read-only (statut, livrables, rapports, ADR) | Conditionnel |
| **7** | SaaS Option | déclencheur 10+ clients | Multi-tenant + billing + marketplace (optionnel) | Conditionnel |

Détails par phase : voir `docs/architekt/phase-{0..7}.md`.

## Vue d'ensemble

```
[P0]──[P1]──[P2]──[P3]──[P4]──[P5]──[P6?]──[P7??]
 Found  Offers Doctr Pilot Clients IDP   Portal  SaaS
  1w    1w     1w    2w    1-3m    1-2m   trig   trig
                            │
                            ▼
              3 clients payants + marge connue
              + case studies réels
              + 1 stack principale maîtrisée
              + plateforme interne crédible
```

## Phase 0 — Foundation & Rebrand (1 semaine)

**Objectif** : marque Architekt + cadre légal + positionnement clair, sans toucher au runtime prod.

**Livrables** :
- Rebrand 3 niveaux (visible + identifiants + runtime reporté) — cf. `docs/architekt/phase-0-rebrand.md`
- **Positionnement** : *"AI-native digital product studio for APAC scale-ups and SMEs"*
- **Brand system minimal** : logo placeholder, palette, typo, tone of voice, templates pitch deck / proposal / case study
- **Décision licence** : plateforme interne propriétaire par défaut ; composants clients sous licence client ; **éviter AGPL** tant que le modèle commercial n'est pas clarifié (cf. ADR-006 révisé)
- **Legal pack** : NDA, MSA (Master Service Agreement), SOW (Statement of Work), DPA (Data Processing Agreement), IP assignment, clause usage IA, AUP
- **Landing page placeholder** (Carrd ou Astro 1-pager) prête

**Gate de passage** :
- [ ] marque Architekt appliquée partout (Niveau 1 + 2)
- [ ] anciens noms (Macaron / Software Factory) supprimés du visible
- [ ] licence décidée (ADR-006)
- [ ] templates commerciaux prêts (NDA, MSA, SOW, DPA)
- [ ] politique IP/IA écrite
- [ ] landing page placeholder live

## Phase 1 — Offer & Stack Catalogue (1 semaine)

**Objectif** : ce qu'on **vend**, comment, à quel prix.

### Offres packagées (5)

| Offre | Durée | Prix cible | Livrable |
|-------|-------|------------|----------|
| **Architekt Launch** | 2-3 semaines | 5k-15k SGD | Site + brand + analytics |
| **Architekt MVP** | 4-8 semaines | 20k-60k SGD | App web exploitable |
| **Architekt Internal Tool** | 3-6 semaines | 15k-40k SGD | Outil métier interne |
| **Architekt AI Workflow** | 2-6 semaines | 10k-50k SGD | Automatisation IA contrôlée |
| **Architekt Audit** | 1 semaine | 3k-10k SGD | Rapport CTO + roadmap |

Détails complets dans `docs/OFFERS.md`.

### Catalogue technos tierisé

| Tier | Politique | Stacks |
|------|-----------|--------|
| **A** | Maîtrisé dès maintenant, projets vendables immédiatement | Astro, Next.js, FastAPI, PostgreSQL, Tailwind+shadcn, Cloudflare Pages, GitHub Actions |
| **B** | Activable sur client (1-3 jours d'équipement) | WordPress, Shopify, Payload CMS, NestJS, Azure, AWS |
| **C** | Uniquement si contrat signé d'avance | Spring Modulith, SwiftUI, Kotlin/Compose, multi-tenant SaaS, Kubernetes |

Détails dans `docs/CATALOG.md`.

**Gate de passage** :
- [ ] 5 offres packagées (one-pager + SOW template chaque)
- [ ] pricing initial défini par offre
- [ ] catalogue technos tierisé
- [ ] critères accept/refuse projet écrits (`docs/intake-checklist.md`)
- [ ] 5 ADR initiaux mergés (001-005), 5 ADR additionnels (008-012) rédigés

## Phase 2 — Delivery Doctrine (1 semaine)

**Objectif** : encoder les pratiques Architekt en **skills agents** + CI sécurité.

### 12 skills Architekt

| Fichier | Sujet |
|---------|-------|
| `skills/architekt-archi.md` | Modular monolith (ADR-002), ADR obligatoire, C4 |
| `skills/architekt-tech.md` | TDD, mutation testing ciblé (ADR-003), 12-Factor |
| `skills/architekt-ux.md` | shadcn+Radix+Tailwind v4 (ADR-004), WCAG 2.2 AA vérifiée |
| `skills/architekt-data.md` | PostgreSQL, migrations, RPO/RTO, FTS, isolation client |
| `skills/architekt-security.md` | **OWASP ASVS L1 par défaut, L2 données sensibles**, **NIST SSDF**, SBOM CycloneDX/SPDX |
| `skills/architekt-sre.md` | SLO, error budget, runbook, OTEL |
| **`skills/architekt-delivery.md`** | Phases discovery/build/hardening/handover, definition of done, scope rules |
| **`skills/architekt-product.md`** | Discovery, jobs-to-be-done, hypothèses, métriques produit |
| **`skills/architekt-finops.md`** | Budget LLM/mission, coût infra max/client, marge cible 50 %, alertes |
| **`skills/architekt-ai-governance.md`** | Human approval (sécu/factu/infra/données client), agent audit logs, version logging |
| **`skills/architekt-commercial.md`** | Cycle commercial, qualification, devis, suivi opportunités |
| **`skills/architekt-qa.md`** | Mutation testing ciblé, a11y audit, perf, security scan |

### Sécurité supply chain

- **OWASP ASVS** comme référentiel verification (L1 par défaut, L2 données sensibles)
- **NIST SSDF SP 800-218** (Rev. 1.2 IPD Dec 2025) mappé sur ASVS
- **SBOM obligatoire** au format **CycloneDX** et/ou **SPDX** (PS.3.2 SSDF)
- SAST + SCA + secret scanning dans CI
- Dépendances signées si possible (Sigstore)

### Mutation testing : politique nuancée

| Périmètre | Politique |
|-----------|-----------|
| Moteurs critiques (paiement, auth, calcul métier) | **Obligatoire** (Stryker / mutmut / PIT) |
| Logique métier standard | **Recommandé** progressif (50 → 70 → 80 %) |
| UI / templates / glue | **Optionnel** |
| Code généré / utilitaires triviaux | **Exclu** |

Évite le théâtre qualité.

**Gate de passage** :
- [ ] 12 skills mergés
- [ ] CI verte (pytest + ruff + bandit)
- [ ] SAST + SCA + secret scanning actifs sur PR
- [ ] SBOM généré au build (CycloneDX)
- [ ] Mutation testing actif sur modules critiques (seuil ≥ 60 %)
- [ ] Checklist delivery prête

## Phase 3 — Public Pilot (2 semaines)

**Objectif** : `architekt.*` en ligne et **utilisable comme actif commercial**.

### Livrables actifs commerciaux

- **Site Architekt** (Astro 5 + Tailwind v4 + shadcn/ui) avec pages **Method**, **Platform**, **Proof**
- **Case study fictif mais réaliste** — démontre la doctrine sur un faux client
- **Démo vidéo 2 minutes** (mission agentique → livrable)
- **Rapport qualité exportable** (DORA + Lighthouse + Stryker + SBOM)
- **Mini dashboard public** : score DORA, tests, a11y, lighthouse, security scan

### Plateforme runtime

- VM **Hetzner CAX11** Helsinki ou Hillsboro (~5 €/mois) — cf. ADR-005
- Auth **fail-closed** (`ARCHITEKT_API_KEY` obligatoire)
- HTTPS via Caddy ou Traefik
- Plausible analytics (PDPA-friendly)
- Domaine `architekt.{sg|ai|io}` à trancher

### Audit a11y

shadcn/Radix donne **les bases** WCAG mais **certains composants nécessitent corrections** (focus, contraste) en 2026. → Audit obligatoire avant go-live.

**Gate de passage** :
- [ ] `architekt.*` accessible publiquement
- [ ] Lighthouse ≥ 95 toutes catégories
- [ ] WCAG 2.2 AA **vérifié** (axe-core + audit manuel composants critiques)
- [ ] Formulaire contact fonctionnel
- [ ] Démo vidéo publiée (LinkedIn + YouTube)
- [ ] 1 case study publié sur le site
- [ ] 1 rapport qualité exportable (PDF + dashboard)
- [ ] Listing sur IMDA SME Digital Solutions (candidature posée)

## Phase 4 — First Paid Clients (1-3 mois)

**Objectif** : prouver la **rentabilité** + **répétabilité** sur 3 clients payants.

### Métriques cibles

| Indicateur | Cible |
|------------|-------|
| Marge brute projet | **> 50 %** |
| Dépassement budget LLM | **< 10 %** |
| Temps cadrage → devis | **< 48 h** |
| Time-to-first-demo | **< 5 jours** |
| NPS client | **> 8/10** |
| Rework post-livraison | **< 15 %** |
| Bugs P1/P2 en prod | **0** |
| Temps handover client | **< 2 jours** |

### Acquisition (canaux à tester)

- **IMDA NAIIP / DEB** : candidater à être listé comme vendor pré-approuvé (subventions SME)
- **SME AI Impact Awards 2026** : candidature
- LinkedIn outbound vers CTOs / founders APAC
- Partenariats avec consultants Singapour (recommandation)
- Content marketing (case study + blog Méthode/Platform)

cf. `docs/GTM.md`.

**Gate de passage** :
- [ ] 3 clients payants signés et livrés
- [ ] 2 case studies réels publiés
- [ ] Marge brute mesurée et communicable
- [ ] Au moins 1 client récurrent (TMA, run, retainer)
- [ ] Portail client non encore nécessaire mais spécifié dans `docs/architekt/phase-6-client-portal.md`

## Phase 5 — Internal Developer Platform (1-2 mois)

**Objectif** : la plateforme Architekt devient un **vrai IDP interne** (mission → repo → CI → report en < 10 min).

Inspiré du paysage IDP 2026 (Backstage, Humanitec, Port, Fortem) mais **sans dépendance externe** pour rester souverain.

### Capacités à construire

- Mission manifest (déjà partiel)
- Agent registry (déjà — `platform/skills/definitions/`)
- Template registry (workflows + stack kits)
- Environment provisioning (Terraform modules par cloud)
- Secrets management (vault par client)
- CI templates (par stack Tier A)
- Quality scanner (déjà — à exposer en API)
- Cost tracker (FinOps par mission)
- Audit trail (agent decisions, prompt versions)
- Client report generator (PDF DORA + qualité)

**Gate de passage** :
- [ ] Nouvelle mission créée en < 10 minutes
- [ ] Repo généré automatiquement (template Tier A)
- [ ] CI créée automatiquement
- [ ] Quality report généré automatiquement à la fin
- [ ] Budget LLM visible par mission (FinOps)
- [ ] Audit trail consultable

## Phase 6 — Client Portal (déclencheur : 5 clients actifs)

**Objectif** : portail **read-only** pour les clients.

**Inclus** :
- Statut projet, livrables, rapports qualité, décisions ADR, factures, feedback, roadmap client, accès read-only GitHub.

**Exclu (Phase 7 ou jamais)** :
- Self-service complet, multi-tenant complexe, billing SaaS, marketplace agents, permissions fines excessives.

cf. `docs/architekt/phase-6-client-portal.md`.

## Phase 7 — SaaS Option (déclencheur : 10+ clients, 3 offres répétables, marge stable)

**Objectif** : envisager productisation (et **seulement** envisager).

Si décidé : multi-tenant, abonnement, usage-based pricing, marketplace templates, dashboard CTO, audit automation.

cf. `docs/architekt/phase-7-saas.md`.

## ADR (Architecture Decision Records)

| # | Sujet | Statut |
|---|-------|--------|
| 001 | Rebrand Architekt | Proposé |
| 002 | Modular monolith par défaut | Proposé |
| 003 | Mutation testing (Stryker/mutmut/PIT) | Proposé |
| 004 | Design system shadcn+Radix+Tailwind v4 | Proposé |
| 005 | Hébergement pilote (Hetzner + Cloudflare) | Proposé |
| 006 | Licence (open-core → propriétaire interne révisé) | Proposé |
| **008** | **Offers before stacks** | À écrire |
| **009** | **Internal platform before SaaS** | À écrire |
| **010** | **Human approval policy for agents** | À écrire |
| **011** | **LLM cost governance (FinOps)** | À écrire |
| **012** | **SBOM and supply-chain baseline** | À écrire |
| **013** | **Client IP and AI-generated code policy** | À écrire |
| **014** | **Accessibility baseline WCAG 2.2 AA** | À écrire |
| **015** | **Quality report as commercial artifact** | À écrire |
| **016** | **Pricing model and margin targets** | À écrire |
| **017** | **Cloud deployment decision matrix** | À écrire |
| **018** | **Data retention and client isolation** | À écrire |
| **019** | **Agent audit logs and reproducibility** | À écrire |
| **020** | **When to introduce multi-tenancy** | À écrire |

## Risques (registre)

cf. `docs/RISKS.md`. Synthèse :

| Risque | Gravité | Mitigation |
|--------|---------|-----------|
| Trop de stacks trop tôt | Haute | Tier A/B/C strict |
| Agents rapides mais code fragile | Haute | CI + tests + review humaine (DORA 2025 cf. amplificateur) |
| Coût LLM invisible | Haute | FinOps par mission, alertes |
| Pas de pipeline commercial | **Critique** | Offres packagées + outreach + IMDA |
| Delivery non rentable | **Critique** | Marge brute par projet ≥ 50 % |
| Sécurité insuffisante B2B | Haute | OWASP ASVS + NIST SSDF + SBOM |
| Confusion agence/SaaS | Haute | Studio jusqu'à 3-5 clients minimum |
| Design system non gouverné | Moyenne | Tokens + audit a11y vérifié |
| Fondateurs surchargés | Haute | Playbooks + scope strict |
| Site vitrine sans preuve | Moyenne | Rapports qualité publics |

## Indicateurs (suivis dans GitHub Project)

| Indicateur | P3 cible | P4 cible | P5 cible |
|------------|----------|----------|----------|
| CI verte sur `main` | 100% | 100% | 100% |
| Couverture mutation testing (critique) | ≥ 60% | ≥ 70% | ≥ 80% |
| Time-to-first-agent-message | < 5 min | < 2 min | < 2 min |
| Concurrence missions | 1 | 3 | 5 |
| Marge brute projet | n/a | > 50% | > 55% |
| Coût LLM tracé / mission | partiel | 100% | 100% |
| SBOM par release | non | oui | oui |
| Time-to-new-mission | n/a | < 30 min | < 10 min |
| NPS client | n/a | > 8 | > 8 |

## Sources externes (ce sur quoi cette roadmap s'appuie)

- **DORA 2025 Report — State of AI-assisted Software Development** (Google Cloud / Google Research, juin-juillet 2025, ~5 000 répondants) — l'IA comme amplificateur, throughput vs stability, foundation challenges vs harmonious high achievers.
- **NIST SP 800-218 SSDF v1.1** (févr. 2022) + **v1.2 IPD** (déc. 2025) — Secure Software Development Framework, mapping ASVS.
- **OWASP ASVS v5** — Application Security Verification Standard, niveaux 1/2/3.
- **CycloneDX & SPDX** — formats SBOM standards (NTIA minimum elements).
- **Shopify / Amazon Prime Video 2023-2026** — retours d'expérience modular monolith vs microservices.
- **Spring Modulith 2.x** (mars 2026) — outil Java modular monolith.
- **Stryker Mutator, mutmut, PIT** — mutation testing JS/TS/Python/Java.
- **shadcn/ui + Radix + Tailwind v4** — consensus marché 2026 design system.
- **IMDA Singapore Digital Economy Report 2025** — SMEs IA adoption 14.5 % (vs 4.2 % en 2023), non-SMEs 62.5 % (vs 44 %).
- **IMDA NAIIP / DEB / SME AI Impact Awards 2026** — programmes subvention SMEs Singapour, 50 000 SMEs cible 2029, vendor pre-approval list.
- **IDP landscape 2026** (Backstage, Humanitec, Port, Fortem) — référence pour Phase 5.

## Liens

- `docs/OFFERS.md` — 5 offres packagées + SOW templates
- `docs/CATALOG.md` — catalogue technos tierisé A/B/C
- `docs/RISKS.md` — registre risques détaillé
- `docs/GTM.md` — stratégie Go-to-market APAC (Singapour, IMDA)
- `docs/architekt/phase-{0..7}.md` — guides détaillés par phase
- `docs/adr/001..020` — ADR
- `docs/skills-spec/` — spécifications des 12 skills Architekt
- `.github/labels.yml` — labels GitHub
- `scripts/github/setup-project.sh` — peuple GitHub Issues + Project + Milestones
