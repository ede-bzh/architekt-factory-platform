# Référence API

API REST de la **plateforme Architekt** (Architekt Factory). URL de base : `http://<hôte>:<port>` (local par défaut : `8099`, Docker : `8090`).

**Swagger UI :** `/docs` (OpenAPI auto-généré par FastAPI).

## Authentification

Selon **ADR-001** (rebrand plateforme), utilisez la variable d'environnement canonique de clé API :

| Variable | Statut | Notes |
|----------|--------|-------|
| `ARCHITEKT_API_KEY` | **Principale** | À définir en production et pour les nouvelles intégrations |
| `MACARON_API_KEY` | **Alias (6 mois)** | Acceptée jusqu'à fin de l'alias ; même valeur que `ARCHITEKT_API_KEY` |

Lorsque l'une des variables est définie, `AuthMiddleware` protège les mutations API. Si aucune n'est définie, l'authentification est désactivée (développement uniquement).

### Jeton Bearer

Envoyez la clé sur chaque requête protégée :

```http
Authorization: Bearer architekt_live_xxxxxxxxxxxxxxxx
```

Exemple avec `curl` :

```bash
export ARCHITEKT_API_KEY="architekt_live_xxxxxxxxxxxxxxxx"

curl -s -X POST "http://localhost:8099/api/missions" \
  -H "Authorization: Bearer ${ARCHITEKT_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"name":"Mon Epic","workflow_id":"product-lifecycle"}'
```

Les déploiements hérités peuvent encore exporter `MACARON_API_KEY` ; le middleware traite les deux noms comme équivalents pendant la fenêtre d'alias de 6 mois.

### Règles d'accès

| Type de requête | Auth requise |
|-----------------|--------------|
| `GET` sur les chemins publics listés (projets, missions, agents, métriques, santé, etc.) | Non |
| `POST`, `PATCH`, `DELETE` sur `/api/*` | Oui (Bearer) |
| Pages HTML, `/static`, `/docs`, flux SSE | Non (pages) ; le SSE suit les règles de l'endpoint de flux |
| Repli query `?token=<clé>` | Supporté pour les scripts (préférer l'en-tête `Authorization`) |

Les cookies de session JWT (`access_token`) sont utilisés par l'interface web ; l'automatisation API doit utiliser la clé API Bearer.

## Format des requêtes

Les endpoints acceptent **JSON + form-data** via `_parse_body` (détection automatique). Préférez `Content-Type: application/json` pour les intégrations.

## Projets

| Méthode | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/projects` | Créer un projet |
| GET | `/api/projects` | Lister les projets |

## Missions

| Méthode | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/missions` | Créer une mission (épopée) |
| POST | `/api/missions/{id}/start` | Démarrer l'exécution de la mission |
| POST | `/api/missions/{id}/run` | Exécuter la phase courante |
| POST | `/api/missions/{id}/wsjf` | Définir les scores WSJF |
| POST | `/api/missions/{id}/sprints` | Créer un sprint |
| POST | `/api/missions/{id}/validate` | Valider une phase (checkpoint HITL) |
| GET | `/api/missions/{id}` | Détails de la mission |

## Epics / Features / Stories

| Méthode | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/epics/{id}/features` | Créer une feature sous l'epic |
| POST | `/api/features/{id}/stories` | Créer une story sous la feature |
| POST | `/api/features/{id}/deps` | Ajouter une dépendance |
| PATCH | `/api/features/{id}` | Mettre à jour une feature |
| PATCH | `/api/stories/{id}` | Mettre à jour une story |
| PATCH | `/api/tasks/{id}/status` | Mettre à jour le statut d'une tâche |
| PATCH | `/api/backlog/reorder` | Réordonner le backlog |
| DELETE | `/api/features/{id}/deps/{dep}` | Supprimer une dépendance |
| DELETE | `/api/sprints/{id}/stories/{id}` | Retirer une story du sprint |
| GET | `/api/sprints/{id}/available-stories` | Lister les stories non assignées |
| GET | `/api/features/{id}/deps` | Obtenir les dépendances |

## Métriques et monitoring

| Méthode | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/metrics/cycle-time` | Métriques de cycle time |
| GET | `/api/releases/{project_id}` | Historique des releases |
| GET | `/api/llm/stats` | Statistiques d'usage LLM |
| GET | `/api/llm/traces` | Traces d'appels LLM |
| GET | `/api/monitoring/live` | Monitoring live (SSE) |

## Système

| Méthode | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/health` | Contrôle de santé |
| GET | `/api/agents` | Lister les agents |
| GET | `/api/sessions` | Lister les sessions |
| GET | `/api/mcps` | Lister les serveurs MCP |
| GET | `/api/docs` | Swagger UI |

## Flux SSE

| Endpoint | Description |
|----------|-------------|
| `/api/missions/{id}/stream` | Événements d'exécution de mission |
| `/api/monitoring/live` | Événements de monitoring système |

Les clients SSE n'envoient pas la clé API sur la connexion EventSource ; les mutations de contrôle de mission exigent toujours l'auth Bearer.

## CLI (`sf`)

Le CLI `sf` utilise le même jeton Bearer (depuis `ARCHITEKT_API_KEY` ou l'alias `MACARON_API_KEY`) :

```bash
export ARCHITEKT_API_KEY="architekt_live_xxxxxxxxxxxxxxxx"
sf status
sf missions list
```

## Documentation associée

- [Sécurité](Security) — en-têtes, limites de débit, garde-fous adversariaux
- [Guide de déploiement](Deployment-Guide) — URLs d'environnement et clés
- [Patterns](Patterns) — orchestration utilisée par les phases de mission

[English](API-Reference)
