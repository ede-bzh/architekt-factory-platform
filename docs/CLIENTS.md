# Architekt — Typologies de clients

> 9 typologies de clients cibles. Chaque type = besoins / régions / contraintes / offres pertinentes.
> Référencé dans `docs/OFFERS.md`, `docs/GTM.md`, ADR-030.

## Doctrine

> Architekt cible **2-3 typologies prioritaires** à un moment donné, pas les 9. Phase 4 (premiers clients) = scale-ups B2B + SMEs + professional services (APAC focus). Le reste s'ouvre selon traction et conformité.

## 1. Scale-ups B2B

| | |
|--|--|
| Besoins | MVP, platform engineering, AI workflows, internal tools, product acceleration |
| Régions | **APAC, EMEA, USA** |
| Offres pertinentes | MVP, AI Workflow, Audit, Run |
| Niveau sécu typique | L1-L2 |
| Ticket moyen | 30k-80k SGD |
| Contraintes | Vitesse, qualité prouvée, transparence IA, IP cession |
| Statut Architekt | **Cible prioritaire Phase 4** |

## 2. SMEs / mid-market businesses

| | |
|--|--|
| Besoins | Digitalisation, sites web, portails, intégrations CRM/ERP, automatisation |
| Régions | **APAC, MENA, EMEA** |
| Offres pertinentes | Launch, Internal Tool, AI Workflow, Run |
| Niveau sécu typique | L0-L1 |
| Ticket moyen | 10k-40k SGD |
| Contraintes | Budget serré, ROI rapide, peu de maturité technique |
| Statut Architekt | **Cible prioritaire Phase 4** (éligible IMDA NAIIP/DEB pour SG) |

## 3. Professional services (consulting, legal, accounting, real estate, recruitment)

| | |
|--|--|
| Besoins | Portails clients, workflows documents, knowledge automation, dashboards reporting |
| Régions | **APAC, EMEA, USA** |
| Offres pertinentes | Portal, Internal Tool, AI Workflow |
| Niveau sécu typique | **L2** (données client sensibles) |
| Ticket moyen | 20k-60k SGD |
| Contraintes | Confidentialité, retention, audit trail |
| Statut Architekt | **Cible prioritaire Phase 4** |

## 4. Hospitality / luxury / tourism

| | |
|--|--|
| Besoins | Sites multilingues, booking flows, intégrations CRM, concierge AI, UX premium |
| Régions | **MENA, APAC, EMEA** |
| Offres pertinentes | Launch (premium), Portal, AI Workflow |
| Niveau sécu typique | L1 |
| Ticket moyen | 15k-60k SGD |
| Contraintes | Design premium attendu, multi-langues (EN/AR/ZH/JA), RTL, marque importante |
| Statut Architekt | Cible Phase 5 (après stabilisation marque et design premium) |

## 5. Industrial / logistics / manufacturing

| | |
|--|--|
| Besoins | Dashboards opérationnels, workflow tools, portails fournisseurs, intégrations IoT/data |
| Régions | **MENA, APAC, EMEA** |
| Offres pertinentes | Internal Tool, Portal, Data dashboard |
| Niveau sécu typique | L1-L2 |
| Ticket moyen | 30k-100k SGD |
| Contraintes | Stack legacy souvent, intégrations multiples, données opérationnelles |
| Statut Architekt | Cible Phase 5+ |

## 6. Education / training

| | |
|--|--|
| Besoins | LMS, portails étudiants, workflows tutoring IA, plateformes contenu |
| Régions | **APAC, MENA, USA** |
| Offres pertinentes | MVP, Portal, AI Workflow |
| Niveau sécu typique | L2 (données mineurs souvent) |
| Ticket moyen | 30k-80k SGD |
| Contraintes | RGPD spécifique (mineurs), accessibilité forte, multi-rôles (étudiant/prof/parent) |
| Statut Architekt | Cible Phase 5+ |

## 7. Healthcare-adjacent / wellness

| | |
|--|--|
| Besoins | Systèmes rendez-vous, portails, formulaires d'intake sécurisés |
| Régions | APAC, EMEA, USA |
| Offres pertinentes | Portal, Internal Tool |
| Niveau sécu typique | **L2-L3** |
| Ticket moyen | 30k-80k SGD |
| **Contrainte forte** | **Éviter projets médicaux régulés** (HIPAA, dispositifs médicaux) jusqu'à maturité compliance Architekt |
| Statut Architekt | **Conditionnel** — wellness OK, médical régulé refusé (cf. ADR-041) |

## 8. E-commerce / retail

| | |
|--|--|
| Besoins | Shopify, headless commerce, catalogues produits, storefronts multilingues, analytics |
| Régions | **APAC, MENA, EMEA, USA** |
| Offres pertinentes | Commerce, Launch (vitrine), AI Workflow |
| Niveau sécu typique | L1-L2 (paiement, données client) |
| Ticket moyen | 15k-80k SGD |
| Contraintes | Performance UX, multi-langues, multi-monnaies, conversion |
| Statut Architekt | Cible Phase 4+ (kit Shopify à activer Tier B) |

## 9. Government-adjacent / public sector suppliers

| | |
|--|--|
| Besoins | Portails, accessibilité, sécurité, documentation conformité |
| Régions | APAC (SG/MY/AU), MENA (UAE/SA), EMEA |
| Offres pertinentes | Portal, Audit |
| Niveau sécu typique | **L3** |
| Ticket moyen | 50k-200k SGD |
| **Contrainte forte** | **Seulement après baseline sécu/compliance mature** (ISO 27001-ready, SBOM, audit logs, pentest récent) |
| Statut Architekt | **Conditionnel** — Phase 6+ minimum |

## Synthèse matrice

| # | Typologie | Régions principales | Phase Architekt | Offres clés |
|---|-----------|---------------------|-----------------|-------------|
| 1 | Scale-ups B2B | APAC, EMEA, USA | **P4 prioritaire** | MVP, AI Workflow, Audit |
| 2 | SMEs / mid-market | APAC, MENA, EMEA | **P4 prioritaire** | Launch, Internal Tool, AI Workflow |
| 3 | Professional services | APAC, EMEA, USA | **P4 prioritaire** | Portal, Internal Tool |
| 4 | Hospitality / luxury | MENA, APAC, EMEA | P5+ | Launch premium, Portal |
| 5 | Industrial / logistics | MENA, APAC, EMEA | P5+ | Internal Tool, Portal |
| 6 | Education / training | APAC, MENA, USA | P5+ | MVP, Portal, AI Workflow |
| 7 | Healthcare wellness (non régulé) | APAC, EMEA, USA | P4 conditionnel | Portal, Internal Tool |
| 8 | E-commerce / retail | APAC, MENA, EMEA, USA | P4+ | Commerce, Launch |
| 9 | Government-adjacent | APAC, MENA, EMEA | **P6+ conditionnel** | Portal, Audit |

## Anti-clients (refus systématique)

- ❌ Projets médicaux régulés (HIPAA, MDR, dispositifs médicaux)
- ❌ Banque/finance régulée nécessitant licence bancaire / monetary authority
- ❌ Crypto / DeFi / token launches (risque légal multi-juridictionnel)
- ❌ Gambling / casino / paris en ligne
- ❌ Surveillance de masse / militaire offensif
- ❌ Désinformation / fake content / deepfakes commerciaux
- ❌ Clients en conflit avec valeurs Architekt (à documenter cas par cas)

## Critères de qualification par typologie

Voir `docs/INTAKE.md` (Global Project Readiness Checklist) et `docs/skills-spec/architekt-commercial.spec.md` pour le process complet.
