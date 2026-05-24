# Spec : architekt-ai-governance

> Skill cible : `skills/architekt-ai-governance.md`
> ADR référents : ADR-010, ADR-019, ADR-013

## Objectif

Encoder les **règles de gouvernance des agents IA** : approvals humains, audit trail, transparence client.

## Quand utiliser

- À chaque action agent de classe L3 ou L4 (cf. ADR-010)
- Lors d'incident sécurité / litige client
- En audit (interne ou externe)
- Lors de prompts contenant données sensibles client

## Classes d'actions (rappel ADR-010)

| Classe | Approbation |
|--------|-------------|
| L0 Read-only | Aucune |
| L1 Write sandbox | Aucune (CI valide) |
| L2 Write prod | Lead dev |
| L3 Critical | **CTO ou CPO** |
| L4 Irreversible | **CTO + CPO (double)** |

## Audit log obligatoire (rappel ADR-019)

Chaque action agent journalisée :
- agent_id + version skill + version LLM model
- timestamp
- prompt hash + context size
- output hash + tokens + coût SGD
- human approval si requis
- downstream actions

Tamper-evident (hash chain), append-only, rétention 90 j actif + 1 an archive.

## Données sensibles client

- **Jamais** envoyer données client à LLM provider sans DPA signé
- **Jamais** utiliser données client pour fine-tuning Architekt
- Logs anonymisés (`presidio` ou regex maison)
- Data residency : Azure OpenAI SG/EU ou Anthropic enterprise

## Transparence client

- **Toujours divulguer** que le code est généré par IA
- Liste modèles utilisés disponible sur demande
- Audit log exportable par mission
- Opt-out IA sur certains modules possible (chiffré, surcoût négocié)

## Workflow approval (Phase 5 plateforme)

```
Action L3/L4 demandée
  → Plateforme met en pause
  → Notification (email + UI)
  → Décideur approuve/refuse (UI plateforme)
  → Décision tracée (audit log)
  → Action exécutée ou annulée
  → Timeout 24 h → annulation auto
```

## Bonnes pratiques agent

- Toujours documenter le **motif** d'une action critique
- Préférer plusieurs petites actions L2 qu'une seule L3
- Demander confirmation explicite avant L4
- Si doute → escalader (jamais "deviner")
- Ne jamais désactiver l'audit log

## Anti-patterns

- ❌ Bypasser approval "parce que c'est rapide"
- ❌ Désactiver logging "pour debug"
- ❌ Envoyer prompt avec données client à provider sans DPA
- ❌ Utiliser données client pour entraîner skills futurs
- ❌ Ne pas divulguer usage IA dans livrables

## Sources

- ADR-010 (Human approval policy)
- ADR-019 (Agent audit logs)
- ADR-013 (Client IP and AI-generated code policy)
- EU AI Act
- NIST AI RMF 1.0
- ISO/IEC 42001 (AI Management System)
- Singapore Model AI Governance Framework 2.0
