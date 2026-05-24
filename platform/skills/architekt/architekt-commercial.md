---
name: Architekt Commercial
description: Cycle vente Architekt — BANT, devis <48h, négociation, pipeline (ADR-008)
tags: [commercial, architekt, sales, bant, sow]
metadata:
  category: commercial
  triggers: [lead, quote, sow, pipeline, prospect, devis]
---

# Architekt Commercial

## Objectif

Encoder le **cycle de vente Architekt** pour gérer l'avant-vente avec discipline et vitesse.

## Quand utiliser

- Réception lead / qualification prospect
- Rédaction devis / SOW
- Suivi pipeline / négociation contrat

## Funnel cible

```
Lead → Qualifié → Devis envoyé → Signé (audit) → Signé (delivery) → Récurrent
```

Conversions cibles : Lead→Qualifié 30% | Qualifié→Devis 40% | Devis→Signé audit 50% | Audit→Delivery 50%

## Qualification BANT adapté Architekt

| Critère | Question |
|---------|----------|
| **B**udget | Fourchette `docs/OFFERS.md` ? |
| **A**uthority | Sponsor exécutif identifié ? |
| **N**eed | Problème mappable à 1 offre catalogue ? |
| **T**iming | Deadline compatible capacité Architekt ? |
| **F**it | Stack Tier A/B ? IP/AI OK ? Secteur OK ? |

→ **3/5 OK = qualifié**. < 3 → décliner ou nurturer 3 mois.

## Process devis < 48h

1. Discovery call 45 min (notes structurées)
2. Intake checklist
3. Choix offre catalogue
4. Estimation effort (heures × coût interne)
5. Prix = effort × 1/marge_cible
6. Rédaction SOW (template offre)
7. Envoi devis PDF
8. Suivi J+3 et J+7

## Négociation

- **Prix plancher** : marge min 40%
- **Remise max** : 20% (1er client offre OU référent)
- **Pivot scope** > baisser prix
- Pas de POC gratuit (sauf exception CPO+CTO)
- Pas de bonus/pénalité asymétrique

## Refus poli

Hors catalogue, budget incompatible, secteur régulé non outillé, conflit éthique → réponse standard + referral partenaire.

## Pipeline CRM

Stages : Lead → Qualifié → Devis → Signé → En cours → Livré → Récurrent.
Revue pipeline **hebdo** 15 min CPO+CTO.

## Métriques

Leads qualifiés/mois, devis/mois, taux conversion, cycle lead→signé, CAC, pipeline ouvert, taux refus.

## Anti-patterns

- ❌ Devis > 5 jours
- ❌ Pas de qualification BANT
- ❌ "On verra le prix après"
- ❌ Kick-off sans SOW signé
- ❌ Pas de suivi J+3 / J+7

## Sources

- ADR-008 Offers before stacks
- BANT framework, Challenger Sale
