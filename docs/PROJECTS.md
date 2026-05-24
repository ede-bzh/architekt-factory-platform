# Architekt — Catalogue de projets (10 typologies)

> 10 typologies de projets que Architekt sait délivrer.
> Distinct de `docs/OFFERS.md` (offres packagées) : ici on liste les **types techniques** de projets.

## Doctrine

> **Projet** = la nature technique (site, MVP, portail…).
> **Offre** = le packaging commercial (Launch, MVP, Portal, Audit…).
> Un projet peut être livré via plusieurs offres. Une offre couvre 1-3 types de projets.

## A. Corporate / marketing platform

| | |
|--|--|
| Use cases | Company website, landing pages multilingues, thought leadership/blog, lead gen, case studies |
| Stack défaut | **Astro + Tailwind + shadcn/ui**, headless CMS optionnel |
| Niveau sécu | L0 (public statique) |
| Régions | Toutes |
| Offre cible | Architekt **Launch** |
| Hébergement | Cloudflare Pages |

## B. Product MVP

| | |
|--|--|
| Use cases | SaaS MVP, portail client, app workflow, dashboard |
| Stack défaut | **Next.js + FastAPI ou NestJS + PostgreSQL + Auth provider** |
| Niveau sécu | L1-L2 |
| Régions | APAC, EMEA, USA |
| Offre cible | Architekt **MVP** |
| Hébergement | Vercel/Cloudflare + Fly.io/Hetzner |

## C. Internal business tool

| | |
|--|--|
| Use cases | Admin panel, ops dashboard, workflow d'approbation, reporting tool |
| Stack défaut | **Next.js + FastAPI + PostgreSQL + RBAC** |
| Niveau sécu | L1-L2 |
| Régions | Toutes |
| Offre cible | Architekt **Internal Tool** |
| Hébergement | Fly.io/Hetzner ou cloud client |

## D. AI workflow automation

| | |
|--|--|
| Use cases | Extraction documents, génération propositions, assistant knowledge interne, triage support, automation reporting |
| Stack défaut | **Python/FastAPI + queue/background jobs + vector DB (si justifié) + audit logs** |
| Niveau sécu | L1-L2 (selon données) |
| Régions | Toutes |
| Offre cible | Architekt **AI Workflow** |
| Contrainte | **Human approval obligatoire** pour décisions sensibles (cf. ADR-010, ADR-036) |

## E. E-commerce / headless commerce

| | |
|--|--|
| Use cases | Shopify storefront, catalogue produits, storefront multi-langues, portail B2B |
| Stack défaut | **Shopify + frontend (Hydrogen/Next/Astro) + CMS** |
| Niveau sécu | L1-L2 |
| Régions | APAC, MENA, EMEA, USA |
| Offre cible | Architekt **Commerce** |
| Hébergement | Shopify hosting + Vercel/Cloudflare frontend |

## F. CMS / content platform

| | |
|--|--|
| Use cases | Site éditorial, resource centre, contenu multilingue |
| Stack défaut | **WordPress** (éditeurs non-techniques) OU **Payload/Strapi/Contentful** (headless développeur) |
| Niveau sécu | L0-L1 |
| Régions | Toutes |
| Offre cible | **Launch** ou **Internal Tool** |
| Contrainte | Choix WordPress vs headless basé sur **besoins éditeurs**, pas préférence dev |

## G. Client portal

| | |
|--|--|
| Use cases | Documents, factures, statut projet, rapports, messagerie sécurisée |
| Stack défaut | **Next.js + PostgreSQL + object storage + RBAC** |
| Niveau sécu | **L2** (sécurité baseline obligatoire) |
| Régions | Toutes |
| Offre cible | Architekt **Portal** |

## H. Data / analytics dashboard

| | |
|--|--|
| Use cases | KPIs business, métriques ops, reporting client |
| Stack défaut | **PostgreSQL + dbt (optionnel) + Metabase/Superset ou custom** |
| Niveau sécu | L1-L2 |
| Régions | Toutes |
| Offre cible | Internal Tool ou Portal |
| Contrainte | **Data quality contract requis** (sources, fraîcheur, owner) |

## I. Modernisation project

| | |
|--|--|
| Use cases | Cleanup app legacy, restructuration monolith, migration cloud, setup CI/CD |
| Stack défaut | **Dépend du client** |
| Architecture | **Modular monolith en premier**, strangler pattern si migration nécessaire |
| Niveau sécu | L2 |
| Régions | EMEA, USA, APAC |
| Offre cible | Architekt **Modernize** |

## J. Security / quality audit

| | |
|--|--|
| Use cases | Audit CTO, due diligence pré-levée, security baseline review, AI-readiness audit |
| Stack défaut | Architekt Platform (QualityScanner sur repo client) + interviews |
| Output | Rapport + roadmap + risk register + remediation backlog |
| Niveau sécu | Advisory |
| Régions | Toutes |
| Offre cible | Architekt **Audit** |

## Matrice projet → offre Architekt

| Projet | Architekt Offre |
|--------|-----------------|
| A. Corporate/marketing | **Launch** |
| B. Product MVP | **MVP** |
| C. Internal business tool | **Internal Tool** |
| D. AI workflow | **AI Workflow** |
| E. E-commerce | **Commerce** |
| F. CMS / content | **Launch** (WP) ou **Internal Tool** (headless) |
| G. Client portal | **Portal** |
| H. Data dashboard | **Internal Tool** ou **Portal** |
| I. Modernisation | **Modernize** |
| J. Audit | **Audit** |

## Référence transverse

- Stack par projet : `docs/STACK-MATRIX.md`
- Architecture par projet : `docs/ARCHITECTURES.md`
- Sécurité par projet : `docs/SECURITY.md`
- Compliance par région : `docs/COMPLIANCE.md`
