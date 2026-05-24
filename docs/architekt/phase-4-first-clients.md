# Phase 4 — First Paid Clients

> Durée cible : **1-3 mois** (selon vitesse pipeline commercial)
> Dépend de : Phase 3 (site live + actifs commerciaux)
> Sortie : **3 clients payants signés et livrés**, marge mesurée, répétabilité prouvée

## Objectif

Sortir du mode "exploration" et entrer en mode "commercial production" : prouver que Architekt **vend, livre et margine** sur des projets réels.

## Métriques cibles (à atteindre fin Phase 4)

| Indicateur | Cible | Source mesure |
|------------|-------|---------------|
| Clients payants signés | **3** | CRM |
| Case studies réels publiés | **2** | Site Architekt `/proof` |
| Marge brute par projet | **> 50 %** | Comptabilité projet |
| Dépassement budget LLM par mission | **< 10 %** | Plateforme FinOps |
| Temps cadrage → devis | **< 48 h** | CRM timestamps |
| Time-to-first-demo (post-kickoff) | **< 5 jours** | Plateforme |
| NPS client | **> 8/10** | Enquête fin de projet |
| Rework post-livraison (jours) | **< 15 %** durée projet | Comptabilité projet |
| Bugs P1/P2 en prod post-livraison | **0** | Incidents trackés |
| Temps handover client | **< 2 jours** | Plateforme |

## Acquisition — 6 canaux à tester en parallèle

Détails dans `docs/GTM.md`. Synthèse :

| Canal | Effort | ROI estimé 3 mois |
|-------|--------|-------------------|
| IMDA NAIIP pre-approved vendor | 1-2 mois candidature | 2-5 leads/mois |
| LinkedIn outbound CTO/founder SG | 2-3 h/sem | 1-3 leads/mois |
| Content marketing + SEO | 1 post/sem | 2-5 leads/mois (mois 6+) |
| Partenariats consultants SG | 3-5 meetings/mois | 1-3 leads/mois |
| Candidature SME AI Impact Awards 2026 | 1 application | Visibilité (pas leads court terme) |
| Partenariat Grab AI for SMEs (DEB) | Discussions partenariat | Potentiel énorme |

**Wedge offer prioritaire** : **Architekt Audit** (3-10k SGD, 1 semaine) → ouvre la porte à MVP / Internal Tool.

## Funnel cible

```
Leads top-funnel    : 30 / mois  (multi-canaux)
Qualifiés           : 10 / mois
Devis envoyés       : 4 / mois
Signés (audit)      : 2 / mois
Signés (delivery)   : 1 / mois → conversion audit → delivery : 50 %

3 mois cumulés      : 3 clients delivery signés (1/mois en rythme)
```

## Process projet client (par mission)

### 1. Intake (1-3 jours)

- [ ] Lead qualifié (sponsor, budget, deadline)
- [ ] Discovery call (45 min) → notes dans CRM
- [ ] Application **intake checklist** (`docs/intake-checklist.md` à créer)
- [ ] Choix offre (cf. `docs/OFFERS.md`)
- [ ] Devis envoyé < 48 h

### 2. Signature (1-7 jours)

- [ ] NDA signé (si demandé)
- [ ] MSA signé
- [ ] SOW signé (spécifique projet)
- [ ] 30 % prépayement reçu
- [ ] Projet créé dans plateforme Architekt
- [ ] Repo client provisionné (template Tier A)

### 3. Discovery (3-5 jours pour MVP/Internal Tool)

- [ ] Mission idéation lancée
- [ ] Brief + objectifs + jobs-to-be-done
- [ ] ADR projet (`<projet>/docs/adr/`)
- [ ] Roadmap projet validée client

### 4. Build (2-6 semaines selon offre)

- [ ] Sprints itératifs
- [ ] Point hebdo avec client
- [ ] Démo intermédiaire (J5 puis hebdo)
- [ ] Mutation testing modules critiques
- [ ] CI verte continue

### 5. Hardening (1-2 semaines)

- [ ] Pentest interne (sast-continuous workflow)
- [ ] Rapport qualité généré (DORA + Lighthouse + Stryker + SBOM)
- [ ] Documentation utilisateur
- [ ] Runbook (cf. `architekt-sre.md`)

### 6. Handover (1-2 jours)

- [ ] Repo transféré (cession IP totale, cf. MSA)
- [ ] Doc handover (`<projet>/HANDOVER.md`)
- [ ] Formation 1-2 h
- [ ] 40 % paiement intermédiaire
- [ ] Démo finale client

### 7. Closure (2 semaines après)

- [ ] 30 % paiement final
- [ ] NPS survey
- [ ] Demande case study (avec accord)
- [ ] 30 jours hotfix offerts
- [ ] Retro interne (qualité méthode)

## Retro post-mission (template)

À écrire pour chaque projet dans `docs/case-studies/<client>.md` (interne) :

```
## Projet
- Client, offre, dates, équipe
## Métriques réelles
- Marge brute, coût LLM, heures réelles vs prévu
- Lighthouse, Stryker, Lighthouse, etc.
- NPS, rework
## Ce qui a marché
- ...
## Ce qui n'a pas marché
- ...
## Ajustements méthode
- Skills à enrichir
- Workflows à modifier
- Pricing à ajuster
## Case study publiable ?
- Oui / Non / Anonymisé
```

## Déclencheurs pendant Phase 4

| Trigger | Action |
|---------|--------|
| 1er client signé | Issue GitHub `[CLIENT]` créée, kit stack activé si Tier B |
| 1er dépassement budget LLM > 10 % | Revue immédiate FinOps |
| 1er rework > 15 % | Revue méthode + ajustement skills |
| 3e client signé | Préparer spec **Phase 5 IDP** |
| 5e mission en parallèle | Augmenter Semaphore plateforme (>1) |
| 1er client récurrent (run/TMA) | Lancer offre **Architekt Run** formalisée |

## Pré-requis

- Phase 3 mergée + `architekt.*` live
- Pipeline commercial démarré (au moins 1 canal actif)
- Entité légale SG opérationnelle (compte bancaire, GST si applicable)
- CRM choisi et configuré (Notion / Airtable / Pipedrive)
- Compte facturation (Stripe / Xero / SG accounting standard)

## Gate de passage

- [ ] 3 clients payants signés et livrés (closure complète)
- [ ] 2 case studies réels publiés sur site Architekt
- [ ] Marge brute mesurée et communicable (rapport interne)
- [ ] Au moins 1 client récurrent (TMA, run, retainer)
- [ ] Spec `docs/architekt/phase-6-client-portal.md` détaillée (déclencheur 5 clients)
- [ ] Retros post-mission complètes pour les 3 projets

## Risques

| Risque | Mitigation |
|--------|-----------|
| Pas de leads (R1) | 3 canaux en parallèle, pivot à 4 semaines si rien |
| Marge < 50 % (R2) | Revue immédiate, scope cut ou renégociation |
| Burnout (R8) | 1 client à la fois maximum (Semaphore = 1 jusqu'à process stabilisé) |
| Sur-promesse | Definition of done stricte, gates client signés |
| Client refus case study | Anonymiser ou créer case study fictif inspiré |
