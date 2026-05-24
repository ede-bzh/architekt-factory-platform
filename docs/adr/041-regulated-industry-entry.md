# ADR-041 : Regulated industry entry criteria

- **Statut** : Proposé
- **Date** : 2026-05-24
- **Décideurs** : CPO, CTO, CISO, legal

## Contexte

Architekt peut être tenté d'accepter projets santé, finance, gouvernement (gros tickets) sans la capacité sécurité / compliance / juridique. Risque pénal et amendes énormes.

## Décision

**Architekt refuse les secteurs régulés tant que les prérequis ne sont pas remplis.**

### Secteurs régulés concernés

| Secteur | Cadre | Statut Architekt actuel |
|---------|-------|--------------------------|
| Healthcare régulé (HIPAA, MDR, dispositifs médicaux) | HIPAA US, MDR EU, etc. | **Refusé** jusqu'à équipe outillée |
| Banque / paiement licencié (MAS SG, FCA UK, etc.) | Cadres bancaires nationaux | **Refusé** |
| Insurance régulée | Cadres assurance nationaux | **Refusé** |
| Gouvernement défense / classifié | Classifications nationales | **Refusé** |
| Gambling / paris | Licences gambling nationales | **Refusé** |
| Crypto / DeFi / token launches | Cadres MiCA, SEC, MAS, etc. | **Refusé** |

### Conditionnellement acceptables (avec prérequis)

| Secteur | Quand accepter |
|---------|----------------|
| Healthcare wellness (non régulé) | Phase 4 OK (L2 sécu suffit) |
| Education K-12 | Phase 5+ (COPPA US, mineurs) |
| Government-adjacent (vendor public sector) | Phase 6+ après ISO 27001 direction maturité (ADR-040) |
| Finance non régulé (fintech adjacent, comptabilité) | Phase 4+ avec L2 sécu |

### Prérequis pour ouvrir un secteur régulé

1. **Equipe dédiée compétente** (1 personne minimum avec expérience secteur)
2. **Budget compliance** (avocat + DPO + auditeur)
3. **Baseline sécu mature** (ADR-040 : ISO 27001 direction maturité minimum)
4. **Pentest récent** (< 12 mois)
5. **Insurance E&O** (Erreurs & Omissions) + Cyber insurance
6. **MSA spécifique secteur** (clauses dédiées)

### Process

Toute demande projet secteur régulé :

1. Réflexe initial : refus poli + referral
2. Si très grosse opportunité → revue CPO + CTO + legal
3. Évaluation prérequis : tous OK ?
4. Si oui : pricing premium (3-5× tarif normal pour absorber risque)
5. Si non : refus définitif, documenter dans CRM

## Conséquences

### Positives
- Évite risque pénal / amendes / réputation
- Force la discipline équipe (vs FOMO)
- Permet montée en maturité avant exposition

### Négatives
- Manque opportunités (acceptable)
- Mitigation : pipeline secteurs non régulés volumineux

## Sources
- HIPAA, MDR (EU), MiCA, MAS, FCA, SEC
- `docs/CLIENTS.md` (anti-clients)
- ADR-040 Enterprise readiness path
