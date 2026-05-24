# ADR-040 : Enterprise readiness path — ISO 27001 / SOC2-ready

- **Statut** : Proposé
- **Date** : 2026-05-24
- **Décideurs** : CTO, CISO

## Contexte

Clients enterprise B2B (US scale-ups, EU corporates, MENA gouvernement-adjacent) exigent souvent une posture sécurité formelle (SOC2, ISO 27001). Sans direction de maturité, on bloque à 30k SGD/projet.

## Décision

**ISO 27001 et SOC2 sont traités comme directions de maturité, pas certifications promises.**

### Phasage maturité

| Phase | Maturité |
|-------|----------|
| Phase 0-2 | Documentation + ADR sécurité + baseline tools |
| Phase 3 | CI sécurité opérationnelle (SAST + SCA + secret scan + SBOM) |
| Phase 4 | Premiers projets L1-L2 livrés, incident response testée |
| Phase 5 | IDP intègre sécurité automatique (vault, RBAC, audit) |
| **Phase 6 (5 clients+)** | **ISO 27001 direction de maturité formalisée** (gap analysis, ISMS draft, contrôles techniques alignés) |
| **Phase 7 (10 clients+)** | **SOC2-ready** si productisation SaaS choisie |
| Phase 8+ | Certification ISO 27001 ou SOC2 Type I si justifié par clients |

### Investissement nécessaire (estimation)

| Étape | Effort | Coût externe |
|-------|--------|--------------|
| Gap analysis ISO 27001 | 5-10 j | 5-10k SGD (auditeur) |
| Implémentation ISMS | 30-60 j | 10-30k SGD (consultant) |
| Pre-audit ISO 27001 | 5 j | 5-10k SGD |
| Audit certification | 5-10 j | 10-30k SGD (organisme accrédité) |
| Maintenance annuelle | 10 j/an | 5-15k SGD/an (surveillance) |

### Anti-patterns

- ❌ Vendre "ISO 27001 certifié" tant qu'on ne l'est pas
- ❌ Faire la doc sans implémenter
- ❌ Faire la certif sans clients qui le demandent (gaspillage)
- ❌ Sous-traiter 100 % à un consultant (mauvaise appropriation)

### Cadrage SOC2

- **SOC2 Type I** = audit point-in-time, ~6 mois prep
- **SOC2 Type II** = audit 6-12 mois ops, ~12 mois prep
- Couvre : Security (obligatoire), Availability, Processing Integrity, Confidentiality, Privacy (optionnels)
- Architekt SOC2 : commencer par Security uniquement

## Conséquences

### Positives
- Débloque clients enterprise (US, EU, gouv-adjacent)
- Posture sécurité réelle (pas marketing)
- Argument vente B2B

### Négatives
- Coût significatif (50-100k SGD investissement initial)
- Charge maintenance annuelle
- Tentation de promettre avant d'avoir → discipline requise

## Sources
- ISO/IEC 27001:2022
- AICPA TSC (Trust Services Criteria) 2017 + 2022
- `docs/SECURITY.md`
- ADR-041 (regulated industry entry)
