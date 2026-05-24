---
name: Architekt Delivery
description: Méthode delivery Architekt — phases, DoD, scope rules, kill criteria (ADR-008)
tags: [delivery, architekt, phases, scope, dod]
metadata:
  category: delivery
  triggers: [mission, phase, handover, scope, discovery, hardening]
---

# Architekt Delivery

## Objectif

Encoder la **méthode delivery Architekt** : phases, gates, règles de scope — pour que toute mission client respecte le cadre contractuel.

## Quand utiliser

- Création nouvelle mission client
- Passage de phase (discovery → build → hardening → handover)
- Demande client out-of-scope
- Revue mi-mission / escalade budget

## Structure mission

```
1. Intake (1-3 j)
2. Signature contractuelle
3. Discovery (3-5 j)
4. Build (2-6 semaines selon offre)
5. Hardening (1-2 semaines)
6. Handover (1-2 j)
7. Closure (2 semaines post-livraison)
```

## Definition of Done par phase

| Phase | DoD |
|-------|-----|
| Discovery | ADR projet, roadmap validée client, équipe assignée, manifest mission |
| Build | CI verte, tests OK, démo intermédiaire validée, mutation modules critiques |
| Hardening | Pentest interne OK, SBOM, Lighthouse ≥ 90, doc utilisateur, runbook |
| Handover | Repo transféré, formation faite, 30 j hotfix, accès Architekt retirés |
| Closure | Paiement final, NPS, retro écrite, case study OK |

## Règles scope (anti-creep)

1. **Out-of-scope = avenant** chiffré et signé
2. Pas de "petite faveur" non tracée (chaque modif = ticket)
3. Sprint planning **hebdo** (pas quotidien)
4. **1 PO/sponsor client** identifié
5. Pivot > 20% scope → re-cadrage formel (SOW v2)

## Limites customisation

| Type | Limite |
|------|--------|
| Custom CSS/composants shadcn | OK |
| Stack hors Tier A/B | Refus ou Tier C premium |
| Intégration > 2 systèmes tiers | Avenant ou refus |
| Secteur régulé (banque, santé) | Refus jusqu'à équipe outillée |

Dépassement projeté > 10% → escalade CPO+CTO.

## Critères kill / no-go

- Sponsor absent > 2 semaines
- Paiement intermédiaire impayé > 30 j
- Scope creep > 50% sans avenant
- Demande incompatible éthique/sécu/loi
- Marge prévisionnelle < 30% non corrigeable

## Anti-patterns

- ❌ Build sans Discovery validée
- ❌ Livrer sans Hardening
- ❌ "Juste un petit fix" non tracé
- ❌ Pas de retro post-mission
- ❌ Sprints quotidiens (inefficace pour petite équipe)

## Sources

- ADR-008 Offers before stacks
- `docs/architekt/phase-4-first-clients.md`
- `docs/OFFERS.md`
