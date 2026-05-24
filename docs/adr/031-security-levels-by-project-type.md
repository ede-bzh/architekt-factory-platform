# ADR-031 : Security levels by project type

- **Statut** : Proposé
- **Date** : 2026-05-24
- **Décideurs** : CTO, CISO

## Contexte

Tous les projets n'ont pas le même niveau de sensibilité. Un site marketing n'a pas besoin du même niveau de sécurité qu'un portail RH. Sans niveau par défaut, sur-investissement ou sous-investissement systématique.

## Décision

**4 niveaux de sécurité** (cf. `docs/SECURITY.md`) :

| Niveau | Description | Contrôles requis |
|--------|-------------|------------------|
| **L0** | Public static (marketing) | Secure headers, dependency scanning, form protection |
| **L1** | Standard business app | + auth, RBAC, audit logs, SAST/SCA, backups, ASVS L1 |
| **L2** | Sensitive business data | + encryption at rest, access reviews, security logging, retention policy, DPIA-light, IR playbook |
| **L3** | Regulated / enterprise | + ASVS L2/L3, threat model formel, pentest externe, vendor risk review, data residency, compliance review |

### Mapping par projet (par défaut, override possible)

| Projet | Niveau | Override possible |
|--------|--------|-------------------|
| A. Marketing | L0 | L1 si lead capture |
| B. MVP | L1 | L2 si B2B |
| C. Internal tool | L1 | L2 si RH/finance |
| D. AI workflow | L1 | L2 si données client |
| E. E-commerce | L1 | L2 si paiement custom |
| F. CMS | L0 | L1 si auth contributeurs |
| G. **Client portal** | **L2** | L3 si régulé |
| H. Dashboard | L1 | L2 si données agrégées clients |
| I. Modernization | L2 | L3 si régulé |
| J. Audit | Advisory | — |

## Conséquences

### Positives
- Effort sécu proportionné au risque
- Pricing par niveau possible (L3 = premium)
- Refus L3 si Architekt pas prêt (ADR-041)

### Négatives
- Choix initial peut être incorrect → revue à mi-projet

## Sources
- OWASP ASVS v5
- NIST SP 800-53 RA-2 (Information Categorization)
- `docs/SECURITY.md`
