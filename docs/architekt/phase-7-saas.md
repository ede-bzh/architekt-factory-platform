# Phase 7 — SaaS Option (conditionnel)

> Déclencheur : **10+ clients**, **3 offres répétables**, **marge stable > 50 %**
> Durée : 6-12 mois si lancé
> Statut : **conditionnel** (ne pas démarrer sans trigger)

## Objectif (si on y va)

Productiser la plateforme Architekt en SaaS pour permettre à d'**autres studios / agences / startups** de l'utiliser en self-service.

## Pourquoi attendre 10 clients

- Avant 10, on n'a pas assez de signal de produit-market fit
- Multi-tenant + billing + support self-service = coût opérationnel énorme
- Studio + delivery doit déjà être profitable à ce stade
- 10 clients = environ 12-18 mois après Phase 4

## Décisions structurantes (à reconsidérer au trigger)

| Question | Réponse à clarifier |
|----------|---------------------|
| Plateforme = SaaS public ou private cloud client ? | À trancher selon demande marché |
| Modèle pricing | Abonnement + usage-based LLM tokens |
| Cible | Petites agences (notre ICP), pas direct SME |
| Quel reste différenciant vs OSS pur ? | Skills Architekt, support, hosting managé |

## Capacités à construire (si décidé)

| Capacité | Effort |
|----------|--------|
| Multi-tenant (vrai, pas faux comme Phase 6) | 4-6 semaines |
| Auth enterprise (SSO OIDC / SAML) | 2-3 semaines |
| Billing (Stripe + usage-based) | 4 semaines |
| Workspace client isolé (compute + storage) | 4-6 semaines |
| Dashboard CTO (DORA cross-projets) | 2-3 semaines |
| Marketplace templates / skills | 4-8 semaines |
| Audit automation (SOC2 / ISO 27001 baseline) | 8-12 semaines |
| Support tier (helpdesk, SLA) | équipe dédiée |

## Modèle économique (hypothèses)

| Plan | Cible | Prix indicatif | Inclus |
|------|-------|----------------|--------|
| **Starter** | Freelance / petite agence | 99 USD/mo + usage LLM | 1 seat, 5 missions/mo, support email |
| **Studio** | Agence 5-20 personnes | 499 USD/mo + usage LLM | 10 seats, 50 missions/mo, support priorité |
| **Enterprise** | Grand compte | Custom (10k+ USD/mo) | Self-hosted ou private cloud, SSO, SLA |

## Risques majeurs

| Risque | Gravité | Mitigation |
|--------|---------|-----------|
| Distraire du delivery client (qui paye le présent) | **Critique** | Trigger strict, équipe SaaS séparée |
| Cannibaliser les services Architekt | Haute | Pricing SaaS doit dégrader UX vs delivery custom |
| Compliance (SOC2, ISO, RGPD multi-juridiction) | Haute | Investissement avocat + auditeur + DPO |
| Coût acquisition SaaS énorme | Haute | Vendre d'abord aux partenaires connus (warm) |
| Concurrence (Devin, Factory, Lovable, etc.) | Haute | Wedge APAC + studio premium → différenciation |

## Pré-requis (cumulés)

- ≥ 10 clients livrés
- ≥ 3 offres répétables (pricing stable)
- Marge brute > 50 % sur 6 mois consécutifs
- Embauche : équipe ≥ 5 personnes (besoin d'un Head of Product SaaS distinct du studio)
- Cash : 12+ mois de runway pour absorber l'investissement
- Décision board / fondateurs : "on veut vraiment être un éditeur SaaS"

## Gate de démarrage

Aucun travail Phase 7 ne démarre tant que :

- [ ] 10 clients livrés
- [ ] 3 offres répétables
- [ ] Marge > 50 % 6 mois
- [ ] Équipe ≥ 5 personnes
- [ ] Décision formelle écrite (`docs/decisions/saas-go-no-go.md`)

## Alternative à Phase 7

Si après 10 clients on décide **de ne pas faire de SaaS** :

- Continuer en studio premium → embaucher, ouvrir bureaux ASEAN
- Vendre la plateforme à une entreprise (acquisition)
- Open-source partiel (composants non-différenciants)
- Rester boutique de 10-30 personnes, marge 30-40 %

Ces options sont tout aussi valides que la productisation SaaS.

## Suivi

- Milestone GitHub : **Phase 7 — SaaS Option** (créé seulement si trigger)
- Labels : `phase:7-saas`, `area:saas`
- Décision document : `docs/decisions/saas-go-no-go.md` (à écrire au trigger)
