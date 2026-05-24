# Architekt — Catalogue d'offres

> Ce qu'on **vend**, à qui, pour combien, et ce qu'on livre.
> 5 offres packagées. Chacune = un livrable client clair, un prix indicatif, un SOW template.

## Principe

> **On vend des livrables, pas des frameworks.**

Un client n'achète pas "Astro + FastAPI". Il achète "un site corporate livré vite avec rapport qualité".
Chaque offre = 1 problème business + 1 livrable + 1 prix + 1 délai cible.

## Les 5 offres

### 1. **Architekt Launch** — Site + brand + analytics

| | |
|--|--|
| **Pour qui** | Scale-up / SME APAC qui lance / refait son site |
| **Durée** | 2-3 semaines |
| **Prix cible** | **5 000 – 15 000 SGD** |
| **Livrables** | Site Astro / Next.js (selon besoin), brand minimal, analytics (Plausible ou GA4), SEO de base, hébergement Cloudflare Pages, rapport qualité |
| **Stack défaut** | Astro 5 + Tailwind v4 + shadcn/ui + Cloudflare Pages |
| **Inclus** | 1 langue (option +1k par langue), brief créatif, 2 rounds de revue |
| **Non inclus** | Création contenu long (copywriting brand strategy), shootings photo, animations 3D |
| **Marge cible** | ≥ 60 % |

### 2. **Architekt MVP** — App web exploitable

| | |
|--|--|
| **Pour qui** | Founder / produit qui valide une idée B2B ou B2C |
| **Durée** | 4-8 semaines |
| **Prix cible** | **20 000 – 60 000 SGD** |
| **Livrables** | App web fullstack (auth, dashboard, base de données, intégration paiement si besoin), CI, monitoring, runbook, handover doc |
| **Stack défaut** | Next.js 15 + FastAPI ou NestJS + PostgreSQL + Cloudflare Pages + Hetzner/Fly.io |
| **Inclus** | Discovery 3 jours, archi (ADR), 2 sprints, hardening, formation handover |
| **Non inclus** | Marketing site (offre Launch séparée), TMA long terme (offre Run séparée) |
| **Marge cible** | ≥ 50 % |

### 3. **Architekt Internal Tool** — Outil métier interne

| | |
|--|--|
| **Pour qui** | PME APAC avec processus métier manuel (CRM léger, suivi production, back-office) |
| **Durée** | 3-6 semaines |
| **Prix cible** | **15 000 – 40 000 SGD** |
| **Livrables** | Outil web interne, auth SSO si demandé, intégration ERP/CRM existant (1-2 systèmes), reporting, doc utilisateur |
| **Stack défaut** | Next.js + FastAPI + PostgreSQL (ou WordPress + custom plugins pour cas simples) |
| **Inclus** | Discovery utilisateurs, 2 rounds prototypage, formation équipe |
| **Non inclus** | Intégration > 2 systèmes (chiffré séparément) |
| **Marge cible** | ≥ 55 % |

### 4. **Architekt AI Workflow** — Automatisation IA contrôlée

| | |
|--|--|
| **Pour qui** | Entreprise qui veut intégrer des agents IA dans ses processus (support, contenu, RAG interne, automation) |
| **Durée** | 2-6 semaines |
| **Prix cible** | **10 000 – 50 000 SGD** |
| **Livrables** | Workflow IA déployé (n8n / Architekt Platform / custom), garde-fous (human-in-the-loop, audit), monitoring coûts, doc runbook |
| **Stack défaut** | Architekt Platform + LLM provider client (Azure OpenAI, Anthropic, Vertex AI) ou n8n hosted |
| **Inclus** | Discovery use case, POC 1 semaine, mise en prod avec garde-fous, formation |
| **Non inclus** | Modèles entraînés sur mesure (offre séparée si demande) |
| **Marge cible** | ≥ 55 % |
| **Différenciant** | "Speed of AI + rigor of senior engineering" — agents + audit + FinOps |

### 5. **Architekt Audit** — Rapport CTO + roadmap

| | |
|--|--|
| **Pour qui** | Entreprise qui hérite d'un système / veut un avis externe / prépare une levée |
| **Durée** | 1 semaine |
| **Prix cible** | **3 000 – 10 000 SGD** |
| **Livrables** | Rapport audit (archi, code, sécu, ops, équipe), scorecard qualité, roadmap 90 jours / 6 mois / 12 mois, présentation 1h |
| **Stack défaut** | Architekt Platform (QualityScanner exécuté sur le repo client) + interviews |
| **Inclus** | 3 interviews (CTO, dev lead, ops), accès repo read-only, rapport 20-40 pages |
| **Non inclus** | Implémentation (offres MVP/Internal Tool séparées) |
| **Marge cible** | ≥ 70 % |
| **Rôle commercial** | **Wedge offer** — petit ticket, ouvre la porte à des contrats plus gros |

## Matrice offres × cibles

| Cible | Launch | MVP | Internal Tool | AI Workflow | Audit |
|-------|--------|-----|---------------|-------------|-------|
| Startup early-stage | ✅ | ✅ | — | ✅ | — |
| Scale-up | ✅ | ✅ | ✅ | ✅ | ✅ |
| PME établie APAC | ✅ | — | ✅ | ✅ | ✅ |
| Grand compte (>200 personnes) | — | — | ✅ | ✅ | ✅ |
| Agence partenaire (white-label) | — | ✅ | ✅ | ✅ | — |

## Critères accept / refuse (intake checklist)

Architekt **refuse** un projet si :

- ❌ Pas de PO/sponsor identifié côté client
- ❌ Budget < seuil bas de l'offre (-30 %)
- ❌ Délai imposé incompatible avec scope
- ❌ Stack imposée hors Tier A ou B (sauf signature contrat Tier C avec premium)
- ❌ Domaine régulé sans budget compliance (santé, banque, défense)
- ❌ Conflit IP / clause AI restrictive non négociable

Architekt **accept** si :

- ✅ Sponsor exécutif identifié
- ✅ Budget validé dans la fourchette
- ✅ Scope cadrable en ≤ 3 jours (Discovery payée si > 1 j)
- ✅ Stack dans Tier A ou B
- ✅ Conditions IP/AI compatibles avec Architekt-MSA-template

## SOW template (structure)

Chaque offre a un SOW (Statement of Work) standard :

```
1. Contexte & objectifs
2. Périmètre (in scope / out of scope)
3. Livrables détaillés
4. Stack & architecture
5. Planning (jalons, gates)
6. Équipe Architekt (rôles, % allocation)
7. Engagement client (PO, points hebdo, validations)
8. Prix & modalités (forfait, jalons, T&M cap)
9. Conditions IP & code (cf. MSA + ADR-013)
10. Garanties post-livraison (30 jours hotfix)
11. Annexes (NFRs, sécurité, a11y, perf)
```

Template par offre dans `docs/offers/<offre>-sow.md` (à créer en Phase 0).

## FinOps par offre

| Offre | Budget LLM cible | Heures humaines max | Coût infra max | Marge minimale |
|-------|------------------|---------------------|----------------|----------------|
| Launch | 100 SGD | 40 h | 50 SGD/mois (3 mois inclus) | 60 % |
| MVP | 500 SGD | 200 h | 200 SGD/mois (3 mois inclus) | 50 % |
| Internal Tool | 300 SGD | 120 h | 150 SGD/mois | 55 % |
| AI Workflow | 1 000 SGD | 100 h | 300 SGD/mois | 55 % |
| Audit | 50 SGD | 30 h | 0 | 70 % |

> Si dépassement projeté > 10 % en cours de mission → escalade au CPO/CTO + décision : continuer (impact marge), facturer avenant, ou scope cut.

## Suivi commercial

À tracker dans CRM (Notion / Airtable / Pipedrive) :

| Étape | Champs clés |
|-------|-------------|
| Lead | Source, offre cible, urgence, budget approx |
| Qualified | Sponsor, scope, deadline, stack |
| Devis envoyé | Offre, prix, date envoi |
| Signé | Date signature, montant, équipe assignée |
| En cours | Mission ID plateforme, marge prévisionnelle |
| Livré | NPS, marge réelle, case study OK ? |
| Récurrent | Contrat run / TMA actif |
