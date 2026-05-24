# ADR-015 : Quality report as commercial artifact

- **Statut** : Proposé
- **Date** : 2026-05-24
- **Décideurs** : CPO, CTO, PMM

## Contexte

Une agence digitale classique livre du code + de la doc. Architekt peut différencier en livrant **systématiquement** un **rapport qualité automatisé** qui prouve la rigueur de la méthode.

## Décision

**Chaque projet Architekt livre un Quality Report.**

### Contenu standard du Quality Report

```
1. Executive Summary (1 page)
2. DORA Metrics
   - Deployment Frequency
   - Lead Time for Changes
   - Change Failure Rate
   - Mean Time To Recovery
3. Quality Dimensions (10, scorecard)
   - Complexity, Coverage UT/E2E, Security, A11y, Performance,
     Documentation, Architecture, Maintainability, Adversarial
4. Test Results
   - Unit tests pass rate
   - Mutation testing score (modules critiques)
   - E2E tests pass rate
5. Security
   - SAST findings (résolus / restants)
   - SCA vulnerabilities
   - SBOM CycloneDX (annexe)
6. Performance
   - Lighthouse scores (perf, a11y, SEO, best practices)
   - p95 latency back-end
7. Accessibility
   - axe-core results
   - WCAG 2.2 AA conformance level
8. Architecture
   - C4 diagrams (Context + Container)
   - ADR list
9. Operational Readiness
   - Runbook checklist
   - Backup/restore tested
   - Monitoring alerts configured
10. Recommendations Roadmap (3/6/12 mois)
```

### Format

- **PDF** : version client (généré par plateforme à la fin de mission)
- **Markdown** : version repo (long-form, versionné)
- **JSON** : version machine (intégrable dans dashboards client)
- **Dashboard live** : `clients.architekt.*/projects/{id}/quality` (Phase 6)

### Pricing

- Inclus dans **toutes les offres** (Launch, MVP, Internal Tool, AI Workflow, Audit)
- Pour offre Audit : c'est **le livrable principal**

### Démo publique

- Le site Architekt expose un Quality Report sur le projet pilote (`architekt.*/proof/quality`)
- Sert de preuve commerciale (cf. Phase 3)

## Conséquences

### Positives
- Différenciation forte vs agences classiques
- Argument vente B2B (CTO client peut auditer)
- Réduit risque litige (preuve de qualité)
- Marketing self-generated (case studies réels)

### Négatives
- Effort initial (3-5 j) pour template + génération automatique (Phase 5)
- Doit rester honnête (mauvais score = bonne occasion de pédagogie)

## Sources

- DORA metrics (DORA 2024, 2025)
- ISO/IEC 25010 (Software Quality Model)
- NIST CSF (Cybersecurity Framework) — pour section sécurité
