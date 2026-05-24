# ADR-030 : Client type taxonomy

- **Statut** : Proposé
- **Date** : 2026-05-24
- **Décideurs** : CPO, GTM

## Contexte

Architekt cible plusieurs types de clients. Sans taxonomie, le ciblage commercial est flou et les offres mal alignées.

## Décision

**9 typologies clients** (cf. `docs/CLIENTS.md`) :

| ID | Typologie | Statut |
|----|-----------|--------|
| 1 | Scale-ups B2B | Prioritaire P4 |
| 2 | SMEs / mid-market | Prioritaire P4 |
| 3 | Professional services | Prioritaire P4 |
| 4 | Hospitality / luxury / tourism | P5+ |
| 5 | Industrial / logistics / manufacturing | P5+ |
| 6 | Education / training | P5+ |
| 7 | Healthcare-adjacent / wellness | Conditionnel (non-régulé OK) |
| 8 | E-commerce / retail | P4+ |
| 9 | Government-adjacent / public sector | P6+ (sécu mature) |

+ **Anti-clients** explicites : healthcare régulé, banque licenciée, crypto/DeFi, gambling, surveillance militaire, désinformation.

## Conséquences

### Positives
- Ciblage commercial clair
- Refus rapide hors cible (gain temps)
- Mapping offre × client (matrice OFFERS.md)

### Négatives
- Manquer certaines opportunités atypiques
- Mitigation : revue trimestrielle, override CPO possible

## Sources
- `docs/CLIENTS.md`
- Analyse marché APAC + MENA + EMEA + USA 2026
