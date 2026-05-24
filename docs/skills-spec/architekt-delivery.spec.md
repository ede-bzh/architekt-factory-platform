# Spec : architekt-delivery

> Skill cible : `skills/architekt-delivery.md`
> ADR référents : ADR-008

## Objectif du skill

Encoder la **méthode de delivery Architekt** pour que tout agent travaillant sur une mission client respecte les phases, gates et règles de scope.

## Quand utiliser

- À la **création** d'une nouvelle mission client
- À chaque **passage de phase** (discovery → build → hardening → handover)
- Lors d'une **demande client out-of-scope**
- En **revue mi-mission**

## Structure d'une mission client Architekt

```
1. Intake (1-3 jours)
2. Signature contractuelle
3. Discovery (3-5 jours)
4. Build (2-6 semaines selon offre)
5. Hardening (1-2 semaines)
6. Handover (1-2 jours)
7. Closure (2 semaines post-livraison)
```

Détails dans `docs/architekt/phase-4-first-clients.md`.

## Definition of Done (par phase)

| Phase | DoD |
|-------|-----|
| Discovery | ADR projet écrits, roadmap validée client, équipe assignée, mission manifest plateforme créé |
| Build | CI verte, tests pass, démo intermédiaire validée client, mutation testing modules critiques OK |
| Hardening | Pentest interne OK, SBOM généré, Lighthouse ≥ 90, doc utilisateur complète, runbook prêt |
| Handover | Repo transféré, formation faite, 30 j hotfix activé, accès retirés pour Architekt |
| Closure | Paiement final reçu, NPS collecté, retro écrite, case study OK |

## Règles de scope (anti-creep)

1. **Tout out-of-scope = avenant** (chiffré, signé)
2. **Pas de "petite faveur"** non tracée (chaque modif = ticket)
3. **Sprint planning hebdo** (pas quotidien)
4. **1 PO/sponsor client** identifié (pas de comité ouvert)
5. **Si client demande pivot > 20 % scope** → re-cadrage formel (peut être SOW v2)

## Limites de customisation

| Type | Limite |
|------|--------|
| Custom CSS sur shadcn | OK |
| Custom composants UI | OK |
| Custom data model | OK |
| Stack hors catalogue Tier A/B | Refus ou Tier C premium |
| Intégration > 2 systèmes tiers | Avenant ou refus |
| Compliance secteur régulé (banque, santé) | Refus jusqu'à équipe outillée |

## Budget temps par offre

cf. `docs/OFFERS.md` (FinOps par offre).

Si dépassement projeté > 10 % → escalade CPO+CTO.

## Critères kill / no-go projet

- Sponsor disparaît > 2 semaines
- Paiement intermédiaire impayé > 30 j
- Scope creep > 50 % vs SOW initial sans avenant
- Client demande action incompatible éthique / sécu / loi
- Marge prévisionnelle < 30 % et impossible à corriger

→ Procédure kill : `docs/architekt-delivery/kill-process.md` (à créer Phase 2)

## Anti-patterns

- ❌ Démarrer build sans Discovery validée
- ❌ Livrer sans Hardening
- ❌ Accepter "juste un petit fix" non tracé
- ❌ Pas de retro post-mission
- ❌ Pas d'ADR sur décisions structurantes
- ❌ Sprints quotidiens (planification = épuisant et inefficace pour 2 personnes)
