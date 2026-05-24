---
name: Architekt Architecture
description: Doctrine architecture Architekt — modular monolith par défaut, catalogue patterns, matrice stack (ADR-002, ADR-037, ADR-038)
tags: [architecture, architekt, monolith, adr]
metadata:
  category: archi
  triggers: [intake, adr, stack-choice, pattern, c4]
---

# Architekt Architecture

## Objectif

Encoder la **doctrine architecture Architekt** : pattern par défaut, catalogue officiel, matrice stack — pour que tout agent architecte décide vite et de façon cohérente.

## Quand utiliser

- Intake projet (choix pattern + stack)
- Rédaction ADR projet client
- Revue architecture mi-mission
- Demande d'extraction microservice ou changement stack

## Pattern par défaut : modular monolith (ADR-002)

```
1 projet = 1 service déployable
  ↳ modules internes stricts (packages, API inter-modules)
  ↳ tables par module (logique)
  ↳ microservice UNIQUEMENT si critères cumulatifs (≥2/3) :
     • cadence déploiement différente
     • profil scale différent (CPU/RAM/IO)
     • équipe propriétaire distincte
  ↳ serverless = jobs/events ponctuels, pas architecture globale
```

## Catalogue 6 patterns (ADR-037)

| Pattern | Use case |
|---------|----------|
| Static-first | Marketing, landing, docs |
| **Modular monolith** | MVP, B2B, internal tools (défaut) |
| API-first backend | Portails, intégrations, mobile futur |
| Headless commerce/content | E-commerce, omnichannel |
| AI workflow | Automation, assistants, doc processing |
| Multi-region-ready | Clients internationaux, data residency |

Chaque projet déclare son pattern dans un **ADR projet**.

## Matrice stack (ADR-038)

| Type projet | Stack par défaut |
|-------------|------------------|
| Marketing | Astro + Tailwind + shadcn + Cloudflare Pages |
| Web app interactive | Next.js + PostgreSQL + FastAPI/NestJS |
| Internal tool | Next.js + FastAPI + PostgreSQL + SSO |
| AI workflow | Python + FastAPI + workers + PostgreSQL (+ pgvector si justifié) |
| E-commerce | Shopify first, headless si besoin |
| Enterprise Java | Spring Modulith (trigger explicite) |
| Mobile | PWA/responsive d'abord, native si validé |

**Règle d'or** : 1 type projet = 1 stack par défaut. Variation = ADR projet obligatoire.

## Outillage boundaries par stack

| Stack | Vérification modules |
|-------|---------------------|
| Java | Spring Modulith verify |
| Python | Packages stricts + pytest-architecture |
| Node/TS | Monorepo Nx ou packages npm internes |
| Next.js | App Router + dossiers `features/` cloisonnés |

## Livrables architecte

- ADR projet (pattern, stack, data residency, intégrations)
- Diagramme C4 (contexte + containers minimum)
- Liste risques architecture + mitigations
- Décision auth (Clerk/Auth0, Entra ID, OIDC/SAML)

## Anti-patterns

- ❌ Microservices par défaut sans critères d'extraction
- ❌ Stack hors Tier A/B sans avenant premium ou refus
- ❌ Pas d'ADR sur décision structurante
- ❌ "Big ball of mud" (imports cross-module sauvages)
- ❌ Choisir stack avant type projet identifié

## Sources

- ADR-002 Modular monolith
- ADR-037 Architecture patterns catalogue
- ADR-038 Stack decision matrix
- Amazon Prime Video monolith rollback, Shopify modular monolith
