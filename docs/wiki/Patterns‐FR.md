# Patterns d'orchestration (15)

Les patterns définissent comment les agents collaborent dans une phase. Chaque phase de workflow fixe un `pattern_id` consommé par `PatternEngine` (`platform/patterns/engine.py`). Quinze patterns sont livrés : **12** stockés en base (modifiables dans l'UI) et **3** moteur uniquement (`solo`, `loop`, `network`).

Voir aussi : [Sécurité](Security) (adversarial L0–L2), [Workflows](Workflows) (36 modèles).

## Comment les patterns s'attachent aux missions

Le contrôle de mission exécute les phases de workflow dans l'ordre. Exemple — **`product-lifecycle`** (épopée de bout en bout canonique) :

| ID de phase | Pattern | Étape de mission |
|-------------|---------|------------------|
| `ideation` | `network` | Débat de découverte (PM, UX, architecte, métier) |
| `strategic-committee` | `human-in-the-loop` | GO / NOGO / PIVOT |
| `project-setup` | `sequential` | Constitution (backlog, sprints, cérémonies) |
| `architecture` | `aggregator` | Analyses parallèles → synthèse architecte |
| `dev-sprint` | `hierarchical` | Lead délègue aux workers TDD |
| `build-verify` | `sequential` | CI compilation from scratch |
| `cicd` | `sequential` | Pipeline + DevSecOps |
| `qa-campaign` | `loop` | Boucle QA jusqu'à approbation |
| `qa-execution` | `parallel` | E2E + API + perf en parallèle |
| `deploy-prod` | `human-in-the-loop` | **Porte de déploiement HITL** (canary → GO humain) |
| `tma-router` | `router` | Routage d'incidents |
| `tma-fix` | `loop` | Boucle de maintenance corrective |

Portes entre phases : `always`, `no_veto`, `all_approved` — voir [Sécurité](Security#human-in-the-loop-hitl-deploy-gate).

## Patterns configurés en base (12)

### `solo-chat`

**Cas d'usage :** Un seul spécialiste, conversationnel (chat projet, boîte à outils).

**Adéquation mission :** Sessions ad hoc, pas les longues épopées SAFe.

**Protocole :** Exécution solo ; adversarial léger sur les écritures de code.

---

### `sequential`

**Cas d'usage :** Pipeline — chaque sortie d'agent alimente la suivante (constitution, CI/CD, documentation).

**Adéquation mission :** `project-setup`, `cicd`, `build-verify`, étapes backup/restore.

**Chaîne exemple :** Brain → Worker → critique code.

---

### `parallel`

**Cas d'usage :** Travail en éventail (QA multi-suites, scénarios chaos, scans de licences).

**Adéquation mission :** `qa-execution`, chaos-scheduled charge + sondes sécurité.

**Porte :** Souvent `all_approved` — toutes les branches doivent terminer.

---

### `hierarchical`

**Cas d'usage :** Le lead décompose les stories, les workers rapportent, le lead intègre.

**Adéquation mission :** `dev-sprint`, planification `cicd-pipeline`, épopées mobile.

**Protocole :** `_DECOMPOSE_PROTOCOL` → `_EXEC_PROTOCOL` → `_QA_PROTOCOL`.

---

### `router`

**Cas d'usage :** Triage — un agent classifie l'entrée et route vers un spécialiste.

**Adéquation mission :** `tma-router`, classification d'incidents `dsi-platform-tma`.

**Créneaux spécialistes :** Dev TMA, SRE, automatisation de tests, sécurité.

---

### `aggregator`

**Cas d'usage :** Des spécialistes en parallèle produisent des brouillons ; un architecte consolide.

**Adéquation mission :** Phase `architecture` (lead dev, UX, sécurité, DevOps → architecte).

**Protocole :** Discussion + synthèse (recherche, pas fusion aveugle).

---

### `human-in-the-loop`

**Cas d'usage :** Les agents travaillent jusqu'à un **checkpoint** ; l'humain soumet GO/NOGO via l'UI ou `POST /api/missions/{id}/validate`.

**Adéquation mission :** Comité stratégique, **déploiement production**, bascule migration de données, promotion canary.

**Porte :** En général `all_approved` — la mission est en pause jusqu'à validation.

---

### `debate`

**Cas d'usage :** Des agents opposés débattent ; le juge (brain) tranche.

**Adéquation mission :** `debate-decide`, choix d'options d'architecture.

**Config :** `max_rounds` (défaut 5).

---

### `sf-tdd`

**Cas d'usage :** Pipeline factory complet : plan → implémentation TDD → multi-critiques → DevOps.

**Adéquation mission :** Workflows feature-sprint, chemins de livraison durcis.

**Chaîne :** Brain → worker TDD → critique code → critique sécurité → critique archi → DevOps.

---

### `wave`

**Cas d'usage :** **Vagues** ordonnées par dépendances — parallèle dans une vague, séquentiel entre vagues.

**Adéquation mission :** Gros backlogs avec DAG de tâches explicite (vagues infra, étapes de migration).

---

## Patterns adversariaux

Ils intègrent la revue **Team of Rivals** (voir [Sécurité](Security#adversarial-validation-l0--l1--l2)).

### `adversarial-pair`

**Cas d'usage :** Rédacteur et relecteur itèrent jusqu'au consensus ou au max d'itérations.

**Adéquation mission :** Revue documentation, validation backup-restore, validation design system.

**Mécanisme :** Arête `conditional: veto` boucle rédacteur → critique (jusqu'à 5×).

**Couches :** Principalement L0 + L1 ; escalade L2 sur signaux d'architecture.

---

### `adversarial-cascade`

**Cas d'usage :** Défense en couches — **L0 → L1 code → L1 sécurité → L2 architecture** en séquence.

**Adéquation mission :** Changements à haut risque (remédiation security-hacking, livrables conformité).

**Agents (défaut) :** worker → code-critic → security-critic → arch-critic.

**Règle :** Pas de sortie de phase sur veto absolu ; incidents journalisés dans `platform_incidents` pour DORA.

---

## Patterns moteur uniquement (3)

| Pattern | Cas d'usage | Adéquation mission |
|---------|-------------|-------------------|
| `solo` | Un agent, pas de trafic bus | Outils one-shot rapides |
| `loop` | Répéter jusqu'à approbation ou max d'itérations | Campagne QA, revue UX, correctif TMA |
| `network` | Discussion multi-agents libre | **Idéation**, découverte fonctionnalités DSI |

`network` ignore L1 adversarial sur les sorties de discussion pour ne pas bloquer le brainstorming ; L0 bloque toujours le slop/mock évident.

## Matrice pattern × protocole

| Protocole | Patterns |
|----------|----------|
| **RESEARCH** (lecture/recherche uniquement) | `network`, `human-in-the-loop`, `debate`, `aggregator` |
| **EXEC / QA / DECOMPOSE** | `hierarchical`, `sequential`, `parallel`, `loop`, `wave`, `sf-tdd` |
| **Adversarial** | `adversarial-pair`, `adversarial-cascade` (+ garde-fous sur tous les patterns d'exécution) |

## Choisir un pattern

| Objectif | Préférer |
|----------|----------|
| Brainstormer les besoins | `network` ou `debate` |
| Besoin d'accord humain | `human-in-the-loop` |
| Livrer du code avec revue | `hierarchical` + garde adversarial |
| Assurance maximale | `adversarial-cascade` ou `sf-tdd` |
| Router les tickets support | `router` + `loop` |

Des patterns personnalisés peuvent être créés dans l'UI (lignes non-builtin dans la table `patterns`) ; les builtins sont re-seedés à la mise à jour via `seed_builtins()`.

## Documentation associée

- [Workflows](Workflows) — quel `pattern_id` chaque modèle utilise
- [Référence API](API-Reference) — endpoint `validate` pour HITL
- [Architecture](Architecture) — PatternEngine et MessageBus

[English](Patterns)
