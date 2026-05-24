# Phase 5 — Internal Developer Platform

> Durée cible : **1-2 mois**
> Dépend de : Phase 4 (≥ 3 clients livrés, retours d'expérience documentés)
> Sortie : **mission → repo → CI → report générés automatiquement en < 10 minutes**

## Objectif

La plateforme Architekt devient un **vrai Internal Developer Platform (IDP)** : capable de lancer une nouvelle mission client avec environnement complet (repo, CI, secrets, déploiement, monitoring) en quelques minutes.

> DORA 2025 : les plateformes internes sont devenues quasi-universelles dans les organisations structurées et sont traitées comme **produits internes**.

## Pourquoi maintenant (et pas avant)

- Phase 4 a montré **où la friction est réelle** (pas spéculé)
- 3+ clients = matière à industrialiser
- Avant Phase 4, on aurait industrialisé du vide

## Référence marché 2026

| Outil | Force | Architekt verdict |
|-------|-------|-------------------|
| Backstage (OSS) | Portal + catalog, 1000+ plugins | **Trop lourd** pour 2 personnes (besoin équipe plateforme dédiée) |
| Humanitec | Platform Orchestrator (Score CNCF) | Vendor lock-in, $2199/mo+ |
| Port | SaaS portal, $30/seat/mo | Devient cher rapidement |
| Fortem | Self-hosted, AIOps built-in, $799/mo flat | Intéressant si on veut un produit clé en main |
| **Architekt Platform** (interne) | Notre code, agents IA déjà là | **Choix retenu** — pas de dépendance externe |

→ Architekt étend sa propre plateforme plutôt que d'adopter un IDP externe.

## Capacités à construire (10)

### 1. Mission manifest formalisé

Format YAML pour décrire une nouvelle mission client :

```yaml
client: acme-corp
offer: architekt-mvp
stack: nextjs-fastapi
budget_llm: 500_SGD
budget_hours: 200
deadline: 2026-08-15
sponsor: cto@acme.com
team:
  - lead_dev
  - architecte
  - qa
  - devops
```

### 2. Agent registry (déjà partiel)

Améliorer `platform/skills/definitions/` : versioning, scoring (Thompson), tags.

### 3. Template registry

- Workflow templates par offre (5 : Launch, MVP, Internal Tool, AI Workflow, Audit)
- Stack kits par Tier A stack
- Repo templates (`.github/workflows/`, `.gitignore`, structure dossiers)

### 4. Environment provisioning (Terraform)

Modules par cloud :

```
infrastructure/
  terraform/
    modules/
      cloudflare-pages/      # déploiement statique
      hetzner-vm/             # backend
      aws-ap-southeast-1/    # client AWS
      azure-sea/              # client Azure
    architects/
      client-template/        # composition modules par projet
```

### 5. Secrets management (vault par client)

- Doppler, Infisical ou HashiCorp Vault
- 1 workspace / projet client
- Rotation automatique
- Audit log accès

### 6. CI templates par stack Tier A

`.github/workflow-templates/` :

- `nextjs.yml` (build, test, mutation, deploy CF Pages)
- `fastapi.yml` (build, test, SAST, SBOM, deploy)
- `astro.yml` (build, a11y, Lighthouse, deploy)

### 7. Quality scanner exposé en API

`platform/metrics/quality.py` (existant) → expose `GET /api/projects/{id}/quality` :

```json
{
  "global_score": 78,
  "dimensions": {
    "complexity": 82,
    "coverage_ut": 75,
    "coverage_e2e": 70,
    "security": 90,
    "accessibility": 88,
    "performance": 92,
    "documentation": 65,
    "architecture": 85,
    "maintainability": 70,
    "adversarial": 80
  }
}
```

### 8. Cost tracker (FinOps par mission)

- Track tokens LLM par agent par mission
- Coût infra alloué (Hetzner, Cloudflare, services tiers)
- Heures humaines (intégration timesheet manuelle ou Toggl)
- Alerte 70 % / 90 % / 100 % budget
- Auto-pause à 100 % (sauf override CTO)

### 9. Audit trail

Pour chaque mission :

- Décisions agents (prompt, output, tool calls)
- Versions modèles utilisés
- Approbations humaines
- Hash code à chaque commit
- Reproductibilité : rejouer une mission identique en théorie

### 10. Client report generator

Génère automatiquement à la fin de chaque mission :

- PDF DORA (déploiement freq, lead time, MTTR, CFR)
- PDF qualité (10 dimensions + screenshots)
- SBOM (CycloneDX + SPDX)
- Handover doc Markdown
- Vidéo démo (capture browser auto)

## Plan en 6-8 semaines

| Semaine | Livrable |
|---------|----------|
| 1 | Mission manifest YAML + agent registry versioned |
| 2 | Template registry (workflows + stack kits) |
| 3 | Terraform modules Cloudflare + Hetzner |
| 4 | Secrets management (choix outil + intégration) |
| 5 | CI templates par stack Tier A |
| 6 | Quality scanner API + cost tracker |
| 7 | Audit trail + client report generator |
| 8 | Stabilisation + doc + retro |

## Pré-requis

- ≥ 3 clients livrés (Phase 4)
- ≥ 1 client récurrent (signal de répétabilité)
- Marge brute mesurée et > 50 %
- CTO + 1 personne dédiée plateforme (si embauche, sinon temps partiel CTO)

## Gate de passage

- [ ] Nouvelle mission créée en **< 10 minutes** (formulaire UI + auto-provisioning)
- [ ] Repo généré automatiquement à partir du template stack
- [ ] CI créée et verte au premier push
- [ ] Quality report généré automatiquement à la fin de mission
- [ ] Budget LLM visible par mission (FinOps dashboard)
- [ ] Audit trail consultable
- [ ] Documentation interne `docs/idp/` complète

## Risques

| Risque | Mitigation |
|--------|-----------|
| Construire un Backstage maison qui ne sert à personne | Toujours valider avec ≥ 1 client réel par capacité |
| Vendor lock-in (Doppler, Terraform Cloud) | Choisir outils self-hostable si possible |
| Complexité IaC pour 2 personnes | Garder modules simples, < 200 lignes par module |
| Coût infra dérive | FinOps dashboard obligatoire |
| Diluer focus delivery | Phase 5 ne démarre **que** quand Phase 4 stabilisée |

## Suivi

- Milestone GitHub : **Phase 5 — Internal Developer Platform**
- Labels : `phase:5-idp`, `area:platform`, `area:idp`
- Indicateur clé : **time-to-new-mission** (cible < 10 min)
