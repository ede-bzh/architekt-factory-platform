# Phase 4 — Équipement à la demande

> Durée : **continue** (déclenché par signature client)
> Dépend de : Phase 3 (site Architekt en ligne)

## Principe

**Aucune nouvelle techno équipée tant qu'aucun client ne la demande.**

Cela évite :
- Brûler 1-2 mois sur des kits sans usage
- Dégrader la qualité agents (trop de cas à gérer)
- Disperser l'équipe (2 personnes)

## Triggers et actions

| Trigger | Action immédiate | Budget temps |
|---------|-----------------|--------------|
| 1er client **WordPress** signé | Activer kit WordPress | 2 j |
| 1er client **Shopify** | Activer kit Shopify | 2 j |
| 1er client **Java/Spring** | Activer kit Spring Modulith + image JDK 21 | 3 j |
| 1er client **Nuxt/Vue** | Activer kit Nuxt | 1 j |
| 1er client **NestJS** | Activer kit NestJS | 1 j |
| 1er client **Payload CMS** | Activer kit Payload | 1 j |
| 3 missions parallèles | Augmenter `Semaphore` missions de 1 à 3 | 1 j |
| 5 clients actifs | Portail client read-only v1 | 5 j |
| Client demande AWS | Module Terraform AWS ap-southeast-1 | 3 j |
| Client demande SSO | OIDC + RBAC v1 | 5 j |
| Client demande facturation usage | Stripe + ACU LLM tracking | 8 j |

## Processus d'activation d'un kit (template)

À reproduire à chaque trigger :

### Étape 1 — Issue GitHub (5 min)
- Template `chore.yml`, label `kit:<stack>`, milestone "Active stacks"
- Référence le client / contrat

### Étape 2 — Agent YAML (30 min)
- Créer `platform/skills/definitions/<role>_dev.yaml` à partir de `_template.yaml`
- Définir : persona, system_prompt, skills, tools, llm, permissions

### Étape 3 — Image Docker si nécessaire (1 j max)
- Suivre modèle `android-builder` (Dockerfile + docker compose entry)
- Ajouter à `deploy/docker-compose-vm.yml`

### Étape 4 — Workflow kit (30 min)
- Créer `platform/workflows/definitions/<stack>-epic.yaml`
- Phases : ideation → archi → dev → qa → ship
- Gates appropriés

### Étape 5 — Documentation catalog (1 h)
- Remplir `docs/catalog/<stack>.md` (commandes build, exemple, gotchas)
- Mettre à jour `docs/CATALOG.md` : statut ⚠️ → ✅

### Étape 6 — Mission de validation (= projet client lui-même)
- Le 1er projet client de cette stack = la validation du kit
- Retour d'expérience dans `docs/case-studies/<client>.md`

## Triggers business

| Étape business | Conséquences plateforme |
|----------------|------------------------|
| 1 case study public | Mettre à jour site Architekt section blog |
| 3 clients facturés | Démarrer ADR-007 multi-tenant |
| 5 clients | Embauche 1ʳᵉ personne (PM ou dev) |
| 10 clients ou 1er gros compte | SSO/RBAC + audit log |
| 1er client réglementé (banque, santé) | SOC2 lite + DR client-spécifique |

## Anti-patterns à éviter

| Tentation | Pourquoi non |
|-----------|--------------|
| Pré-équiper 5 stacks "au cas où" | Aucun ROI tant qu'aucun client |
| Refactor majeur plateforme | Attendre signaux clients réels |
| Multi-tenant avant 3 clients | YAGNI |
| AWS + Azure dès le début | Cloud cible suit le 1er client enterprise |
| SaaS public | Hors stratégie studio |

## Suivi

- Milestone GitHub **Phase 4 — On-demand** (toujours ouvert)
- Labels `kit:wordpress`, `kit:shopify`, `kit:spring`, etc.
- Tableau de bord projet : nb missions/mois, nb stacks actives, MRR
