# ADR-010 : Human approval policy for agents

- **Statut** : Proposé
- **Date** : 2026-05-24
- **Décideurs** : CTO, CISO, CAIO

## Contexte

Les agents IA peuvent prendre des actions destructrices ou coûteuses (deploy prod, écriture DB client, achat infra, accès données sensibles). Sans gate humaine, risque légal + sécurité + financier.

## Décision

**Toute action de classe critique nécessite approbation humaine explicite** (Human-In-The-Loop, HITL).

### Classes d'actions

| Classe | Définition | Approbation requise |
|--------|-----------|---------------------|
| L0 — Read-only | Lecture code, search, queries SELECT | Aucune (logging suffit) |
| L1 — Write sandbox | Écriture fichiers workspace, commits feature branch | Aucune (CI valide) |
| L2 — Write prod | Merge `main`, deploy staging, modif secrets non-prod | Validation lead dev |
| L3 — Critical | Deploy prod, modif DB prod, accès données client | **Validation CTO ou CPO** |
| L4 — Irreversible | Suppression DB, achat infra > X SGD, communication externe client | **Double validation CTO + CPO** |

### Mise en œuvre

- Workflow plateforme insère gate `human-in-the-loop` pour L3/L4
- Action mise en pause, notification (email + plateforme)
- Décision tracée (qui, quand, motif) dans audit log
- Timeout 24h → cancel auto (sauf override)

## Conséquences

### Positives
- Sécurité réelle (pas du théâtre)
- Conformité PDPA / RGPD facilitée (accès données = humain)
- Confiance client (transparence)

### Négatives
- Ralentit certains workflows (acceptable pour L3/L4)
- Risque oubli notification → timeout
- Mitigation : escalade à 2e personne après 12h

## Sources

- NIST AI RMF 1.0 (Risk Management Framework)
- EU AI Act (high-risk systems → human oversight)
- DORA 2025 : "AI in critical path needs control systems"
