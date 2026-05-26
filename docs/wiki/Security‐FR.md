# Sécurité

Modèle de sécurité de la **plateforme Architekt** (Architekt Factory) : authentification API, durcissement HTTP, garde-fous adversariaux de qualité et isolation des conteneurs.

## Authentification

### Clé API (ADR-001)

| Variable | Rôle |
|----------|------|
| `ARCHITEKT_API_KEY` | **Requis (production)** — à définir sur tous les hôtes déployés et dans les secrets CI |

`AuthMiddleware` (`platform/security.py`) valide les jetons Bearer par comparaison SHA-256. Les mutations (`POST`, `PATCH`, `DELETE` sur `/api/*`) exigent une clé valide lorsque `ARCHITEKT_API_KEY` est définie.

```http
Authorization: Bearer <votre-clé-api>
```

**Règles :**

- Les endpoints publics en `GET` (projets, liste des missions, agents, métriques, santé) restent lisibles sans clé
- L'interface HTML peut utiliser des cookies JWT ; l'automatisation doit utiliser Bearer + `ARCHITEKT_API_KEY`
- Si aucune clé n'est configurée et `ENVIRONMENT=dev`, l'authentification est désactivée (ne jamais utiliser en production)
- Les stacks de production Azure peuvent ajouter une **authentification HTTP basique nginx** devant l'application

### Authentification de session (interface web)

`platform/auth/middleware.py` prend en charge le JWT via le cookie `access_token` ou un JWT Bearer long. Les clés API sont associées à un utilisateur équivalent administrateur pour les accès scriptés.

## Human-in-the-loop (porte de déploiement HITL)

Le déploiement en production n'est pas entièrement autonome. Le pattern **`human-in-the-loop`** suspend le workflow jusqu'à l'approbation humaine d'un point de contrôle.

Portes typiques (voir le workflow `product-lifecycle`) :

| Phase | Pattern | Porte | Décision humaine |
|-------|---------|-------|------------------|
| Comité stratégique | `human-in-the-loop` | `all_approved` | GO / NOGO / PIVOT |
| Déploiement production | `human-in-the-loop` | `all_approved` | Valider canary → 100 % après revue des métriques |
| Migration de données | `human-in-the-loop` | checkpoint | GO/NOGO avant bascule |
| Déploiement canary | `human-in-the-loop` | checkpoint | Promouvoir ou rollback |

La phase de déploiement (`deploy-prod`) exécute les agents DevOps/SRE pour le canary (1 %), puis bloque sur **`POST /api/missions/{id}/validate`** jusqu'à ce qu'un chef de projet confirme la promotion complète. Il s'agit de la **porte de déploiement HITL** — les agents préparent les preuves ; les humains conservent le veto sur le trafic de production.

Workflows associés : `canary-deployment`, `data-migration`, `ao-compliance`.

## Validation adversariale (L0 / L1 / L2)

Inspirée de *Team of Rivals* (arXiv:2601.14351). **Les auteurs de code ne peuvent pas déclarer eux-mêmes leur succès** — les critiques s'exécutent sur des créneaux modèle/fournisseur séparés lorsque c'est configuré.

### L0 — Déterministe (veto absolu)

Coût LLM nul ; s'exécute sur chaque sortie d'agent dans les patterns d'exécution :

- Raccourcis interdits : `test.skip`, `@ts-ignore`, `#[ignore]`, `catch` vide
- SLOP : lorem ipsum, `TBD`, `XXX`, texte placeholder
- MOCK : `NotImplementedError`, faux scripts de build, `BUILD SUCCESS` codé en dur
- Hallucination : allégations de modification de fichiers sans preuve d'appel d'outil correspondante
- Inadéquation de stack : mauvais langage pour la plateforme cible

**Résultat :** **VETO** absolu — la phase ne peut pas passer en cas d'échec dur.

### L1 — Sémantique LLM (veto absolu)

Un LLM distinct révise le slop, les erreurs de logique et le raisonnement halluciné. Ignoré pour les patterns de **discussion** (`network`, `debate`, `aggregator`, `human-in-the-loop`) afin de ne pas bloquer l'idéation.

**Résultat :** **VETO** absolu en cas de rejet.

### L2 — Architecture (veto + escalade)

`arch-critic` / critiques sécurité évaluent RBAC, frontières de validation, conception d'API et adéquation au modèle de menace.

**Résultat :** **VETO** avec escalade optionnelle vers un comité humain.

### Patterns d'orchestration

| Pattern | Rôle |
|---------|------|
| `adversarial-pair` | Boucle rédacteur ↔ relecteur (max 5 itérations) |
| `adversarial-cascade` | Défense en couches : code → L1 code → L1 sécurité → L2 archi |
| `sf-tdd` | Brain → worker TDD → critiques → DevOps |

Nouvelles tentatives : configuration du pattern jusqu'à **5 essais** ; le garde-fou peut accepter en souple les avertissements vs rejet dur (score ≥ 7).

## Limitation de débit

Deux couches :

### API HTTP (`RateLimitMiddleware`)

- Par défaut : **60 requêtes / 60 secondes** par clé client
- Clé client = **IP + préfixe du jeton Bearer** (haché)
- La table PostgreSQL `rate_limit_hits` persiste les compteurs entre redémarrages de conteneur lorsque `DATABASE_URL` pointe vers PG
- Réponse : `429 Rate limit exceeded`

### Fournisseur LLM (`llm/client.py`)

- `LLM_RATE_LIMIT_RPM` (par défaut **15** RPM) avec budget de jetons par fenêtre
- Cooldown **90 s** sur HTTP 429 des fournisseurs
- L'orchestrateur de mission réessaie les phases jusqu'à `MAX_LLM_RETRIES` en cas de limitation

Configurer des limites plus strictes au reverse proxy (nginx) pour les démos publiques.

## En-têtes de sécurité HTTP

Définis dans `platform/server.py` pour chaque réponse :

| En-tête | Valeur |
|---------|--------|
| `Strict-Transport-Security` | `max-age=31536000` (HTTPS uniquement) |
| `X-Frame-Options` | `DENY` (sauf routes d'aperçu workspace) |
| `X-Content-Type-Options` | `nosniff` |
| `X-XSS-Protection` | `1; mode=block` |
| `Referrer-Policy` | `strict-origin-when-cross-origin` |

### Content-Security-Policy (CSP)

La CSP est appliquée globalement. Directives importantes :

- **`connect-src 'self'`** — HTMX/fetch/SSE uniquement vers la même origine (atténue l'exfiltration de données via scripts injectés)
- `script-src` autorise `'unsafe-inline'` pour HTMX + CDN Chart.js sur les pages standard
- Les routes workspace (`/projects/{id}/workspace`) assouplissent `frame-src` pour les outils de dev embarqués (aperçu, admin DB)

Les modèles Jinja2 utilisent l'**auto-échappement** contre le XSS ; la CSP constitue une seconde couche.

## Sécurité du code et des données

| Sujet | Atténuation |
|-------|-------------|
| **Injection SQL** | Requêtes paramétrées (placeholders `?`) ; pas de f-strings SQL |
| **XSS** | Autoescape Jinja2 + CSP `connect-src 'self'` |
| **Injection de prompt** | Garde-fous adversariaux L0 + L1 sur les sorties d'outils |
| **Secrets** | `~/.config/factory/*.key`, chmod `600` ; ne jamais committer `*_API_KEY=dummy` |
| **Docker** | Le conteneur tourne sous un **utilisateur non-root** dédié (image minimale, pas de PID 1 root) |

## Niveaux de veto A2A

Les messages agent-à-agent supportent une force de veto : `ABSOLUTE`, `STRONG`, `ADVISORY` (`platform/a2a/veto.py`). Les L0/L1 adversariaux correspondent à des blocages absolus ; L2 peut apparaître en STRONG + escalade humaine.

## Documentation associée

- [Référence API](API-Reference) — exemples d'authentification Bearer
- [Patterns](Patterns) — patterns HITL et adversariaux
- [Guide de déploiement](Deployment-Guide) — durcissement production

[English](Security)
