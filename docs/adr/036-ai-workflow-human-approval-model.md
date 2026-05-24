# ADR-036 : AI workflow human approval model

- **Statut** : Proposé
- **Date** : 2026-05-24
- **Décideurs** : CTO, CAIO, CISO

## Contexte

Les workflows IA Architekt peuvent prendre des actions irréversibles (envoi email client, modification DB prod, achat, communication externe). Sans modèle clair, risque légal + sécurité + reputation.

## Décision

**Modèle Human-In-The-Loop (HITL) standard** pour les AI workflows livrés aux clients (extension de ADR-010 pour la plateforme Architekt elle-même).

### Classification d'actions IA (par workflow client)

| Classe | Action exemple | Approbation humaine |
|--------|---------------|---------------------|
| A0 | Classification, scoring, suggestion read-only | Aucune |
| A1 | Draft contenu, brouillon proposition | Aucune (mais visible) |
| A2 | Envoi notification interne, log enrichi | Aucune (logging) |
| A3 | Action externe traçable (ticket Jira, email équipe) | Validation rôle métier |
| A4 | **Action externe client** (email client, post LinkedIn, transaction) | **Validation explicite humain** |
| A5 | **Action irréversible critique** (paiement, contrat signé, suppression données) | **Double validation + audit log** |

### Implémentation standard

```
[AI workflow] → action proposée
    │
    ▼
[Classification classe A0-A5]
    │
    ├── A0-A2 → exécution + log
    │
    └── A3-A5 → pause + notification humain
        │
        ▼
[Décision humain]
    │
    ├── Approve → exécution + audit log (qui, quand, motif)
    ├── Reject → annulation + audit log
    └── Timeout 24h → annulation auto (ou config selon use case)
```

### Composants techniques requis

- Queue persistante (RQ, BullMQ)
- DB états d'actions (en attente / approuvée / rejetée / expirée)
- UI notification (email, dashboard plateforme, Slack/Teams)
- Audit log append-only (cf. ADR-019)

### Règles

- **Jamais d'action A4-A5 autonome** sans approval
- **Audit log obligatoire** pour A3-A5
- **Coût LLM tracé** par action (cf. ADR-011)
- **Transparence client** : utilisateur final informé que l'action IA est en attente d'approbation

## Conséquences

### Positives
- Sécurité client (pas d'IA "qui part en vrille")
- Conformité EU AI Act (Article 14 — human oversight)
- Argument vente B2B ("on contrôle l'IA")

### Négatives
- Ralentit certains workflows (acceptable, c'est le point)
- Process oubli notification → timeout
- Mitigation : escalade à 2e personne après 12h

## Sources
- ADR-010 (Human approval policy for agents — plateforme Architekt interne)
- ADR-019 (Agent audit logs and reproducibility)
- EU AI Act Article 14 (Human oversight)
- NIST AI RMF Manage 2.1 (Human-AI configuration)
- OWASP LLM Top 10 — LLM02 Insecure Output Handling
