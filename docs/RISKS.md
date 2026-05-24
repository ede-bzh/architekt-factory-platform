# Architekt — Registre des risques (révision globale)

> 25 risques identifiés à date (2026-05-24, révisé pour scope global APAC + MENA + EMEA + USA).
> Revu à chaque fin de phase, chaque trimestre, et à chaque incident.

## Légende

- **Gravité** : Critique / Haute / Moyenne / Basse
- **Probabilité** : Élevée / Moyenne / Basse
- **Priorité** = Gravité × Probabilité (P1 = action immédiate, P4 = surveillance)

## Vue d'ensemble

| # | Risque | Gravité | Probabilité | Priorité | Owner |
|---|--------|---------|-------------|----------|-------|
| R1 | Pas de pipeline commercial | **Critique** | Élevée | **P1** | CPO |
| R2 | Delivery non rentable (marge < 50 %) | **Critique** | Élevée | **P1** | CPO + CTO |
| R3 | Coût LLM invisible / dérive | Haute | Élevée | **P1** | CTO |
| R4 | Code fragile (DORA 2025 amplificateur) | Haute | Moyenne | P2 | CTO |
| R5 | Trop de stacks trop tôt | Haute | Élevée | **P1** | CTO |
| R6 | Sécurité insuffisante B2B / refus client enterprise | Haute | Moyenne | P2 | CTO |
| R7 | Confusion agence vs SaaS prématuré | Haute | Moyenne | P2 | CPO |
| R8 | Fondateurs surchargés (2 personnes) | Haute | Élevée | **P1** | CPO + CTO |
| R9 | Site vitrine sans preuve | Moyenne | Moyenne | P3 | CPO |
| R10 | Design system non gouverné (a11y non vérifié) | Moyenne | Moyenne | P3 | Designer |
| R11 | Conflit licence (AGPL vs SaaS revente) | Haute | Basse | P2 | CTO + avocat |
| R12 | Dépendance LLM single-provider | Moyenne | Moyenne | P3 | CTO |
| R13 | PDPA / RGPD non conforme client régulé | Haute | Basse | P2 | CTO + DPO externe |
| R14 | Hetzner indisponibilité (single VM) | Moyenne | Basse | P3 | SRE |
| R15 | Marque "Architekt" confondue | Basse | Moyenne | P4 | Designer |
| R16 | Concurrence Devin / Factory / Lovable | Moyenne | Élevée | P2 | CPO |
| R17 | Mauvaise interprétation IMDA NAIIP eligibility | Moyenne | Moyenne | P3 | CPO |
| R18 | Sync La Poste casse pendant rebrand | Moyenne | Moyenne | P3 | CTO |
| R19 | Mutation testing devient théâtre qualité | Moyenne | Moyenne | P3 | CTO |
| R20 | Agents IA traitent données sensibles client sans consent | Haute | Basse | P2 | CISO |
| **R21** | **Régional compliance manqué (UAE PDPL, Saudi SDAIA, GDPR SCC)** | **Haute** | **Moyenne** | **P2** | CTO + legal |
| **R22** | **i18n / RTL bâclé sur projets MENA → refus client** | Haute | Moyenne | P2 | Designer + CTO |
| **R23** | **Data residency violation (transfert non autorisé)** | **Critique** | Basse | **P2** | CTO + DPO |
| **R24** | **Acceptation projet régulé sans capacité** | **Critique** | Moyenne | **P1** | CPO + CTO |
| **R25** | **Pas de listing IMDA pre-approved → perte avantage local** | Moyenne | Moyenne | P3 | CPO |

## Détails des risques globaux (nouveaux)

### R21 — Régional compliance manqué

**Description** : Architekt accepte projet UAE/KSA/EU sans intégrer correctement UAE PDPL, Saudi PDPL (SDAIA), ou GDPR SCC pour transferts. Risque amende ou résiliation contrat.

**Indicateur** : projets avec DPA région-spécifique vs sans.

**Mitigation** :
- INTAKE.md section 5 obligatoire (compliance assumptions)
- 4 templates DPA (SG, UAE, EU, US) dans legal pack
- Conseil juridique consulté pour nouveau pays
- ADR-032 (regional compliance matrix)
- COMPLIANCE.md à charger en skill `architekt-compliance.md`

**Trigger escalade** : 1 projet sans DPA approprié → audit immédiat + correctif.

### R22 — i18n / RTL bâclé MENA

**Description** : Projet pour client UAE/KSA livré sans RTL correct, sans fonts Arabe, layout cassé. Refus client + perte réputation MENA.

**Indicateur** : projets MENA avec axe-core a11y + RTL test pass.

**Mitigation** :
- I18N.md doctrine + checklist obligatoire MENA
- UX-REGIONAL.md section MENA
- Tests Playwright avec snapshot per-locale (LTR + RTL)
- Designer + dev formés Arabe + RTL (Phase 5)
- Refus projet MENA si équipe pas prête (Phase 4)

### R23 — Data residency violation

**Description** : Donnée client UAE stockée en US par défaut Cloudflare, sans review. Violation contractuelle + risque légal.

**Indicateur** : audit hébergement par client.

**Mitigation** :
- ADR-035 (data residency decision model)
- INTAKE.md section 5 + 6 obligatoires
- COMPLIANCE.md matrice par région
- Cloudflare data localization plans pour clients sensibles
- Audit annuel hébergement (cf. ADR-018)

**Trigger escalade** : Critique — incident immédiat = freeze deploys + revue.

### R24 — Acceptation projet régulé sans capacité

**Description** : Client healthcare US (HIPAA), banque licenciée, gouvernement signé sans capacité interne. Risque pénal + amendes énormes.

**Indicateur** : projets acceptés avec niveau sécu L3 sans toutes les capacités requises.

**Mitigation** :
- INTAKE.md critères refus systématique
- ADR-041 (regulated industry entry criteria)
- ADR-009 (internal platform before SaaS) — pas de capacité = pas de projet
- Refus systématique tant que pentest récent + ISO 27001 prerequisites pas en place
- Anti-clients dans CLIENTS.md

**Trigger escalade** : Critique — toute exception nécessite double validation CPO+CTO+legal.

### R25 — Pas de listing IMDA pre-approved vendor

**Description** : Architekt rate la fenêtre IMDA NAIIP/DEB → perd avantage compétitif local (subventions clients).

**Indicateur** : statut candidature IMDA.

**Mitigation** :
- Candidature dès Phase 3 (site Architekt + 1 case study + entité SG opérationnelle)
- Suivi process IMDA mensuel
- Backup plan si refus (autres canaux SG)

## Risques régionaux par marché

### Risques spécifiques APAC

- Concurrence locale forte agences SG (Applify, Kryst, SleekDigital) → différenciation Quality Report
- LINE/WeChat intégrations attendues mais pas dans skills par défaut
- Hong Kong et China : restrictions LLM provider (Anthropic non disponible) → avoir Azure SEA fallback

### Risques spécifiques MENA

- Cycle de vente long (3-6 mois souvent) → cashflow à anticiper
- Relation personnelle critique → présence physique attendue à terme
- Sharia compliance pour finance (KSA) → refuser secteur si pas équipé
- Données féminines : sensibilité culturelle (KSA)

### Risques spécifiques EMEA

- GDPR enforcement augmentée 2025-2026 → DPO externe quasi-obligatoire dès Phase 5
- Accessibility EU EAA 2025 → projets EU doivent être AA strict
- Multi-langue often attendu (FR, DE, NL en plus EN) → coût i18n

### Risques spécifiques USA

- SOC2-ready expectation → préparation 6-12 mois avant premier client US enterprise
- State privacy patchwork → suivre CCPA strict par défaut
- Coût LLM USD plus élevé → marge dégradée si pas tracé
- Litigation culture → MSA solide obligatoire, avocat US à contractualiser

## Process de revue (révisé)

- **Hebdo** (15 min) : check R1, R2, R3, R5, R8 (les 5 P1)
- **Fin de phase** : revue complète + nouveaux risques + ajustement
- **Trimestrielle** : revue + retrait/ajout/dé-priorisation
- **Sur incident** : ajout immédiat + post-mortem + action correctives trackées

## Issues GitHub liées

Chaque risque P1 et P2 sécurité/compliance a un issue tracker `risk:*` ouvert en permanence (cf. `.github/labels.yml`).
