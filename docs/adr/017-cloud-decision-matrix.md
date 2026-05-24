# ADR-017 : Cloud deployment decision matrix

- **Statut** : Proposé
- **Date** : 2026-05-24
- **Décideurs** : CTO, SRE, CISO

## Contexte

Plusieurs clouds disponibles (Azure, AWS, GCP, Cloudflare, Hetzner, Fly.io). Sans matrice claire, dispersion ops et lock-in vendor.

## Décision

**Matrice de décision cloud par type de workload.**

### Workloads et défauts

| Workload | Recommandation 1 | Recommandation 2 | Notes |
|----------|------------------|------------------|-------|
| Sites statiques Astro/Next | **Cloudflare Pages** | Vercel | Edge global ASEAN, gratuit |
| Backend Python/Node léger | **Fly.io ap-southeast** | Hetzner CAX | Géoredondance possible |
| Backend lourd (>4GB RAM) | **Hetzner CAX21+** | AWS EC2 | Hetzner = ratio prix/perf |
| Bases PostgreSQL | **Supabase** | RDS / Neon | Supabase = setup rapide |
| Stockage S3 | **Cloudflare R2** | AWS S3 | R2 = no egress fee |
| Plateforme Architekt | **Hetzner CAX11** SG-friendly | Azure existant | Pilote |
| Client AWS imposé | **EKS Fargate / ECS** ap-southeast-1 | — | Premium 10 % |
| Client Azure imposé | **AKS / App Service** Southeast Asia | — | Premium 10 % |
| Client GCP imposé | **Cloud Run** asia-southeast1 | — | Premium 10 % |
| Mobile builds Android | Docker Hetzner | macOS Anka (iOS) | Cluster dédié |
| Workflows IA agentique | Plateforme Architekt (Hetzner) | — | Notre métier |

### Critères décision

```
Si workload = static site
  → Cloudflare Pages (par défaut)
Sinon si client impose cloud
  → respecter (+ premium pricing 10-15%)
Sinon si workload < 4GB et budget serré
  → Fly.io ap-southeast
Sinon
  → Hetzner CAX
```

### Multi-région (post Phase 5)

- Primary : SG (ap-southeast-1 / SEA / SG datacenter)
- Failover : Helsinki ou Tokyo (selon client)
- DR formel : phase d'industrialisation (Phase 5+)

### Souveraineté / résidence données

| Cas | Cloud obligatoire |
|-----|-------------------|
| Client SG gouvernement | AWS ou Azure Singapore region uniquement |
| Client santé SG (HSA) | AWS / Azure SG + chiffrement KMS client-managed |
| Client EU | AWS / Azure / GCP region EU + DPA |
| Client par défaut | Choix Architekt selon recommandation |

## Conséquences

### Positives
- Décisions rapides (matrice claire)
- Coûts maîtrisés (Hetzner / Cloudflare = bas)
- Compatibilité enterprise (peut suivre client)

### Négatives
- Plusieurs clouds à maîtriser (acceptable post Phase 5 IDP)
- Mitigation : Terraform modules par cloud (Phase 5)

## Coûts indicatifs 2026

| Service | Coût mensuel pilote |
|---------|---------------------|
| Hetzner CAX11 (plateforme Architekt) | 5 € |
| Backups Hetzner | 1 € |
| Cloudflare Pages (site Architekt) | 0 € |
| Cloudflare R2 (100 GB) | 1,5 € |
| Domaine .ai ou .sg | 50-100 € / an |
| Plausible self-hosted (dans VM) | 0 € |
| **Total pilote** | **~10 €/mois** |

## Sources

- Hetzner pricing 2026
- Cloudflare pricing 2026
- AWS / Azure / GCP region maps APAC
