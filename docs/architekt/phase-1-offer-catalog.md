# Phase 1 — Offer & Stack Catalogue

> Durée cible : **1 semaine**
> Dépend de : Phase 0 (rebrand mergé, legal pack OK)
> Sortie : **ce qu'on vend** + **avec quelles technos**

## Objectif

Définir formellement :

1. Les **5 offres packagées** d'Architekt (cf. `docs/OFFERS.md`)
2. Le **catalogue technos tierisé A/B/C** (cf. `docs/CATALOG.md`)
3. Les **ADR additionnels** business (008-012)

## Livrables

### A. Offres packagées (cf. `docs/OFFERS.md`)

Pour chaque offre (5) :

- [ ] **One-pager** prospect (1 page Markdown + PDF export)
- [ ] **SOW template** prêt à remplir (`docs/legal/sow-<offre>-template.md`)
- [ ] **FinOps** : budget LLM + heures + infra + marge cible documentés
- [ ] **Critères accept/refuse** intake checklist
- [ ] **Stack par défaut** (Tier A)

### B. Catalogue technos tierisé (cf. `docs/CATALOG.md`)

- [ ] **Tier A** (7 stacks max) — vérifier que chaque ligne a un agent référent et un statut clair
- [ ] **Tier B** (6 stacks) — documenter les conditions d'activation
- [ ] **Tier C** (7 stacks) — documenter premium pricing et délais
- [ ] **Hors scope** (10 stacks) — refus poli scripté

### C. ADR additionnels (5 nouveaux)

| ID | Sujet |
|----|-------|
| 008 | Offers before stacks |
| 009 | Internal platform before SaaS |
| 010 | Human approval policy for agents |
| 011 | LLM cost governance (FinOps) |
| 012 | SBOM and supply-chain baseline |

Détails dans `docs/adr/008..012`.

### D. Squelettes catalog stacks

Pour chaque stack ⚠️ Tier B et C, créer `docs/catalog/<stack>.md` vide (rempli quand activé) :

```
docs/catalog/
  astro.md
  nextjs.md
  fastapi.md
  postgresql.md
  shadcn.md
  cloudflare-pages.md
  github-actions.md
  wordpress.md
  shopify.md
  nuxt.md
  payload.md
  nestjs.md
  spring-modulith.md
  swiftui.md
  android-compose.md
  azure.md
  aws.md
```

## Pré-requis Phase 1

- Phase 0 mergée
- Licence tranchée (ADR-006)
- Brand system minimal disponible

## Plan en 5 jours

| Jour | Action |
|------|--------|
| J1 | 5 one-pagers offres (1 par jour-mi) + intake checklist |
| J2 | SOW templates (5) + FinOps par offre |
| J3 | Catalogue tierisé revue + finalisation (17 lignes A/B/C) |
| J4 | 5 ADR additionnels (008-012) écrits |
| J5 | Squelettes `docs/catalog/*.md` + PR merge |

## Gate de passage

- [ ] 5 offres packagées (one-pager + SOW + FinOps)
- [ ] Catalogue technos tierisé (mergé)
- [ ] 17 squelettes `docs/catalog/*.md` créés
- [ ] Critères accept/refuse projet écrits
- [ ] 5 ADR additionnels (008-012) mergés
- [ ] Milestone Phase 1 fermé sur GitHub

## Risques

| Risque | Mitigation |
|--------|-----------|
| Sur-spécifier les SOW (rigidité) | Garder ≤ 2 pages, sections "à compléter par projet" |
| Pricing trop bas | Cross-check vs concurrents SG (Applify, Kryst, SleekDigital) |
| Catalogue trop ambitieux | Tier A limité à 7 stacks (R5) |
