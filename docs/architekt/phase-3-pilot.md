# Phase 3 — Public Pilot

> Durée cible : **2 semaines**
> Dépend de : Phase 2 (CI verte, 12 skills mergés, sécurité supply-chain)
> Sortie : **`architekt.*` live + actif commercial complet**

## Objectif

Le site Architekt n'est **pas seulement un site** — c'est un **actif commercial complet** :

- preuve produit (fait par la plateforme elle-même)
- preuve qualité (Lighthouse, WCAG, Stryker, SBOM publiés)
- preuve méthode (page Method)
- preuve différenciation (case study + démo vidéo)

## Livrables (10)

### Site

| # | Livrable |
|---|----------|
| 1 | **Site Architekt** Astro 5 + Tailwind v4 + shadcn/ui |
| 2 | Pages **Home / Offres / Method / Platform / Proof / Team / Contact / Blog** |
| 3 | i18n **EN + FR + ZH** |
| 4 | Plausible analytics (PDPA-friendly) |
| 5 | Formulaire contact fonctionnel (Formspark ou similaire) |

### Actifs commerciaux

| # | Livrable |
|---|----------|
| 6 | **Case study fictif réaliste** ("How Architekt would deliver X for Y") |
| 7 | **Démo vidéo 2 minutes** (mission agentique → livrable) |
| 8 | **Rapport qualité exportable** (DORA + Lighthouse + Stryker + SBOM) |
| 9 | **Mini dashboard public** (`architekt.TBD/proof`) : score DORA, tests, a11y, Lighthouse, security scan |
| 10 | **Candidature IMDA SME Digital Solutions** déposée |

### Plateforme runtime

- VM **Hetzner CAX11** Helsinki ou Hillsboro (~5 €/mois) — ADR-005
- Auth **fail-closed** (`ARCHITEKT_API_KEY` obligatoire)
- HTTPS via Caddy ou Traefik
- Backups snapshots quotidiens (+1 €/mois)
- Domaine `architekt.{sg|ai|io}`

## Stack pilote (Tier A uniquement)

```
Astro 5 + Tailwind v4 + shadcn/ui
  ↳ Contenu : Markdown (pas de CMS)
  ↳ i18n : Astro built-in (EN/FR/ZH)
  ↳ Forms : Formspark ou Web3Forms
  ↳ Analytics : Plausible (cloud ou self-hosted)
  ↳ Deploy : Cloudflare Pages (push GitHub → auto-deploy)
  ↳ Domain : Cloudflare DNS
```

## Audit accessibilité (a11y) obligatoire

shadcn/Radix donne **les bases** WCAG mais **certains composants nécessitent corrections** (focus, contraste, ARIA labels). Outils :

- **axe-core** (automatique en CI Playwright)
- **Pa11y** (CLI scan)
- **Tests manuels** : navigation clavier, screen reader VoiceOver/NVDA sur Home + Contact

Gate : **WCAG 2.2 AA** vérifié, pas seulement "présumé".

## Brief mission idéation (à coller dans la plateforme)

```
Projet : site vitrine Architekt (architekt.TBD)
Cible : prospects ASEAN (entrepreneurs, scale-ups, founders, DSI SG/MY/ID/TH/VN)
Objectif : convertir vers un appel découverte (CTA principal) ou audit
Stack imposée : Astro 5 + Tailwind v4 + shadcn/ui
Langues : EN + FR + ZH
Tone : pro, technique, asiatique-friendly, PAS startup-hype
Pages : Home, Offres (5 cards), Method (3 piliers), Platform (capacités), Proof (case study + démo + dashboard), Team, Contact, Blog
Contenu :
  - docs/ROADMAP.md pour la méthode
  - docs/OFFERS.md pour les offres
  - docs/CATALOG.md pour les stacks
  - 1 case study "How Architekt delivers a SaaS MVP in 6 weeks"
Contraintes :
  - Score Lighthouse >= 95 toutes catégories
  - a11y WCAG 2.2 AA vérifié (axe-core en CI)
  - Mutation testing Stryker >= 60% sur logique critique
  - Pas de tracking invasif (Plausible only)
  - Hébergement Cloudflare Pages
  - Branding Architekt (palette définie Phase 0)
  - Mobile-first
  - Conforme PDPA SG (mentions légales, cookie banner si analytics > strictly necessary)
```

## Plan en 2 semaines

### Semaine 1 — Plateforme runtime + setup

| Jour | Action |
|------|--------|
| J1 | Acheter VM Hetzner CAX11, SSH, Docker, clone repo `architekt-factory-platform` |
| J2 | Déploiement plateforme (docker compose) + `ARCHITEKT_API_KEY` |
| J3 | Domaine `platform.architekt.TBD` + HTTPS (Caddy ou Traefik) |
| J4 | Login UI, projet créé `architekt-website` dans la plateforme |
| J5 | Première mission test (idéation simple), validation que tout tourne |

### Semaine 2 — Site

| Jour | Action |
|------|--------|
| J6 | Brief mission "site Architekt" via UI idéation |
| J7-J8 | Mission tourne, observation, ajustements skills/prompts |
| J9 | Code généré dans workspace → push GitHub `architekt-website` (repo séparé) |
| J10 | Cloudflare Pages branchée, premier deploy preview |
| J11 | Domaine `architekt.TBD` acheté + DNS, HTTPS, deploy production |
| J12 | Tests Lighthouse + axe-core, corrections, démo vidéo enregistrée, post LinkedIn |

## Pré-requis

- Phase 2 mergée (CI verte, 12 skills présents)
- Carte bancaire pour Hetzner (~5 €/mois)
- Carte bancaire pour domaine (~15 €/an)
- Compte Cloudflare (gratuit)
- Compte Plausible (cloud ~9 €/mois ou self-hosted)
- Compte Formspark ou similaire (gratuit jusqu'à 250 soumissions)
- 1 vidéo screencast (Loom gratuit ou OBS)

## Gate de passage

- [ ] `https://architekt.*` accessible publiquement
- [ ] Lighthouse ≥ 95 toutes catégories
- [ ] WCAG 2.2 AA **vérifié** (axe-core + audit manuel)
- [ ] Formulaire contact fonctionnel (email reçu)
- [ ] Démo vidéo publiée (LinkedIn + YouTube unlisted)
- [ ] 1 case study publié sur le site (`/proof`)
- [ ] 1 rapport qualité exportable (PDF + page `/proof/quality`)
- [ ] Candidature IMDA SME Digital Solutions déposée
- [ ] `docs/case-studies/architekt-website.md` interne écrit (retour d'expérience)

## Risques

| Risque | Mitigation |
|--------|-----------|
| VM Hetzner indisponible | Backups + restore documenté |
| Lighthouse < 95 (images, fonts) | Optimisation images (AVIF), font-display swap, preload |
| WCAG fail | Audit obligatoire avant go-live |
| Coût LLM mission trop élevé | Budget tokens limite + alerte (cf. FinOps) |
| Domaine indisponible | Avoir un fallback (.sg + .ai + .io vérifiés) |
