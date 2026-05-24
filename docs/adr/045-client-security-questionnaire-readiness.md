# ADR-045 : Client security questionnaire readiness

- **Statut** : Proposé
- **Date** : 2026-05-24
- **Décideurs** : CTO, CISO

## Contexte

Les clients enterprise (B2B US, EU, gouv-adjacent) envoient des questionnaires sécurité (SIG, CAIQ, custom). Sans réponse pré-préparée, on perd des deals ou on bâcle (= refus).

## Décision

**Pack "réponses standardisées" maintenu à jour** pour répondre à tout questionnaire sécurité client en < 1 jour.

### Pack contenu

| Document | Contenu |
|----------|---------|
| `docs/security-pack/architekt-security-overview.md` | 2 pages, posture sécurité Architekt |
| `docs/security-pack/sig-lite-answers.md` | Réponses SIG (Standardized Information Gathering) Lite |
| `docs/security-pack/caiq-answers.md` | Réponses CSA CAIQ (Consensus Assessments Initiative Questionnaire) |
| `docs/security-pack/iso27001-controls-mapping.md` | Mapping nos contrôles aux Annexe A ISO 27001 |
| `docs/security-pack/data-flow-diagram.md` | Flow données générique projet Architekt |
| `docs/security-pack/subprocessors-list.md` | Liste vendors avec certifications et juridictions |
| `docs/security-pack/incident-response.md` | Procédure (cf. ADR-043) |
| `docs/security-pack/business-continuity.md` | RPO/RTO + DR plan |
| `docs/security-pack/privacy-policy.md` | Architekt privacy policy |
| `docs/security-pack/aup.md` | Acceptable Use Policy |

### Process client questionnaire

| Étape | Action |
|-------|--------|
| 1. Réception | Triage par CTO (1h) |
| 2. Mapping | Identifier sections couvertes par pack |
| 3. Réponses standard | Coller depuis pack |
| 4. Réponses custom | Rédiger spécifiquement (< 10 % du total) |
| 5. Revue | CISO + CTO valide |
| 6. Envoi | Avec cover letter |
| 7. Tracking | CRM : date envoi, follow-up J+7 |

### Cadres à connaître

- **CSA CAIQ** : Cloud Security Alliance — pour vendors cloud
- **SIG / SIG Lite** : Shared Assessments — banking / finance
- **ISO 27001 Annexe A** : 93 contrôles (mapping)
- **NIST CSF** : Cybersecurity Framework
- **SOC2 TSC** : Trust Services Criteria
- **VSA** : Vendor Security Alliance

### Maintenance

- Revue trimestrielle
- Mise à jour si nouveau contrôle déployé ou vendor changé
- Versioning Git du pack

### Phase d'application

- Phase 3 : pack démarré (5 docs base)
- Phase 4 : pack complet (10 docs)
- Phase 5+ : enrichissement selon retours questionnaires reçus

## Conséquences

### Positives
- Cycle commercial accéléré (réponse en 1 j vs 1-2 sem)
- Démontre maturité (différenciant vs petites agences)
- Argument vente

### Négatives
- Effort initial setup pack (~5-10 j)
- Maintenance trimestrielle
- Mitigation : 80 % deals couverts par 10 docs

## Sources
- CSA CAIQ v4
- Shared Assessments SIG 2024
- ISO/IEC 27001:2022
- NIST CSF 2.0
- AICPA TSC
- `docs/SECURITY.md`, ADR-040, ADR-042
