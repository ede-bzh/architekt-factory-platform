# Phase 3 — Pilote : site Architekt en ligne

> Durée cible : **2 semaines**
> Dépend de : Phase 2 (CI verte, skills mergés)
> Sortie : `architekt.TBD` accessible publiquement

## Objectif

Utiliser la plateforme Architekt pour fabriquer son **propre site**, et l'avoir en ligne.
Sert de **preuve produit + demo client**.

## Sous-objectifs

1. Plateforme Architekt déployée (cf. ADR-005 : Hetzner)
2. Mission "site Architekt" lancée sur la plateforme
3. Site Astro construit par les agents
4. Déploiement Cloudflare Pages
5. Rapport DORA + QualityScanner exporté → 1er case study interne

## Stack site Architekt

- **Astro 5** + **Tailwind v4** + **shadcn/ui** (via `shadcn` Astro adapter)
- Contenu : Markdown (pas de CMS au début)
- i18n : EN + FR + ZH (Singapour)
- Analytics : Plausible
- Hébergement : Cloudflare Pages
- Domaine : `architekt.TBD` (acheter quand tranché)

## Pages

| Page | Contenu |
|------|---------|
| `/` Home | Pitch Architekt + 3 offres + CTA contact |
| `/offres` | Discover / Build / Run |
| `/methode` | SAFe agentique, TDD, mutation testing, modular monolith |
| `/stacks` | Catalogue technos (extrait de `docs/CATALOG.md`) |
| `/equipe` | CPO + CTO |
| `/contact` | Form simple → email |
| `/blog` | 1 post au lancement (case study site Architekt lui-même) |

## Plan en 2 semaines

### Semaine 1 — Plateforme runtime

| Jour | Action |
|------|--------|
| J1 | Acheter VM Hetzner CAX11, SSH, Docker, clone repo |
| J2 | Déploiement plateforme + auth fail-closed (ARCHITEKT_API_KEY) |
| J3 | Domaine `platform.architekt.TBD` + HTTPS (Caddy ou Traefik) |
| J4 | Login UI, projet créé "architekt-website" |
| J5 | Première mission test (idéation → epic), validation |

### Semaine 2 — Site

| Jour | Action |
|------|--------|
| J6 | Brief mission "site Architekt" via UI idéation |
| J7-J8 | Mission tourne, observation, ajustements |
| J9 | Code généré dans workspace → push GitHub `architekt-website` |
| J10 | Cloudflare Pages branchée, premier deploy preview |
| J11 | Domaine `architekt.TBD` acheté + DNS |
| J12 | Go-live, screenshot, post LinkedIn |

## Brief idéation (à coller dans la plateforme)

```
Projet : site vitrine Architekt
Cible : prospects ASEAN (entrepreneurs, scale-ups, DSI)
Objectif : convertir vers un appel découverte
Stack imposée : Astro 5 + Tailwind v4 + shadcn/ui
Langues : EN + FR + ZH
Tone : pro, technique, asiatique-friendly, pas startup-hype
Pages : Home, Offres (Discover/Build/Run), Méthode, Stacks, Équipe, Contact, Blog
Contenu : voir docs/CATALOG.md et docs/ROADMAP.md pour références
Contraintes :
- Score Lighthouse >= 95 toutes catégories
- a11y WCAG 2.2 AA
- Mutation testing Stryker >= 60%
- Pas de tracking invasif (Plausible only)
- Hébergement Cloudflare Pages
- Branding Architekt (couleur TBD, fallback purple actuel)
```

## Pré-requis

- Phase 2 mergée (CI verte, skills présents)
- Carte bancaire pour Hetzner (~5 €/mois)
- Carte bancaire pour domaine (~15 €/an)
- Compte Cloudflare (gratuit)

## Gate de passage

- [ ] `https://architekt.TBD` accessible
- [ ] Lighthouse ≥ 95
- [ ] Rapport QualityScanner exporté
- [ ] Case study écrit (`docs/case-studies/architekt-website.md`)
- [ ] Demo 5 min enregistrée
