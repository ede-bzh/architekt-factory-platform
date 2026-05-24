# ADR-044 : Backup and restore standard

- **Statut** : Proposé
- **Date** : 2026-05-24
- **Décideurs** : CTO, SRE

## Contexte

"Backups exist" ne veut rien dire sans restore testé. Beaucoup d'agences ont perdu des données client sur backup corrompu / partiel / inaccessible.

## Décision

**Tout projet Architekt en production doit avoir backup ET restore testés.**

### Standards par niveau sécurité

| Niveau | RPO max | RTO max | Type backups | Test restore |
|--------|---------|---------|--------------|--------------|
| L0 | 24 h | 24 h | Snapshot quotidien | Annuel |
| L1 | 24 h | 8 h | Snapshot quotidien + WAL | Trimestriel |
| L2 | 4 h | 4 h | PITR + snapshots + offsite | Mensuel |
| L3 | 1 h | 1 h | PITR + multi-region + immutable | Mensuel + 1 DR drill annuel |

### Composants à backup

| Composant | Stratégie |
|-----------|-----------|
| PostgreSQL | pg_dump + WAL archiving + PITR (Supabase / RDS / Neon : built-in) |
| Object storage (R2/S3) | Versioning + cross-region replication (L2+) |
| Repo Git | GitHub default + miroir (GitLab, Codeberg) si critique |
| Secrets | Vault backup chiffré + recovery codes physiques |
| Config IaC | Versioned (Terraform state encrypted) |
| Logs | Archive cold storage (S3 Glacier, R2 archive) |

### Standard "3-2-1"

- **3** copies des données
- **2** types de stockage différents
- **1** copie offsite (autre cloud / autre région)

### Encryption

- Backups encryptés at rest (AES-256)
- Clés gérées séparément du backup
- Tester restore avec clés (sinon backup inutile)

### Tests restore

- Quarterly minimum : restore en environnement isolé
- Documenter temps réel (vs RTO cible)
- Si > RTO → revue + correction
- Documenter dans `<projet>/docs/runbook.md`

### Disaster Recovery (L2-L3)

- DR runbook documenté
- Sauvegarde infrastructure (Terraform state, network config)
- Annual DR drill (full failover + restore)
- Communication plan client en cas de DR

## Anti-patterns

- ❌ "On a des backups" sans jamais avoir restauré
- ❌ Backup sur même serveur que prod (vol/crash = tout perdu)
- ❌ Snapshot manuel (humain oublie)
- ❌ Pas de versioning S3 (overwrite supprime irréversiblement)
- ❌ Backups sans encryption (fuite via vol disque)

## Conséquences

### Positives
- Confiance client (continuité business)
- Conformité (RGPD Article 32 — disponibilité)
- Argument vente B2B

### Négatives
- Coût storage backups (faible vs valeur)
- Process à maintenir
- Mitigation : automatisation (Phase 5 IDP)

## Sources
- NIST SP 800-34 (Contingency Planning Guide)
- ISO/IEC 27001 A.5.30 (ICT readiness for business continuity)
- 3-2-1 rule (industry standard)
- `docs/SECURITY.md`
