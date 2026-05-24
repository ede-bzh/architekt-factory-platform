# Spec : architekt-commercial

> Skill cible : `skills/architekt-commercial.md`
> ADR référents : ADR-008

## Objectif

Encoder le **cycle de vente Architekt** pour que les agents (et fondateurs) gèrent l'avant-vente avec discipline et vitesse.

## Quand utiliser

- Réception d'un lead
- Qualification d'un prospect
- Rédaction d'un devis / SOW
- Suivi pipeline commercial
- Préparation négociation contrat

## Funnel cible (cf. GTM.md)

```
Lead → Qualifié → Devis envoyé → Signé (audit) → Signé (delivery) → Récurrent
```

Conversions cibles :
- Lead → Qualifié : 30 %
- Qualifié → Devis : 40 %
- Devis → Signé audit : 50 %
- Audit → Delivery : 50 %

## Qualification (BANT adapté Architekt)

| Critère | Question |
|---------|----------|
| **B**udget | Quel budget alloué ? (fourchette `docs/OFFERS.md`) |
| **A**uthority | Qui décide ? (sponsor exécutif identifié) |
| **N**eed | Quel problème business ? (mapper à 1 des 5 offres) |
| **T**iming | Quelle deadline ? (compatible avec capacité Architekt) |
| **F**it | Stack dans Tier A/B ? Conditions IP/AI compatibles ? Secteur ok ? |

→ Si 3/5 OK → qualifié. Si < 3 → décliner ou nurturer (3 mois).

## Process devis < 48h

1. **Discovery call** 45 min (notes structurées)
2. **Application intake checklist** (`docs/intake-checklist.md` à créer)
3. **Choix offre** dans catalogue (cf. `docs/OFFERS.md`)
4. **Estimation effort** (heures × coût horaire interne)
5. **Calcul prix** (effort × 1/marge_cible)
6. **Rédaction SOW** (template par offre)
7. **Envoi devis** (PDF + tracking ouverture si possible)
8. **Suivi à J+3 et J+7**

## Négociation : règles

- **Prix plancher** : marge minimale 40 % (jamais en dessous)
- **Remise max** : 20 % pour 1er client offre OU client référent
- **Pivot scope** : préférer réduire scope que baisser prix
- **Pas de bonus pénalité fixe** sans clause symétrique
- **Pas de gratuit "POC"** (sauf cas exceptionnel, validé CPO+CTO)

## Refus poli (cas)

- Hors scope catalogue
- Budget incompatible (proposer alternative ou décliner)
- Secteur régulé non outillé
- Conflit valeurs / éthique

→ Réponse standard : "Merci pour l'opportunité. À ce stade, [raison]. Voici un partenaire qui pourrait mieux vous accompagner : [referral]."

## Suivi pipeline

CRM (Notion / Airtable / Pipedrive) avec stages :
- Lead (source, date)
- Qualifié (BANT scoré)
- Devis envoyé (montant, deadline)
- Signé audit / delivery (montant final)
- En cours (mission ID plateforme)
- Livré (NPS, marge réelle, case study OK ?)
- Récurrent (TMA / Run actif)

Revue pipeline **hebdo** (15 min CPO+CTO).

## Métriques

- Leads qualifiés / mois
- Devis envoyés / mois
- Taux conversion par étape
- Cycle moyen lead → signé
- CAC (Coût Acquisition Client)
- Pipeline ouvert ($)
- Taux refus projet (signal qualité filtre)

## Anti-patterns

- ❌ Devis > 5 jours (perte momentum)
- ❌ Ne pas qualifier BANT (perte temps)
- ❌ Accepter "on verra le prix après"
- ❌ Pas de SOW signé avant kick-off
- ❌ Promesse verbale non tracée
- ❌ Pas de suivi à J+3 / J+7 (50 % deals perdus par silence)

## Sources

- BANT framework (IBM)
- Challenger Sale methodology
- Retours terrain agences APAC 2026
