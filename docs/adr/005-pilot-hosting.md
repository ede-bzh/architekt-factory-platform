# ADR-005 : Hébergement du pilote (plateforme + site Architekt)

- **Statut** : Proposé
- **Date** : 2026-05-24
- **Décideurs** : CTO, SRE (agent), CPO

## Contexte

Pour le pilote (Phase 3), il faut deux choses qui tournent :

1. **La plateforme Architekt** (FastAPI + agents) → besoin VM ou conteneur quelque part
2. **Le site Architekt** (Astro) → besoin hébergement static + edge

## Décision

### Plateforme : **VM Hetzner ARM dédiée Architekt**

| Paramètre | Valeur |
|-----------|--------|
| Provider | Hetzner Cloud |
| Type | CAX11 (ARM, 2 vCPU, 4 GB RAM) |
| Région | **Helsinki** (proche Europe) ou **Hillsboro** (proche Asie) |
| Coût | ~5 €/mois |
| OS | Debian 12 |
| Déploiement | Docker compose (réutilise `deploy/docker-compose-vm.yml` adapté) |

**Pourquoi pas Azure existant ?**
- Azure prod actuel = ancienne marque, partagé avec ancien projet
- Repartir propre = pas de confusion clients, pas de risque casser l'existant

**Pourquoi pas Mac local ?**
- 2 utilisateurs (CPO + CTO) → besoin instance partagée
- Vraie URL nécessaire pour démo client

### Site Architekt : **Cloudflare Pages**

| Paramètre | Valeur |
|-----------|--------|
| Provider | Cloudflare Pages |
| Stack | Astro 5 build → assets statiques + edge functions |
| Coût | Gratuit (plan free suffit largement) |
| Edge | Global, incluant nœuds Singapour / Hong Kong |
| Domaine | `architekt.TBD` (CNAME vers Pages) |
| Analytics | Plausible (auto-hébergé ou Cloud, PDPA-friendly) |

## Alternatives écartées

| Option | Pourquoi non |
|--------|--------------|
| AWS Singapore (EC2 + ALB) | Surdimensionné, ~30 €/mois minimum |
| Azure SEA nouvelle VM | Coût + lock-in vendor au lancement |
| Vercel pour site | Très bien aussi, mais Cloudflare moins cher Asie |
| Render / Fly.io pour plateforme | Hetzner = meilleur ratio prix/perf |

## Plan d'activation

1. Acheter VM Hetzner CAX11 (1 jour)
2. SSH + Docker installé + clone du repo (`cursor/architekt-roadmap-7576` puis `main`)
3. `docker compose up -d` avec config Architekt
4. Domaine `architekt.TBD` acheté (cf. issue dédiée)
5. Nginx + Let's Encrypt → HTTPS sur sous-domaine `platform.architekt.TBD`

## Conséquences

### Positives
- 5 €/mois total → quasi gratuit
- Indépendance vendor cloud
- Setup propre, séparé de l'existant historique

### Négatives
- VM unique → pas de HA (acceptable phase pilote)
- ARM → certaines images Docker à vérifier (FastAPI, Python : OK ; Android-builder : KO)

### Risques
- Si charge augmente → migrer vers VM plus grosse (Hetzner CAX21, ~10 €/mois) ou ajouter une 2e
- Backups : snapshot quotidien Hetzner (+1 €/mois)

## Migration vers cloud client

Si un futur client demande AWS SG ou Azure SEA :

- Le code étant 12-Factor (Phase 2), redéploiement = 1-2 jours
- ADR séparé à écrire pour ce client
