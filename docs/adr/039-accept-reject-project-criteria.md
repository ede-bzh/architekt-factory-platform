# ADR-039 : Accept / reject project criteria

- **Statut** : Proposé
- **Date** : 2026-05-24
- **Décideurs** : CPO, CTO

## Contexte

Architekt à 2 personnes ne peut pas accepter tout. Sans critères clairs, on dit oui à des projets non rentables, hors scope, à risque légal.

## Décision

**Critères formels accept / reject** (cf. `docs/INTAKE.md`).

### Refus systématique (1 seul suffit)

- ❌ Pas de PO / sponsor identifié côté client
- ❌ Budget < seuil bas de l'offre (-30 %)
- ❌ Délai imposé incompatible avec scope
- ❌ Stack imposée hors Tier A/B (sauf signature Tier C avec premium)
- ❌ Domaine régulé sans budget compliance (santé HIPAA, banque, défense, gambling)
- ❌ Conflit IP / clause AI non négociable
- ❌ Client refuse security gates ou Quality Report
- ❌ Client veut autonomie IA sans human approval (ADR-036)
- ❌ Multi-tenant SaaS complexe avant validation marché
- ❌ Trop de systèmes tiers non contrôlés
- ❌ Pas de critères d'acceptation possibles
- ❌ Anti-client (cf. CLIENTS.md liste anti-clients)

### Acceptation (TOUS doivent être OK)

- ✅ Sponsor exécutif identifié
- ✅ Budget validé dans fourchette
- ✅ Scope cadrable en ≤ 3 jours (Discovery payée si > 1 j)
- ✅ Stack Tier A ou B (ou C avec premium signé)
- ✅ Conditions IP/AI compatibles avec MSA Architekt
- ✅ Async-first accepté
- ✅ Security gates acceptés
- ✅ Quality Report accepté comme livrable standard
- ✅ Region/compliance assumptions documentés

## Process

1. INTAKE.md rempli à partir discovery call
2. Critères vérifiés
3. Si refus → réponse polie avec referral si possible
4. Si accept → devis envoyé < 48 h + signature MSA + SOW

## Conséquences

### Positives
- Pas de "mauvais clients" (qui détruisent l'équipe)
- Marge protégée (R2)
- Image marque préservée

### Négatives
- Manquer ~20 % deals qu'on aurait acceptés sans rigueur
- Mitigation : revue trimestrielle des refus

## Sources
- `docs/INTAKE.md`
- `docs/CLIENTS.md` (anti-clients)
- `docs/skills-spec/architekt-commercial.spec.md`
