# ADR-016 : Pricing model and margin targets

- **Statut** : Proposé
- **Date** : 2026-05-24
- **Décideurs** : CPO, CTO

## Contexte

Sans cadre pricing, on tombe dans le piège du devis sur-mesure permanent → marges incertaines, négociation lente, projets à perte.

## Décision

### Pricing modèle : forfait par offre

- **Pas de Time & Materials** (sauf retainer Run)
- Forfait basé sur scope défini (SOW)
- Si scope dérive → avenant facturé

### Modalités

- 30 % à la signature
- 40 % à mi-mission (jalon démo intermédiaire)
- 30 % à la livraison (handover validé)
- Audit : 100 % à la signature
- Run / TMA : abonnement mensuel d'avance

### Currency

- **SGD** par défaut
- USD accepté hors SG
- EUR possible (Europe)

### Marges cibles

| Offre | Marge brute minimale |
|-------|---------------------|
| Architekt Audit | **70 %** |
| Architekt Launch | **60 %** |
| Architekt Internal Tool | **55 %** |
| Architekt AI Workflow | **55 %** |
| Architekt MVP | **50 %** |

### Calcul marge brute

```
Marge brute = (Revenue - Direct costs) / Revenue
Direct costs = LLM tokens + Infra dédiée + Heures imputées * coût horaire interne
```

- **Coût horaire interne** : 100 SGD/h (fondateurs), à ajuster avec embauches
- Infra inclut hosting client 3 premiers mois (puis facturé en sus)

### Seuils d'alerte

- Marge prévisionnelle < 40 % en cours de mission → **revue CPO+CTO immédiate**
- Marge réelle < 40 % à la livraison → **retro obligatoire** + ajustement pricing offre
- Marge < 30 % deux projets consécutifs sur la même offre → **freeze offre** jusqu'à correctif

### Conditions de remise

- Premier client d'une nouvelle offre : 20 % remise (en échange case study)
- ONG / pro bono : 1 projet / an gratuit (à choisir CPO+CTO)
- Refus systématique : "1 client réfère 1 nouveau = 5 % remise client suivant"

## Pricing public ?

- **NON** sur site jusqu'à 5 clients (négocier au cas par cas, apprendre)
- **OUI fourchettes indicatives** sur site post-5 clients
- **OUI prix précis** seulement pour offre Audit (3-10k SGD)

## Conséquences

### Positives
- Marge prévisible et défendable
- Process de vente accéléré (pricing connu)
- Apprentissage continu (data marges)

### Négatives
- Risque perdre un deal sur prix
- Mitigation : marge à 40 % acceptable si stratégique (logo majeur, secteur prioritaire)

## Sources

- Pricing 2026 agences digitales SG (benchmarks Applify, Kryst, SleekDigital)
- Salaire moyen dev senior SG : 80-120k SGD/an → coût horaire ~80 SGD chargé
