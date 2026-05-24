---
name: Architekt AI Governance
description: Gouvernance agents IA — approvals L3/L4, audit trail, transparence client (ADR-010, ADR-019, ADR-013)
tags: [governance, architekt, ai, audit, approval]
metadata:
  category: governance
  triggers: [approval, audit-log, L3, L4, ai-governance, sensitive-data]
---

# Architekt AI Governance

## Objectif

Encoder les **règles de gouvernance des agents IA** : approvals humains, audit trail, transparence client.

## Quand utiliser

- Action agent classe L3 ou L4 (ADR-010)
- Incident sécurité / litige client
- Audit interne ou externe
- Prompts contenant données sensibles client

## Classes d'actions (ADR-010)

| Classe | Approbation |
|--------|-------------|
| L0 Read-only | Aucune |
| L1 Write sandbox | Aucune (CI valide) |
| L2 Write prod | Lead dev |
| L3 Critical | **CTO ou CPO** |
| L4 Irreversible | **CTO + CPO (double)** |

Exemples L3/L4 : deploy prod, rotation secrets, suppression data, facturation, infra critique.

## Audit log obligatoire (ADR-019)

Chaque action journalisée :
- agent_id + version skill + version LLM
- timestamp, prompt hash, context size
- output hash, tokens, coût SGD
- human approval si requis, downstream actions

Tamper-evident (hash chain), append-only, rétention 90 j actif + 1 an archive.

## Données sensibles client

- **Jamais** envoyer data client à LLM sans DPA signé
- **Jamais** fine-tuning Architekt sur data client
- Logs anonymisés (`presidio` ou regex)
- Data residency : Azure OpenAI SG/EU ou Anthropic enterprise

## Transparence client (ADR-013)

- Divulguer que le code est généré par IA
- Liste modèles disponible sur demande
- Audit log exportable par mission
- Opt-out IA possible (surcoût négocié)

## Workflow approval (Phase 5)

```
L3/L4 demandée → pause → notification → approbation UI
→ décision tracée → exécution ou annulation → timeout 24h = annulation
```

## Bonnes pratiques agent

- Documenter le **motif** d'une action critique
- Préférer plusieurs L2 qu'une seule L3
- Confirmation explicite avant L4
- Si doute → escalader (jamais deviner)
- Ne jamais désactiver l'audit log

## Anti-patterns

- ❌ Bypass approval "parce que c'est rapide"
- ❌ Désactiver logging pour debug
- ❌ Prompt client vers provider sans DPA
- ❌ Data client pour entraîner skills futurs
- ❌ Ne pas divulguer usage IA dans livrables

## Sources

- ADR-010 Human approval policy
- ADR-019 Agent audit logs
- ADR-013 Client IP and AI-generated code
- EU AI Act, NIST AI RMF, ISO/IEC 42001
