# Architekt — Sécurité baseline et niveaux par projet

> Référence sécurité unique pour Architekt. À lire en complément de ADR-012 (SBOM), ADR-018 (data retention), ADR-019 (audit logs), `skills/architekt-security.md`.
> Cadres alignés : **NIST SSDF SP 800-218**, **OWASP ASVS v5**, **CISA/NTIA SBOM**.

## Baseline sécurité (tous projets)

Chaque projet Architekt **doit inclure** :

| Contrôle | Détail | Outil |
|----------|--------|-------|
| Threat model light | 1 page, STRIDE simplifié | Markdown dans `<projet>/docs/security/threat-model.md` |
| Authentication design | Méthode + flow + recovery | ADR projet |
| Authorization matrix | Rôles × actions × ressources | Markdown ou table DB |
| Secrets management | Vault externe (Doppler/Infisical), pas dans repo | `git-secret-scan` pre-commit |
| Dependency scanning (SCA) | Vuln + licences | Safety, npm audit, OWASP Dependency-Check |
| SAST | Static analysis | Bandit (Python), Semgrep (multi-lang) |
| Secret scanning | Repo + CI | TruffleHog, gitleaks |
| SBOM | À chaque release | CycloneDX (Syft) + SPDX |
| Audit logs (actions sensibles) | Append-only, hash chain | DB table dédiée |
| Backup / restore plan | RPO/RTO documentés | Runbook + test mensuel |
| Vulnerability remediation policy | SLA par sévérité | Documenté `<projet>/docs/security/policy.md` |
| Secure headers | HSTS, CSP, X-Frame-Options, etc. | Middleware (FastAPI/Next) |
| Rate limiting (public endpoints) | Par IP + par token | Plateforme + middleware |
| Least privilege access | Prod = pas d'accès dev | IAM cloud + secrets |
| Production access policy | Qui peut, comment, audit | Documenté + JIT (si possible) |

## 4 niveaux de sécurité par projet

> Choisir le niveau au début du projet, documenter dans ADR projet, appliquer les contrôles correspondants.

### Level 0 — Public static

| | |
|--|--|
| **Exemples** | Site marketing, blog, landing pages |
| **Contrôles requis** | Secure headers, dependency scanning, form protection (anti-bot), no sensitive data stored |
| **Pas requis** | Auth utilisateur, audit logs, encryption at rest, RBAC |
| **Coût additionnel** | Bas |
| **Offres concernées** | Launch |

### Level 1 — Standard business app

| | |
|--|--|
| **Exemples** | Internal tool, portail basique, app sans données critiques |
| **Contrôles requis** | + Auth (Clerk/Auth0/SSO), + RBAC basique, + audit logs, + SAST/SCA en CI, + backups testés, + **OWASP ASVS L1-inspired checklist** |
| **Coût additionnel** | Faible-moyen |
| **Offres concernées** | Internal Tool basique, MVP early-stage |

### Level 2 — Sensitive business data

| | |
|--|--|
| **Exemples** | Client portal, documents financiers, documents RH, données B2B sensibles |
| **Contrôles requis** | + RBAC fin (rôle × ressource), + **encryption at rest** (DB + storage), + access reviews trimestrielles, + security logging structuré, + data retention policy, + **DPIA-style review** (light DPIA), + incident response playbook |
| **Coût additionnel** | Moyen |
| **Offres concernées** | Portal, MVP avec données B2B, Internal Tool avec données client |

### Level 3 — Regulated / enterprise

| | |
|--|--|
| **Exemples** | Healthcare-adjacent, finance-adjacent, government-adjacent |
| **Contrôles requis** | + **OWASP ASVS L2/L3 mapping complet**, + threat model formel STRIDE, + **pentest externe**, + vendor risk review, + data residency stricte, + revue légale/compliance, + SOC2-ready ou ISO 27001 prerequisites |
| **Coût additionnel** | Élevé (5-15k SGD pentest + audit légal) |
| **Contrainte** | **Refuser tant que Architekt n'est pas prêt** (ADR-041) |
| **Offres concernées** | Phase 6+ uniquement, après baseline sécu mature |

## Mapping niveau ↔ type de projet (cf. ADR-031)

| Projet | Niveau par défaut | Override possible |
|--------|-------------------|-------------------|
| A. Marketing/corporate | L0 | L1 si données prospects |
| B. Product MVP | L1 | L2 si données client B2B |
| C. Internal tool | L1 | L2 si données RH/finance |
| D. AI workflow | L1 | L2 si données client |
| E. E-commerce | L1 | L2 si paiement custom |
| F. CMS / content | L0 | L1 si auth contributeurs |
| G. Client portal | **L2** | L3 si secteur régulé |
| H. Data dashboard | L1 | L2 si données client agrégées |
| I. Modernization | L2 | L3 si secteur régulé |
| J. Audit | Advisory | — |

## Outils & process CI sécurité

```yaml
# Extrait .github/workflows/ci-security.yml (Phase 2)
jobs:
  sast:
    runs: bandit / semgrep
  sca:
    runs: safety / npm audit / OWASP Dependency-Check
  secret-scan:
    runs: trufflehog --only-verified
  sbom:
    runs: anchore/sbom-action (CycloneDX)
  container-scan:
    runs: trivy (si Docker)
```

Gate : **CI verte obligatoire avant merge** (cf. Phase 2).

## Incident response (process baseline)

1. **Détection** — alerte monitoring ou report client/agent
2. **Triage** — sévérité P1/P2/P3, lead assigné
3. **Containment** — isoler, freeze deploys
4. **Eradication** — patch, rotate secrets
5. **Recovery** — restore, vérifier
6. **Post-mortem** — blameless, dans 7 jours, actions correctives trackées

Document : `<projet>/docs/security/incident-response.md`

## Vendor / subprocessor management (cf. ADR-042)

Pour chaque vendor utilisé (LLM provider, hébergement, monitoring, etc.) :

- Liste maintenue `<projet>/docs/security/subprocessors.md`
- Évaluation : data access, certifications, juridiction, DPA signée
- Revue annuelle
- Notification client si changement majeur

## Maturité sécurité Architekt — roadmap

| Phase | Maturité visée |
|-------|----------------|
| Phase 0-1 | Documentation + ADR sécurité |
| Phase 2 | CI sécurité opérationnelle (SAST + SCA + secret scan + SBOM) |
| Phase 3 | Pilote site Architekt avec L0 sécu prouvée |
| Phase 4 | Premiers projets L1-L2 livrés, incident response testée |
| Phase 5 | IDP intègre sécurité automatique (vault, RBAC, audit) |
| Phase 6+ | **ISO 27001 direction de maturité** (pas certification promise — cf. ADR-040) |
| Phase 7 | SOC2-ready pour SaaS si choisi |

## Sources

- NIST SP 800-218 SSDF v1.1 (févr. 2022), v1.2 IPD (déc. 2025)
- OWASP ASVS v5
- CISA SBOM Minimum Elements / NTIA SBOM
- ISO/IEC 27001:2022
- OWASP Top 10 2025, OWASP LLM Top 10
- NIST SSDF community profiles
