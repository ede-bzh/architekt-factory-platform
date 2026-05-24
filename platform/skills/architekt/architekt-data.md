---
name: Architekt Data
description: Doctrine données Architekt — PostgreSQL, isolation client, rétention, RPO/RTO (ADR-018)
tags: [data, architekt, postgresql, retention, isolation]
metadata:
  category: data
  triggers: [database, migration, schema, retention, postgres]
---

# Architekt Data

## Objectif

Encoder la **doctrine données Architekt** : PostgreSQL par défaut, isolation client, rétention formalisée, droits sujets — conformité PDPA/RGPD.

## Quand utiliser

- Choix modèle de données / migrations
- Setup DB nouveau projet client
- Politique rétention / anonymisation
- Demande export / suppression données client

## Stack data (défaut)

| Cas | Recommandation |
|-----|----------------|
| DB principale | **PostgreSQL** |
| Cache | + Redis |
| Search | PostgreSQL FTS, sinon Meilisearch |
| Vector AI | pgvector d'abord (pas vector DB dédiée sans justification) |

## Isolation par client (ADR-018)

| Donnée | Isolation |
|--------|-----------|
| Code | Repo Git dédié (1 repo = 1 client) |
| Secrets | Vault workspace dédié (Doppler/Infisical) |
| DB fonctionnelle | **DB dédiée par client** (pas multi-tenant phase studio) |
| Logs missions | Tag `client_id`, rétention par client |
| Backups | Snapshot par projet, chiffrement client-side |

## Rétention par type

| Type | Rétention | Après |
|------|-----------|-------|
| Code client | Contrat + 90 j post-livraison | Transfert client + suppression Architekt |
| Données fonctionnelles | 3-7 ans (contrat) | Suppression certifiée |
| Logs avec data client | 90 j | Anonymisation → archive 1 an |
| Traces LLM | 30 j | Anonymisation |
| Backups | 90 j rolling | Suppression auto |
| Factures/contrats | 7 ans (SG) | Archive sécurisée |

## Droits client

- **Accès** : copie complète sous 30 j
- **Suppression** : sous 30 j (sauf obligation légale)
- **Portabilité** : export JSON/CSV
- **Breach** : notification 72 h (PDPA/RGPD)

## Anonymisation

- Hash noms/emails/identifiants ; suppression secrets/tokens
- Outils : `presidio` ou regex maison
- Conserver patterns techniques uniquement pour skills internes

## Migrations

- Migrations versionnées (Alembic, Prisma, Flyway)
- Rollback testé en staging
- Pas de migration destructive sans backup + fenêtre validée

## Anti-patterns

- ❌ Multi-tenant DB partagée sans isolation (phase studio)
- ❌ Timestamps sans timezone (toujours UTC ISO 8601)
- ❌ Pas de politique rétention documentée
- ❌ Backup sans restore testé
- ❌ Données client dans logs non anonymisés

## Sources

- ADR-018 Data retention and client isolation
- NIST SP 800-88 Media Sanitization
- Singapore PDPA, RGPD
