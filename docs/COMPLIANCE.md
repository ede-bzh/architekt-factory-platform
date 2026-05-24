# Architekt — Matrice de compliance régionale

> Cadres réglementaires par région et leur impact sur l'architecture / les contrats.
> Référence : ADR-032 (regional compliance matrix), ADR-035 (data residency).

## Doctrine

> **Compliance = contrainte d'entrée**. Identifier dès le devis. Pas de "on verra plus tard".
> Architekt **ne joue pas** au cabinet d'avocats — on s'aligne sur des baselines connues + on escalade à conseil juridique si seuil dépassé.

## APAC

### Singapore PDPA (cible primaire Architekt)

| Aspect | Implication |
|--------|-------------|
| Consent obligation | Recueillir consent explicite pour collecte/usage |
| Notification obligation | Informer scope, finalité, destinataires |
| Purpose limitation | Usage limité au consent donné |
| Access & correction | Sujet peut demander accès + correction |
| Data protection (reasonable) | Mesures techniques et organisationnelles "reasonable" |
| Retention limitation | Conserver pas plus que nécessaire |
| DPO obligation | Désignation Data Protection Officer obligatoire |
| Cross-border transfer | Notification + protections équivalentes requises |

**Impact architecture** :
- ✅ **Hébergement Singapore par défaut** pour clients SG
- ✅ Liste processor/subprocessor claire dans DPA
- ✅ Mécanisme d'export / suppression des données
- ✅ Logs anonymisés (cf. ADR-018)

**Risques** : amendes jusqu'à 1M SGD ou 10 % turnover.

### Autres APAC (référentiel)

| Pays | Cadre | Particularité |
|------|-------|---------------|
| Malaisie | PDPA 2010 (révision 2024) | Notification breach 72h |
| Indonésie | UU PDP (2022) | Localisation possible pour certaines catégories |
| Thaïlande | PDPA 2019 | Aligné GDPR, DPIA possible |
| Vietnam | Decree 13/2023 | Localisation pour données sensibles |
| Australia | Privacy Act + APP | Notification breach obligatoire |
| Japon | APPI | Cross-border restreint |
| Corée du Sud | PIPA | Strict, consent granulaire |

## MENA

### UAE PDPL (Federal Decree-Law 45/2021)

| Aspect | Implication |
|--------|-------------|
| Consent | Obligatoire, granulaire |
| Data subject rights | Accès, rectification, suppression, portabilité |
| Cross-border transfers | Restrictions, mécanismes spécifiques |
| DPO | Obligatoire selon échelle |
| Data residency | **Souvent attendue UAE** pour secteurs sensibles |

**Impact architecture** :
- ✅ Option hébergement UAE (AWS Bahrain / Azure UAE / G42 Cloud)
- ✅ DPA spécifique UAE
- ✅ Support RTL + Arabe localisation
- ✅ Review transfert renforcée

### Saudi Arabia PDPL (2021, révisé 2023)

| Aspect | Implication |
|--------|-------------|
| Régulateur | **SDAIA** (Saudi Data and AI Authority) |
| Consent | Granulaire |
| Cross-border | **Restrictif** — autorisation SDAIA requise hors GCC |
| Localisation données | Forte attente local |
| DPO | Obligatoire |

**Impact architecture** :
- ✅ Hébergement KSA fortement recommandé (STC Cloud, Mobily, AWS région KSA quand disponible)
- ✅ Localisation Arabe obligatoire pour interfaces publiques
- ✅ Conformité Sharia pour secteur finance

### Autres MENA

| Pays | Cadre |
|------|-------|
| Qatar | DPL 2016 |
| Bahrain | PDPL 2018 |
| Egypt | DPL 151/2020 |
| Maroc | Loi 09-08 |
| Tunisie | Loi 63/2004 |
| Israël | Privacy Protection Law |

## EMEA

### GDPR (UE)

| Aspect | Implication |
|--------|-------------|
| Lawful basis | Identifier (consent, contract, legitimate interest, etc.) |
| DPA | Obligatoire client ↔ Architekt si Architekt = processor |
| International transfer | **SCC (Standard Contractual Clauses)** + TIA (Transfer Impact Assessment) |
| Data minimization | Collecter le strict nécessaire |
| Right to deletion/export | Mécanisme technique obligatoire |
| Breach notification | Sous 72h à l'autorité |
| DPO | Obligatoire selon scope |
| DPIA | Obligatoire pour traitement à risque élevé |

**Impact architecture** :
- ✅ **EU hosting par défaut** pour clients EU (AWS eu-west-1, Azure West Europe, Hetzner FSN)
- ✅ Stockage données EU par défaut
- ✅ Review SCC/DPA avant tout traitement cross-border
- ✅ Mécanismes droit accès / portabilité / suppression
- ✅ Cookie consent banner (ePrivacy)

**Risques** : amendes jusqu'à 4 % CA mondial ou 20 M €.

### UK GDPR + DPA 2018

- Aligné GDPR avec quelques spécificités UK
- ICO comme régulateur
- TIA spécifique post-Brexit

### Suisse — LPD révisée 2023

- Aligné mais pas identique GDPR
- FDPIC comme régulateur

## USA

### SOC2-ready (attente B2B enterprise)

Pas une loi, mais **attente marché** pour vendeurs SaaS B2B aux USA.

| Critère SOC2 | Architekt préparation |
|--------------|----------------------|
| Security | OWASP ASVS + SBOM + audit logs |
| Availability | SLO documenté, incident response |
| Processing integrity | Audit trail agents (ADR-019) |
| Confidentiality | Data classification + encryption |
| Privacy | Cf. CCPA / state laws |

**SOC2 Type I** = audit point-in-time, ~6 mois prep.
**SOC2 Type II** = audit 6-12 mois ops, ~12 mois prep.

### State privacy laws

| État | Loi |
|------|-----|
| California | **CCPA + CPRA** (le plus strict, modèle de référence) |
| Colorado | CPA |
| Connecticut | CTDPA |
| Virginia | VCDPA |
| Utah | UCPA |
| + 15 autres états | Patchwork en évolution rapide |

**Architekt** : aligner sur CCPA par défaut (le plus strict).

### HIPAA (santé US)

| Aspect | Implication |
|--------|-------------|
| **Quand applicable** | Si données santé US, sinon non |
| BAA | Business Associate Agreement obligatoire |
| Encryption | At rest + in transit obligatoire |
| Audit logs | Obligatoires + rétention 6 ans |

**Architekt** : **refuser projets HIPAA** jusqu'à équipe outillée (cf. ADR-041).

### Autres USA-relevant

- **GLBA** (finance)
- **FERPA** (éducation)
- **COPPA** (enfants < 13 ans)
- **Section 508** (accessibilité gouvernement)

## Matrice résumée

| Région | Cadre baseline | Hébergement par défaut | DPA | Cross-border |
|--------|----------------|------------------------|-----|--------------|
| **APAC SG** | PDPA SG | Singapore | Obligatoire | Protections équivalentes |
| **MENA UAE** | UAE PDPL | UAE | Obligatoire | Restrictif |
| **MENA KSA** | Saudi PDPL (SDAIA) | KSA strongly preferred | Obligatoire | **Très restrictif** |
| **EMEA** | GDPR | EU | Obligatoire | SCC + TIA |
| **USA** | CCPA + SOC2-ready | US | Souhaité | Selon état |

## Process Architekt par projet

1. **Intake** : identifier région client + nature données
2. **DPA template** par juridiction (4 templates : SG, UAE, EU, US)
3. **Hébergement** : choix selon ADR-017 + matrice ci-dessus
4. **Sub-processor list** : maintenue par projet
5. **Breach notification** : runbook prêt par projet
6. **Annual review** : DPA + sub-processor list

## Quand escalader à un avocat / DPO externe

- Premier projet dans une nouvelle juridiction
- Données secteur régulé (santé, finance, gouvernement)
- Données mineurs
- Transfert cross-border non standard
- Demande client de modifier DPA template
- Incident security ayant fuité données

**Réseau Architekt** : 1 avocat SG (Phase 0), 1 DPO externe à mettre en place Phase 4+.

## Sources

- Singapore PDPC ([pdpc.gov.sg](https://pdpc.gov.sg))
- UAE PDPL ([Federal Decree-Law 45/2021](https://uaegisre.uae/))
- Saudi PDPL ([sdaia.gov.sa](https://sdaia.gov.sa))
- GDPR ([gdpr-info.eu](https://gdpr-info.eu)) + EDPB guidelines
- ICO UK ([ico.org.uk](https://ico.org.uk))
- CCPA ([oag.ca.gov/privacy/ccpa](https://oag.ca.gov/privacy/ccpa))
- SOC2 / AICPA TSC
