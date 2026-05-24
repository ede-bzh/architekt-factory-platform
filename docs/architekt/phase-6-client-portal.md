# Phase 6 — Client Portal

> Déclencheur : **5 clients actifs** ou **3 clients récurrents**
> Durée : 4-6 semaines une fois lancé
> Statut : **conditionnel** (ne pas démarrer avant trigger)

## Objectif

Donner aux clients un **portail read-only** pour suivre leur projet sans dépendre d'emails / Slack / appels.

## Pourquoi attendre 5 clients

- En dessous de 5, l'overhead de support direct est plus simple
- Au-delà, les emails / DMs deviennent ingérables
- 5 clients = signal que les patterns d'usage sont stables

## Inclus dans v1

| Capacité | Détail |
|----------|--------|
| **Statut projet** | Phase actuelle, sprint en cours, % completion, prochaine démo |
| **Livrables** | Liste des livrables passés + à venir (téléchargement) |
| **Rapports qualité** | DORA + Lighthouse + Stryker + SBOM exportables PDF |
| **Décisions ADR** | Liste des ADR projet avec statut |
| **Factures** | Téléchargement factures émises + statut paiement |
| **Feedback** | Formulaire NPS + commentaires libres |
| **Roadmap client** | Vue Kanban roadmap projet (read-only) |
| **Accès read-only GitHub** | Lien vers repo (si client n'a pas accès direct) |

## Exclu de v1 (Phase 7 ou jamais)

- Self-service complet (créer mission depuis le portail)
- Multi-tenant complexe (1 tenant = 1 client, isolation simple)
- Billing automatique SaaS
- Marketplace d'agents
- Permissions fines (admin/viewer suffit)
- Notifications real-time push
- Workspace collaboratif client

## Architecture (proposition)

```
Portal client (Next.js)
  ↓ API read-only
Architekt Platform API (FastAPI)
  ↓ DB lookup
PostgreSQL (tenant isolation par client_id)
```

- Auth : magic link email (pas de password)
- 1 utilisateur principal par client + jusqu'à 3 invités
- Read-only strict (aucune mutation depuis le portail)
- PDPA compliant (consent banner si analytics)

## Plan en 4-6 semaines

| Semaine | Livrable |
|---------|----------|
| 1 | Spec UX + wireframes |
| 2 | Auth + tenant isolation (DB) |
| 3 | Pages statut + livrables + rapports |
| 4 | Factures + feedback + roadmap |
| 5 | Tests, sécurité, audit a11y |
| 6 | Pilote avec 1 client, ajustements, release |

## Pré-requis

- Phase 5 mergée (IDP fonctionnel, cost tracker en place)
- 5 clients actifs (ou 3 récurrents)
- Décision UI : Next.js + shadcn (cohérent stack Architekt)

## Gate de passage

- [ ] Portail accessible `clients.architekt.*`
- [ ] 1 client pilote l'utilise avec satisfaction
- [ ] Audit a11y WCAG 2.2 AA passé
- [ ] PDPA conformité vérifiée
- [ ] 100 % des données affichées sont lues depuis sources de vérité (pas de duplication)

## Risques

| Risque | Mitigation |
|--------|-----------|
| Construire trop tôt | Trigger strict (5 clients) |
| Feature creep self-service | Read-only strict v1, pas de négociation |
| Maintenance lourde | UI simple, peu d'écrans, shadcn pour ne pas réinventer |
| Compliance multi-juridiction | PDPA SG d'abord, GDPR à part si client EU |

## Suivi

- Milestone GitHub : **Phase 6 — Client Portal** (créé au trigger)
- Labels : `phase:6-portal`, `area:portal`
