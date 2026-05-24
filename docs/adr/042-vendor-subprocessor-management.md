# ADR-042 : Vendor / subprocessor management

- **Statut** : Proposé
- **Date** : 2026-05-24
- **Décideurs** : CTO, CISO, legal

## Contexte

Chaque projet Architekt utilise des vendors (LLM, hébergement, monitoring, payment, etc.). Sans gestion formelle, risque non-conformité GDPR (Article 28 sub-processors), incident sécu sur chaîne, fuite données via vendor.

## Décision

**Liste de sub-processors maintenue par projet** + évaluation initiale + revue annuelle.

### Process onboarding vendor

| Étape | Action |
|-------|--------|
| 1. Identification besoin | Pourquoi ce vendor ? Alternative ? |
| 2. Évaluation initiale | Certifications (SOC2, ISO 27001), juridiction, DPA |
| 3. Data access | Quelles données accessibles ? Granularité ? |
| 4. DPA signed | Si données personnelles |
| 5. Documentation | `<projet>/docs/security/subprocessors.md` |
| 6. Notification client | Si Architekt = processor, client doit consentir |

### Critères évaluation

| Critère | Niveau acceptable |
|---------|-------------------|
| Certifications | SOC2 Type II ou ISO 27001 (idéalement) |
| Juridiction | Compatible compliance projet (cf. ADR-035) |
| DPA disponible | Oui |
| Breach notification SLA | < 72 h |
| Encryption at rest | Oui (AES-256 minimum) |
| Encryption in transit | Oui (TLS 1.2+) |
| Audit logs | Disponibles client |
| Réputation | Pas d'incident majeur récent |

### Vendors typiques Architekt + statut

| Vendor | Usage | Évaluation |
|--------|-------|-----------|
| **LLM providers** | | |
| Anthropic | LLM | SOC2, data residency US/EU |
| OpenAI / Azure OpenAI | LLM | Azure = SOC2 + EU/SG region |
| MiniMax | LLM (China) | **Attention** juridiction Chine |
| **Hébergement** | | |
| Cloudflare | CDN, Pages, R2 | SOC2, data residency partielle |
| Hetzner | VPS | ISO 27001, juridiction DE |
| AWS | Tout | SOC2, multi-region |
| Azure | Tout | SOC2, multi-region |
| Fly.io | App hosting | SOC2 |
| **DB/Storage** | | |
| Supabase | PostgreSQL | SOC2 |
| Neon | PostgreSQL | SOC2 |
| Cloudflare R2 | Object storage | SOC2 |
| **Monitoring** | | |
| Sentry | Errors | SOC2 |
| Plausible | Analytics | EU only |
| Better Stack | Logs + uptime | SOC2 |
| **Auth** | | |
| Clerk | Auth as a service | SOC2 |
| Auth0 | Auth as a service | SOC2, ISO 27001 |

### Revue annuelle

Chaque projet : revue sub-processors annuelle

- Certifications encore valides ?
- Incident récent ?
- Nouveau vendor ajouté ?
- Notifier client si changement majeur

## Conséquences

### Positives
- Conformité GDPR Article 28
- Réduction surface attaque supply chain
- Argument vente B2B (transparence)

### Négatives
- Process à maintenir
- Mitigation : template subprocessors.md + revue annuelle calendée

## Sources
- GDPR Article 28 (Processor)
- ISO/IEC 27001:2022 A.5.19-A.5.23 (Supplier relationships)
- ADR-018 Data retention and client isolation
