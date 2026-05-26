# Configuration LLM

## Routage multi-modèles (v2.2.0+)

La plateforme **Architekt Factory** achemine automatiquement les agents vers le **bon modèle** selon leur rôle :

| Catégorie | Modèle lourd | Modèle léger | Tags agent |
|-----------|---------------|--------------|------------|
| Raisonnement | gpt-5.2 | gpt-5-mini | `reasoner`, `architect`, `strategist`, `planner` |
| Production / Code | gpt-5.1-codex | gpt-5-mini | `developer`, `tester`, `security`, `refactoring` |
| Tâches | gpt-5-mini | gpt-5-mini | Agents génériques |
| Rédaction | gpt-5.1-codex | gpt-5-mini | `doc_writer`, `tech_writer` |

Configurez en direct dans **Paramètres → LLM** (sans redémarrage).

## Thompson Sampling LLM (Darwin)

La même équipe (agent + pattern) **teste A/B automatiquement plusieurs modèles LLM** :

```
Beta(wins+1, losses+1) par (agent_id, pattern_id, technology, phase_type, llm_model)
```

- **Warmup** : exploration aléatoire pour les 5 premières exécutions par contexte
- **Après warmup** : Thompson Sampling choisit le modèle avec la meilleure distribution Beta
- Résultats dans l'onglet **Teams → LLM A/B**

## Fournisseurs (multi-fournisseur avec repli)

| Fournisseur | Modèles | Cas d'usage |
|-------------|---------|-------------|
| MiniMax | MiniMax-M2.5 | Par défaut (dev local) |
| Azure OpenAI | gpt-5-mini | Production légère |
| Azure AI Foundry | gpt-5.2, gpt-5.1-codex, gpt-5.1-mini | Production avancée |
| Demo | Mock | Tests (sans clé API) |

## Chaîne de repli

```
minimax → azure-openai → azure-ai
Cooldown : 90 s sur HTTP 429 (limite de débit)
```

## Variables d'environnement

```bash
PLATFORM_LLM_PROVIDER=minimax          # ou azure-openai, azure-ai, demo
PLATFORM_LLM_MODEL=MiniMax-M2.5       # ou gpt-5-mini
LLM_RATE_LIMIT_RPM=50                 # requêtes par minute

# Azure AI Foundry (pour gpt-5.2 / gpt-5.1-codex)
AZURE_AI_API_KEY=...
AZURE_DEPLOY=your-deployment-endpoint

# Azure OpenAI (pour gpt-5-mini)
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_ENDPOINT=...
```

## Clés API

Clés stockées dans `~/.config/factory/*.key` (chmod 600).  
⚠️ **NE JAMAIS** définir `*_API_KEY=dummy` — utilisez `PLATFORM_LLM_PROVIDER=demo` à la place.

## API de configuration du routage

```bash
# Matrice de routage actuelle
GET /api/llm/routing

# Mise à jour de la matrice (vide le cache 60 s immédiatement)
POST /api/llm/routing
Content-Type: application/json
{
  "routing": {
    "reasoning_heavy": {"provider": "azure-ai", "model": "gpt-5.2"},
    "reasoning_light": {"provider": "azure-openai", "model": "gpt-5-mini"},
    "production_heavy": {"provider": "azure-ai", "model": "gpt-5.1-codex"},
    "production_light": {"provider": "azure-openai", "model": "gpt-5-mini"}
  }
}
```

## APIs LLM A/B

```bash
# Classement fitness des modèles
GET /api/teams/llm-leaderboard?technology=generic&phase_type=generic

# Résultats récents des tests A/B
GET /api/teams/llm-ab-tests?limit=20
```

## Notes par fournisseur

| Fournisseur | Notes |
|-------------|-------|
| MiniMax | Les balises `<think>` consomment des tokens (contexte min 16K) |
| gpt-5-mini | PAS de paramètre `temperature` ; `max_completion_tokens` ≥ 8K |
| gpt-5.1-codex | Optimisé pour le code ; utiliser `max_completion_tokens` |
| Demo | Réponses mock, pas d'appels externes |

## Observabilité

Chaque appel LLM est tracé avec : fournisseur, modèle, tokens (entrée/sortie), coût, latence.  
Consultation : `/api/llm/stats`, `/api/llm/traces`, et **Monitoring → MCP Tool Calls** dans le dashboard.

[English](LLM-Configuration)
