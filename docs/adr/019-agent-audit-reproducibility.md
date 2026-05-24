# ADR-019 : Agent audit logs and reproducibility

- **Statut** : Proposé
- **Date** : 2026-05-24
- **Décideurs** : CTO, CAIO, CISO

## Contexte

Les agents IA prennent des décisions opaques. En cas d'incident, de litige client ou d'audit, il faut pouvoir reproduire **qui** a décidé **quoi**, **quand**, **avec quel contexte**.

## Décision

**Toute action agent est journalisée de façon auditable et théoriquement reproductible.**

### Données journalisées (par action agent)

```json
{
  "action_id": "uuid",
  "mission_id": "uuid",
  "agent_id": "string",
  "agent_version": "string (skill version)",
  "timestamp": "ISO 8601 UTC",
  "llm": {
    "provider": "anthropic | openai | minimax | ...",
    "model": "claude-sonnet-4 | gpt-5-mini | ...",
    "model_version": "string"
  },
  "input": {
    "prompt_hash": "sha256",
    "tools_called_before": [...],
    "context_size_tokens": int
  },
  "output": {
    "content_hash": "sha256",
    "tool_calls": [...],
    "tokens_used": int,
    "cost_sgd": float
  },
  "human_approval": {
    "required": bool,
    "approved_by": "user_id | null",
    "approved_at": "timestamp | null"
  },
  "downstream_actions": ["action_id", ...]
}
```

### Stockage

- Table `agent_audit_log` (append-only)
- Rétention : 90 jours actif + 1 an archive (cf. ADR-018)
- Tamper-evident : hash chain (chaque entry inclut hash entry précédente)
- Export : JSON par mission à la demande

### Reproductibilité (théorique)

Pour rejouer une mission :

1. Récupérer `mission_id`
2. Lister actions ordonnées (`agent_audit_log`)
3. Pour chaque action :
   - Charger version exacte du skill (`platform/skills/definitions/<agent>.yaml@version`)
   - Charger modèle LLM exact (provider + version)
   - Reconstruire prompt depuis hash + context store
   - Appeler LLM (résultat peut différer = nature non-déterministe LLM)
4. Comparer outputs (delta acceptable < seuil similarité)

**Limites** : déterminisme LLM imparfait (temperature > 0, fine-tunes provider, changements modèle silencieux). Reproductibilité = **traçabilité parfaite** + **rejeu best-effort**.

### Cas d'usage

| Cas | Utilisation audit log |
|-----|----------------------|
| Litige client | Démontrer la décision et la validation humaine |
| Investigation incident | Tracer la cause racine d'une régression |
| Audit sécurité | Vérifier qu'aucune action L3/L4 sans approbation |
| Audit conformité (PDPA, RGPD) | Démontrer la gouvernance |
| Amélioration skills | Analyser patterns de rejet adversarial |

### Accès

- **Lecture** : CTO + CPO + CISO (toujours)
- **Lecture client** : limité à son `client_id` (Phase 6 portail)
- **Modification** : impossible (append-only, hash chain)

## Conséquences

### Positives
- Confiance et conformité
- Argument vente B2B (clients régulés)
- Capacité forensic

### Négatives
- Volume de logs (mitigation : compression, archive S3)
- Coût storage (faible vs valeur)

## Sources

- EU AI Act Article 13 (transparence, audit trail)
- NIST AI RMF (Manage 4.1 — Documentation)
- ISO/IEC 42001 (AI Management System) 2026
