---
name: Architekt Compliance
description: Doctrine compliance régionale Architekt (GDPR, PDPA SG, UAE/Saudi PDPL, CCPA, SOC2-ready)
tags: [compliance, architekt, gdpr, pdpa]
metadata:
  category: compliance
  triggers: [intake, hosting, vendor, personal-data, dpa]
---

# Architekt Compliance


## Objectif

Encoder la **doctrine compliance régionale Architekt** (GDPR, PDPA SG, UAE/Saudi PDPL, CCPA, SOC2-ready) pour que tout agent travaillant sur un projet international applique les bonnes pratiques.

## Quand utiliser

- À l'intake d'un nouveau projet (section 5 INTAKE.md)
- Lors du choix d'hébergement (ADR projet)
- Lors d'intégration vendor / sub-processor
- Lors d'envoi d'email transactionnel client
- Lors de stockage / traitement données personnelles

## Cadres baseline par région

| Région | Cadre principal |
|--------|-----------------|
| Singapore | **PDPA SG** + DPO + sub-processor list + cross-border équivalence |
| UAE | **UAE PDPL** + DPA + RTL/Arabe |
| Saudi Arabia | **Saudi PDPL (SDAIA)** + localisation forte + cross-border autorisation |
| EU | **GDPR** + DPA + SCC + TIA + droits sujets |
| UK | UK GDPR + DPA 2018 + ICO |
| USA | **CCPA + SOC2-ready** + state laws (HIPAA si santé régulée seulement) |

cf. `docs/COMPLIANCE.md` pour détails.

## Règles d'application

### Au démarrage projet

1. Identifier juridictions client + utilisateurs finaux
2. Sélectionner template DPA approprié (4 templates : SG, UAE, EU, US)
3. Documenter dans ADR projet : data residency, sub-processors, retention
4. Si juridiction nouvelle pour Architekt → escalade conseil juridique

### Pendant build

- Mécanisme export / suppression données (GDPR Article 15, 17, 20)
- Cookie consent banner si analytics > strictly necessary (ePrivacy EU)
- Encryption at rest + in transit
- Audit logs (cf. ADR-019)
- Sub-processor list maintenue
- Breach notification runbook (72h GDPR / PDPL)

### Données mineurs

- COPPA (US, < 13 ans)
- GDPR Article 8 (UE, < 16 ans selon État)
- Consent parental obligatoire
- Refus traitement marketing direct

### Cross-border transfers

| Cas | Mécanisme |
|-----|-----------|
| EU → US | SCC + TIA (Schrems II) + DPF si applicable |
| EU → Singapore | SCC + adequacy partielle |
| UAE → tiers | Restriction selon catégorie |
| KSA → tiers (hors GCC) | Autorisation SDAIA |

### Conservation données

| Type | Rétention par défaut |
|------|---------------------|
| Code client | Durée contrat + 90 j |
| Données fonctionnelles | Selon contrat (3-7 ans typique) |
| Logs avec data client | 90 jours, puis anonymisation |
| Traces LLM | 30 j puis anonymisation |
| Backups | 90 j rolling |
| Factures/contrats | 7 ans (obligation SG) |

cf. ADR-018.

## Quand escalader

- Nouveau pays / juridiction
- Données secteur régulé (santé, finance, gouv)
- Données mineurs
- Demande client modifier DPA template
- Incident security ayant fuité données

→ Conseil juridique + DPO externe

## Anti-patterns

- ❌ "On verra plus tard"
- ❌ Choisir hébergement sans data residency review
- ❌ Vendor ajouté sans DPA + évaluation
- ❌ Logs centralisés cross-region sans review
- ❌ Cookie banner "Accept all" non conforme GDPR
- ❌ Politique privacy générique "made in US" sur site UE
- ❌ Email marketing avant consent vérifié

## Sources

- ADR-032 Regional compliance matrix
- ADR-035 Data residency decision model
- ADR-013 Client IP and AI-generated code policy
- `docs/COMPLIANCE.md`
- Singapore PDPC ([pdpc.gov.sg](https://pdpc.gov.sg))
- UAE Federal Decree-Law 45/2021
- Saudi PDPL ([sdaia.gov.sa](https://sdaia.gov.sa))
- GDPR + EDPB guidelines
- CCPA + CPRA
- Schrems II (CJEU C-311/18)
