# ADR-032 : Regional compliance matrix

- **Statut** : Proposé
- **Date** : 2026-05-24
- **Décideurs** : CTO, CISO, conseil juridique externe

## Contexte

Architekt opère dans 4 régions (APAC, MENA, EMEA, USA). Chaque région a son cadre réglementaire. Sans matrice claire, risque non-conformité + refus client + amendes.

## Décision

**Matrice de compliance officielle** par région (cf. `docs/COMPLIANCE.md`) :

| Région | Cadre baseline | Hébergement défaut | DPA | Cross-border |
|--------|----------------|--------------------|-----|--------------|
| **APAC SG** | PDPA SG | Singapore | Obligatoire | Protections équivalentes |
| **MENA UAE** | UAE PDPL | UAE | Obligatoire | Restrictif |
| **MENA KSA** | Saudi PDPL (SDAIA) | KSA fortement préféré | Obligatoire | **Très restrictif** |
| **EMEA** | GDPR | EU | Obligatoire | SCC + TIA |
| **USA** | CCPA + SOC2-ready | US | Souhaité | Selon état |

### Process intake

1. INTAKE.md section 5 obligatoire
2. Choix template DPA correspondant (4 templates : SG, UAE, EU, US)
3. Hébergement aligné (ADR-017 + ADR-035)
4. Sub-processor list maintenue

### Quand escalader (avocat / DPO)

- Premier projet dans nouvelle juridiction
- Données secteur régulé (santé, finance, gouvernement)
- Données mineurs
- Transfert cross-border non standard
- Demande client modifier DPA template

## Conséquences

### Positives
- Conformité dès l'intake (pas à la livraison)
- 4 templates DPA = 80 % des cas couverts
- Confiance client B2B

### Négatives
- Setup initial (4 DPA templates + revue avocat) ~5-10 j
- Coût avocat externe récurrent

## Sources
- Singapore PDPC
- UAE Federal Decree-Law 45/2021
- Saudi PDPL (SDAIA 2021, révisé 2023)
- GDPR + EDPB guidelines
- CCPA + CPRA
- `docs/COMPLIANCE.md`
