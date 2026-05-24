# ADR-018 : Data retention and client isolation

- **Statut** : Proposé
- **Date** : 2026-05-24
- **Décideurs** : CTO, CISO, DPO (externe)

## Contexte

Architekt manipule des données client (code, secrets, logs, missions). Sans politique formelle de rétention et d'isolation, risque PDPA SG / RGPD UE / contrats clients.

## Décision

### Isolation par client

| Type de donnée | Isolation |
|----------------|-----------|
| Code client | Repo Git dédié par client (1 repo = 1 client) |
| Secrets | Vault workspace dédié par client (Doppler / Infisical) |
| Logs missions | Tag `client_id` sur tous les logs, retention par client |
| Memory plateforme | Tag `project_id`, FTS par projet |
| Données fonctionnelles client | DB dédiée par client (pas de schema multi-tenant phase studio) |
| Backups | Snapshot par projet, chiffrement client-side |

### Rétention par type

| Type | Rétention | Action après |
|------|-----------|--------------|
| Code client | Pendant contrat + 90 j post-livraison | Transfert au client + suppression Architekt (sauf accord pour case study anonymisé) |
| Données fonctionnelles client | Selon contrat (3-7 ans typique) | Suppression certifiée |
| Logs missions (avec data client) | 90 jours | Anonymisation puis archive 1 an |
| Logs missions (anonymisés) | 2 ans | Suppression |
| Traces LLM (prompts/outputs) | 30 jours | Anonymisation puis 1 an pour entraînement skills |
| Backups | 90 jours rolling | Suppression auto |
| Factures + contrats | 7 ans (obligation SG) | Archive sécurisée |
| Données employés | Selon loi locale | — |

### Anonymisation (process)

- Remplacement noms / emails / identifiants par hash
- Suppression secrets / clés / tokens
- Conservation patterns techniques uniquement
- Outils : `presidio` (Microsoft) ou regex maison

### Droit du client

- **Droit accès** : copie complète des données dans les 30 j de demande
- **Droit suppression** : suppression complète dans les 30 j de demande (sauf obligations légales)
- **Droit portabilité** : export JSON / CSV
- **Notifier breach** : dans les 72 h (PDPA SG + RGPD)

### Localisation données

- Par défaut : **Singapour** ou **EU** (selon préférence client)
- Pas de transfert hors région sans consent explicite
- Cloudflare R2 : multi-region, accepter selon DPA
- LLM providers : prioriser data residency garantie (Azure OpenAI SG / EU)

## Conséquences

### Positives
- Conformité PDPA SG + RGPD + futures lois SG IA
- Confiance client (clause contractuelle)
- Réduit blast radius en cas d'incident sécu

### Négatives
- Overhead ops (snapshots par client, vaults séparés)
- Mitigation : automatisation Phase 5 (IDP)

## Sources

- Singapore PDPA (Personal Data Protection Act 2012, rev. 2020)
- RGPD (Règlement UE 2016/679)
- ISO 27001 A.8 (Asset Management)
- NIST SP 800-88 (Media Sanitization)
