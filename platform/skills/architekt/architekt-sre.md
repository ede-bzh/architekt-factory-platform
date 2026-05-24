---
name: Architekt SRE
description: Doctrine SRE Architekt — cloud matrix, SLO, runbooks, backup/restore, OTEL (ADR-005, ADR-017, ADR-044)
tags: [sre, architekt, hosting, slo, runbook, otel]
metadata:
  category: sre
  triggers: [deploy, hosting, monitoring, backup, slo, infra]
---

# Architekt SRE

## Objectif

Encoder la **doctrine SRE Architekt** : choix cloud rapide, observabilité, backups testés, incident response — ops proportionnées au niveau sécurité.

## Quand utiliser

- Choix hébergement (intake / ADR infra)
- Setup monitoring / alerting
- Rédaction runbook projet
- Incident production ou drill trimestriel

## Matrice cloud (ADR-017)

| Workload | Défaut | Alternative |
|----------|--------|-------------|
| Sites static Astro/Next | **Cloudflare Pages** | Vercel |
| Backend léger | **Fly.io ap-southeast** | Hetzner CAX |
| Backend lourd (>4GB) | **Hetzner CAX21+** | AWS EC2 |
| PostgreSQL | **Supabase** | RDS / Neon |
| Object storage | **Cloudflare R2** | AWS S3 |
| Plateforme Architekt | Hetzner CAX11 | — |
| Client impose cloud | Respecter (+ premium 10-15%) | — |

**Règle** : static → Cloudflare ; client impose → suivre ; budget serré <4GB → Fly.io ; sinon Hetzner.

## Pilote Architekt (ADR-005)

- Plateforme : VM Hetzner CAX11 (~5 €/mois), Docker compose
- Site : Cloudflare Pages (gratuit, edge ASEAN)
- Domaine + nginx + Let's Encrypt

## SLO & observabilité

- Définir SLO par service (disponibilité, latence p95)
- **OpenTelemetry** opt-in (`OTEL_ENABLED=1`) → Jaeger/OTLP
- Dashboards : DORA + erreurs + latence LLM
- Alertes P1/P2 avec runbook lié

## Backup & restore (ADR-044)

| Niveau | RPO | RTO | Test restore |
|--------|-----|-----|--------------|
| L0 | 24 h | 24 h | Annuel |
| L1 | 24 h | 8 h | Trimestriel |
| L2 | 4 h | 4 h | Mensuel |
| L3 | 1 h | 1 h | Mensuel + DR drill annuel |

**Règle 3-2-1** : 3 copies, 2 médias, 1 offsite. Backups chiffrés AES-256.

Composants : PostgreSQL (pg_dump + WAL/PITR), R2/S3 versioning, Git miroir, secrets Vault.

## Incident response (ADR-043)

| P | Exemple | Résolution cible |
|---|---------|------------------|
| P1 | Service down, data breach | < 4 h |
| P2 | Dégradation majeure | < 24 h |
| P3 | Bug fonctionnel subset | < 7 j |
| P4 | Cosmétique | Sprint suivant |

Process : Détection → Triage → Containment → Eradication → Recovery → Post-mortem (7 j).

## Livrables SRE par projet

- `<projet>/docs/runbook.md`
- `<projet>/docs/security/incident-response.md`
- Monitoring + alertes configurés
- Backup auto + restore test documenté

## Anti-patterns

- ❌ Backup jamais restauré ("on a des backups")
- ❌ Snapshot sur même serveur que prod
- ❌ Pas de runbook avant go-live
- ❌ Sur-provisionner infra "au cas où"
- ❌ Monitoring sans alerte actionnable

## Sources

- ADR-005 Pilot hosting
- ADR-017 Cloud decision matrix
- ADR-043 Incident response baseline
- ADR-044 Backup and restore standard
- Google SRE Book
