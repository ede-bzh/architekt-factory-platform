# ADR-009 : Internal platform before SaaS

- **Statut** : Proposé
- **Date** : 2026-05-24
- **Décideurs** : CPO, CTO

## Contexte

99 % des "AI agencies" essayent de lancer un SaaS avant d'avoir des clients delivery. Résultat habituel : pas de revenue, fuite cash, abandon.

## Décision

**Studio premium d'abord. Plateforme interne ensuite. SaaS éventuellement.**

Phases gouvernées par triggers stricts :

| Phase | Trigger pour démarrer |
|-------|----------------------|
| Studio | Maintenant |
| IDP (Phase 5) | ≥ 3 clients livrés |
| Client portal (Phase 6) | ≥ 5 clients actifs |
| SaaS (Phase 7) | ≥ 10 clients + 3 offres répétables + marge > 50 % 6 mois |

Aucun travail multi-tenant / billing / RBAC fin / portail self-service avant les triggers.

## Conséquences

### Positives
- Pas de gaspillage capacité 2 personnes
- Risque commercial réduit (on valide avant d'investir)
- Plateforme = bras virtuel pour delivery réel (utilité immédiate)

### Négatives
- Pas de revenu MRR récurrent au début
- Mitigation : offre Architekt Run (TMA) post-livraison = MRR studio

## Alternative écartée

**Lancer un SaaS dès le rebrand** : rejeté (trop coûteux, pas validé, pas notre métier).

## Sources

- "Default alive" Paul Graham — runway first
- DORA 2025 : foundation first, then scale
