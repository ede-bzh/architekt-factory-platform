---
name: Architekt Security
description: Sécurité Architekt — OWASP ASVS, NIST SSDF, SBOM, niveaux L0-L3 (ADR-012, ADR-013, ADR-031)
tags: [security, architekt, asvs, sbom, owasp]
metadata:
  category: security
  triggers: [security, sast, sbom, pentest, asvs, secrets]
---

# Architekt Security

## Objectif

Encoder la **doctrine sécurité Architekt** : niveaux proportionnés, supply chain transparente, SBOM obligatoire — effort sécu = risque réel du projet.

## Quand utiliser

- Classification niveau sécurité à l'intake
- CI pipeline (SAST, SCA, secret scan)
- Phase Hardening / pentest interne
- Réponse questionnaire sécurité client

## 4 niveaux sécurité (ADR-031)

| Niveau | Description | Contrôles clés |
|--------|-------------|----------------|
| **L0** | Site marketing static | Headers sécu, dependency scan, form protection |
| **L1** | App business standard | + auth, RBAC, audit logs, SAST/SCA, backups, ASVS L1 |
| **L2** | Données sensibles | + encryption at rest, access reviews, DPIA-light, IR playbook |
| **L3** | Régulé / enterprise | + ASVS L2/L3, threat model, pentest externe, data residency |

Mapping par défaut : MVP L1, portal L2, marketing L0 — override documenté en ADR projet.

## SBOM & supply chain (ADR-012)

- **SBOM obligatoire** à chaque release — CycloneDX JSON (+ SPDX secondaire)
- Outils : Syft, cyclonedx-py/npm, pip-audit, npm audit
- **SAST** : Bandit (Py), Semgrep (multi)
- **Secret scan** : trufflehog CI + pre-commit
- Lockfiles : versions **exactes** (pas de `^`/`~`)
- Signature release : Cosign (Phase 5+)

## Politique IP & code IA (ADR-013)

- Code livré = **cédé au client** (MSA)
- Refus dépendances **AGPL** sauf accord explicite
- Préférer MIT / Apache-2.0 / BSD / ISC
- `NOTICE.md` licences à la livraison
- Données client jamais pour fine-tuning LLM

## Pipeline CI sécurité (bloquant)

```
lint → tests → bandit/safety → trufflehog → SBOM artifact → deploy gate
```

0 finding **critique** pour go-live.

## Questionnaires client (ADR-045)

Pack standard : SIG-lite, CAIQ, ISO27001 mapping — réponse < 1 jour.
80% réponses depuis pack versionné Git.

## Anti-patterns

- ❌ L3 sur projet marketing (sur-investissement)
- ❌ L0 sur portail RH (sous-investissement)
- ❌ Release sans SBOM
- ❌ Secrets en repo (même "temporaire")
- ❌ AGPL intégré sans revue juridique

## Sources

- ADR-012 SBOM supply-chain baseline
- ADR-013 Client IP and AI-generated code
- ADR-031 Security levels by project type
- ADR-045 Client security questionnaire readiness
- OWASP ASVS v5, NIST SP 800-218 SSDF
