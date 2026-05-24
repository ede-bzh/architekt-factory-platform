# ADR-008 : Offers before stacks

- **Statut** : Proposé
- **Date** : 2026-05-24
- **Décideurs** : CPO, CTO, PMM

## Contexte

Les agences techniques tombent souvent dans le piège : *"on supporte 18 stacks"*. Les clients n'achètent pas une stack — ils achètent un livrable.

## Décision

**Architekt vend 5 offres packagées** (cf. `docs/OFFERS.md`) avant de proposer des stacks :

1. Architekt Launch (site)
2. Architekt MVP (app web)
3. Architekt Internal Tool (outil métier)
4. Architekt AI Workflow (automatisation)
5. Architekt Audit (rapport CTO)

Chaque offre a un prix, une durée, un livrable, un SOW template.

Le **catalogue technos** (tier A/B/C) n'est que **l'implémentation** des offres.

## Conséquences

### Positives
- Cycle de vente plus court (prospect comprend en 30 sec)
- Pricing comparable et défendable
- Marge prévisible par offre
- Pas de dispersion technique

### Négatives
- Risque de refuser un projet "non standard"
- Mitigation : offre custom existe mais demande sign-off CPO

## Sources

- Marketing 2026 : "outcome selling > feature selling"
- Retour terrain agences APAC (Applify, Kryst, OrfeoAI) : toutes vendent par outcome
