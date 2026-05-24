# Architekt — KPIs et indicateurs

> Indicateurs suivis par Architekt à tous les niveaux (commercial, delivery, sécurité, architecture, international, finance).
> Source de vérité unique pour les revues hebdo / mensuelles / trimestrielles.

## Catégories

1. Market / Sales
2. Delivery
3. Security
4. Architecture
5. International readiness
6. Finance
7. Plateforme (interne)

---

## 1. Market / Sales

| KPI | Cible Phase 4 | Cible Phase 5+ | Source mesure |
|-----|---------------|----------------|---------------|
| Revenue total / mois | n/a → 5-15k SGD | 30-50k SGD | CRM + facturation |
| Revenue par région | n/a | tracked | CRM |
| Revenue par offre | n/a | tracked | CRM |
| Average project value | n/a | > 25k SGD | CRM |
| Proposal-to-close rate | n/a | > 25 % | CRM |
| Lead source | tracked | tracked | CRM (`source` field) |
| Client type (cf. CLIENTS.md) | tracked | tracked | CRM |
| Project type (cf. PROJECTS.md) | tracked | tracked | CRM |
| Leads qualifiés / mois | 10 | 20 | CRM |
| Pipeline ouvert (SGD) | 50k+ | 200k+ | CRM |
| CAC (Coût Acquisition Client) | < 1k SGD | < 1,5k SGD | Compta + CRM |
| Taux refus projet | 30 % | 40 % | CRM (signal qualité filtre) |

## 2. Delivery

| KPI | Cible Phase 4 | Cible Phase 5+ | Source mesure |
|-----|---------------|----------------|---------------|
| Time-to-first-demo | < 5 jours | < 3 jours | Plateforme |
| Cycle time (story → prod) | < 7 jours | < 4 jours | DORA |
| Rework rate | < 15 % | < 10 % | Compta projet |
| Region-specific assumptions missed | 0 critiques | 0 critiques | INTAKE.md vérifié |
| Client acceptance delay | < 5 jours | < 3 jours | Plateforme |
| Bugs P1/P2 post-livraison (30 j) | 0 | 0 | Incident tracker |
| NPS client | > 8/10 | > 9/10 | Survey post-mission |
| Temps handover client | < 2 jours | < 1 jour | Plateforme |
| Mission rejection rate (adversarial) | < 20 % | < 15 % | Plateforme `agent_scores` |
| Adversarial L0/L1 catches | tracked | tracked | Plateforme |

## 3. Security

| KPI | Cible Phase 4 | Cible Phase 5+ | Source mesure |
|-----|---------------|----------------|---------------|
| Security level per project | tracked | tracked | INTAKE.md |
| Vulnerabilities by severity | < 5 medium | < 3 medium | SAST + SCA |
| Mean time to remediate (P1) | < 7 jours | < 3 jours | Issue tracker |
| Mean time to remediate (P2) | < 30 jours | < 15 jours | Issue tracker |
| SBOM generated | 100 % releases | 100 % releases | CI artifact |
| Secrets leaked in CI | **0** | **0** | TruffleHog |
| Projects with audit logs | 100 % L1+ | 100 % L1+ | Plateforme |
| Projects with backup tested | 100 % L1+ | 100 % L1+ | Runbook log |
| Pentest récent (< 1 an) | requis L3 | requis L2-L3 | Compliance log |
| Incident response drills | 0 | 1 / trimestre | Runbook log |

## 4. Architecture

| KPI | Cible Phase 4 | Cible Phase 5+ | Source mesure |
|-----|---------------|----------------|---------------|
| Architecture pattern used | tracked | tracked | ADR projet |
| Stack tier used (A/B/C) | majoritairement A | majoritairement A-B | Plateforme |
| Number of custom components | minimisé | minimisé | Plateforme |
| Number of third-party integrations | tracked | tracked | ADR projet |
| Deployment region | tracked | tracked | ADR projet |
| ADR count per project | ≥ 5 | ≥ 5 | Repo client |
| Modular monolith ratio | > 80 % | > 80 % | ADR projet |
| Microservices ratio | < 10 % | < 10 % | ADR projet |

## 5. International readiness

| KPI | Cible Phase 4 | Cible Phase 5+ | Source mesure |
|-----|---------------|----------------|---------------|
| Locales supportés (moyenne) | tracked | tracked | Plateforme |
| RTL required | tracked | tracked | INTAKE.md |
| Data residency requirement | tracked | tracked | COMPLIANCE.md |
| DPA required | 100 % EU/MENA | 100 % EU/MENA | Plateforme |
| Support timezone overlap | > 4 h | > 6 h | Contrat |
| Cross-border data flow | tracked + reviewed | tracked + reviewed | DPA |
| Conformité PDPA/GDPR/PDPL | 100 % projets concernés | 100 % | Audit |

## 6. Finance

| KPI | Cible Phase 4 | Cible Phase 5+ | Source mesure |
|-----|---------------|----------------|---------------|
| **Marge brute par projet** | > 50 % | > 55 % | Compta projet |
| LLM cost per project | < budget | < budget -10 % | Plateforme FinOps |
| Infrastructure cost per project | < budget | < budget -10 % | Cloud bills |
| Maintenance revenue (MRR Run) | 5-15k SGD | 30-50k SGD | Stripe / Xero |
| Project overrun percentage | < 15 % | < 10 % | Compta projet |
| Cash runway | > 6 mois | > 12 mois | Compta |
| Burn rate | tracked | tracked | Compta |
| Revenue par fondateur | n/a | tracked | Compta |

## 7. Plateforme (interne)

| KPI | Cible Phase 4 | Cible Phase 5+ | Source mesure |
|-----|---------------|----------------|---------------|
| CI verte sur `main` | 100 % | 100 % | GitHub Actions |
| Test pass rate | > 95 % | > 98 % | pytest |
| Mutation testing score (critiques) | ≥ 60 % | ≥ 70 % | Stryker/mutmut |
| Time-to-new-mission | n/a | < 10 min | Plateforme |
| Concurrence missions | 1 | ≥ 3 | Plateforme |
| Tenants isolés | non | oui (P6+) | Plateforme |
| Quality Report exporté | 100 % missions | 100 % missions | Plateforme |
| Audit log accessible | 100 % missions | 100 % missions | Plateforme |

## Indicateurs DORA (souverains, plateforme)

Référence : `platform/metrics/dora.py` existant.

| KPI DORA | Cible Phase 4 | Cible Phase 5+ |
|----------|---------------|----------------|
| Deployment frequency | 1+ / sem | 1+ / jour |
| Lead time for changes | < 1 jour | < 4 h |
| Change failure rate | < 15 % | < 10 % |
| Mean time to recovery | < 4 h | < 1 h |

## Revues

| Cadence | Indicateurs reviewed | Audience |
|---------|---------------------|----------|
| **Hebdo** (15 min) | Pipeline ouvert, leads qualifiés, missions actives, marge prévisionnelle | CPO + CTO |
| **Mensuel** (1 h) | Revenue, marge réelle, NPS, incidents, qualité | CPO + CTO + équipe |
| **Trimestriel** (3 h) | Toutes catégories + ajustement pricing/offres/stacks | Board + équipe |

## Outils suggérés

- **Dashboard interne** : Metabase ou Superset sur PostgreSQL (Phase 5)
- **CRM** : Notion / Airtable / Pipedrive (Phase 4)
- **Compta** : Xero (SG-friendly) ou QuickBooks
- **Compta projet** : Toggl / Harvest pour timesheet (si > 2 personnes)
- **Plateforme native** : `platform/metrics/` existant à enrichir

## Anti-patterns

- ❌ Tracker tous les KPIs dès le début (overhead pour 2 personnes) → 5-10 KPIs critiques d'abord
- ❌ KPIs sans owner → définir qui regarde et agit
- ❌ KPIs sans seuil → mesurer + comparer à cible
- ❌ Vanity metrics (visiteurs sans conversion, etc.)
- ❌ Mesurer sans modifier les process (revue sans action = perte de temps)
