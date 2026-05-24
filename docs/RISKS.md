# Architekt — Registre des risques

> Risques identifiés à date (2026-05-24). Revu à chaque fin de phase et chaque trimestre.

## Légende

- **Gravité** : Critique / Haute / Moyenne / Basse
- **Probabilité** : Élevée / Moyenne / Basse
- **Priorité** = Gravité × Probabilité

## Vue d'ensemble

| # | Risque | Gravité | Probabilité | Priorité | Owner |
|---|--------|---------|-------------|----------|-------|
| R1 | Pas de pipeline commercial | **Critique** | Élevée | **P1** | CPO |
| R2 | Delivery non rentable (marge < 50 %) | **Critique** | Élevée | **P1** | CPO + CTO |
| R3 | Coût LLM invisible / dérive | Haute | Élevée | **P1** | CTO |
| R4 | Agents rapides mais code fragile (DORA 2025 amplificateur) | Haute | Moyenne | P2 | CTO |
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
| R15 | Marque "Architekt" confondue (orthographe DE) | Basse | Moyenne | P4 | Designer |
| R16 | Concurrence Devin / Factory / Lovable | Moyenne | Élevée | P2 | CPO |
| R17 | Mauvaise interprétation IMDA NAIIP eligibility | Moyenne | Moyenne | P3 | CPO |
| R18 | Sync La Poste casse pendant rebrand | Moyenne | Moyenne | P3 | CTO |
| R19 | Mutation testing devient théâtre qualité | Moyenne | Moyenne | P3 | CTO |
| R20 | Agents IA traitent données sensibles client sans consent | Haute | Basse | P2 | CISO |

## Détails par risque P1

### R1 — Pas de pipeline commercial

**Description** : tout l'effort va sur la plateforme, aucun lead entrant ni outbound structuré.

**Indicateur** : nombre de leads qualifiés / mois.

**Mitigation** :
- Phase 1 : offres packagées **obligatoires** (cf. `docs/OFFERS.md`)
- Phase 3 : site Architekt + démo vidéo + case study fictif
- Phase 4 : outreach structuré + candidature **IMDA NAIIP** + listing SME Digital Solutions
- Tester 3 canaux d'acquisition en parallèle dès Phase 4

**Trigger d'escalade** : 0 lead qualifié 4 semaines consécutives.

### R2 — Delivery non rentable

**Description** : projets livrés à perte (sous-évaluation, scope creep, sur-customisation).

**Indicateur** : marge brute par projet.

**Mitigation** :
- `docs/OFFERS.md` : prix planchers documentés
- `skills/architekt-delivery.md` : règles scope, definition of done
- `skills/architekt-finops.md` : budget LLM + heures max par offre
- Gate avant kick-off : "Architekt accept criteria" remplis
- Revue marge à mi-mission + retro post-livraison obligatoire

**Trigger d'escalade** : marge brute < 40 % sur 1 projet → revue immédiate ; sur 2 projets → freeze nouveaux contrats jusqu'à correctif méthode.

### R3 — Coût LLM invisible / dérive

**Description** : missions longues consomment 5-10× le budget LLM prévu sans visibilité temps réel.

**Indicateur** : ratio coût LLM réel / budget prévu par mission.

**Mitigation** :
- ADR-011 (LLM cost governance)
- FinOps obligatoire dans mission manifest (budget tokens/jour)
- Alerte UI à 70 % et 90 % budget consommé
- Auto-pause mission à 100 % budget (sauf override CTO)
- `skills/architekt-finops.md`

**Trigger d'escalade** : dépassement > 20 % sur 1 mission → audit ; sur 3 missions → règle automatique de cut-off durci.

### R5 — Trop de stacks trop tôt

**Description** : tentation d'équiper 11 stacks "au cas où". 2 personnes ne peuvent pas maintenir.

**Indicateur** : nombre de stacks actives / nombre de personnes.

**Mitigation** :
- Catalogue tierisé A/B/C strict (cf. `docs/CATALOG.md`)
- Tier A limité à **7 stacks max**
- Tier B activable seulement sur contrat signé
- Tier C uniquement sur contrat signé d'avance + premium pricing
- Revue trimestrielle promotion/rétrogradation

**Trigger d'escalade** : > 3 stacks Tier B activées en parallèle → freeze nouvelle activation jusqu'à stabilisation.

### R8 — Fondateurs surchargés

**Description** : 2 personnes ne peuvent pas faire CPO + CTO + dev + ops + vente + admin.

**Indicateur** : heures travaillées / personne / semaine.

**Mitigation** :
- Scope strict des offres (cf. R2)
- Playbooks (skills Architekt) automatisent répétition
- Plateforme = bras humain virtuel (c'est l'idée)
- **Embauche** déclenchée à 5 clients actifs (PM ou senior dev)
- Pas de side projects, pas de "petites faveurs"

**Trigger d'escalade** : > 55 h / semaine / personne pendant 4 semaines → embauche prioritaire ou réduction nb clients actifs.

## Risques sécurité (focus CISO)

### R6 — Sécurité insuffisante B2B

**Mitigation** :
- ADR-012 (SBOM + supply chain baseline)
- `skills/architekt-security.md` : OWASP ASVS L1 par défaut, L2 données sensibles
- NIST SSDF SP 800-218 v1.1 (v1.2 IPD) comme référence
- SAST + SCA + secret scanning en CI obligatoire
- SBOM CycloneDX/SPDX à chaque release
- Audit pentest externe à 5 clients (avant 1er client régulé)

### R13 — PDPA / RGPD non conforme

**Mitigation** :
- DPA template dans legal pack (Phase 0)
- ADR-018 (data retention + client isolation)
- Pas de transfert hors SG/EU sans consent explicite
- DPO externe sur contrat (déclencheur : 1er client santé/banque/gouvernement)

### R20 — Données sensibles client sans consent

**Mitigation** :
- ADR-013 (Client IP and AI-generated code policy)
- `skills/architekt-ai-governance.md` : human approval pour données client
- Agents jamais entraînés sur données client
- Logs anonymisés (cf. ADR-019)

## Risques techniques (focus CTO/SRE)

### R4 — Code fragile (effet amplificateur DORA 2025)

**Description** : DORA 2025 : *"AI adoption now improves software delivery throughput, but still increases delivery instability"*. Sans CI/tests/feedback rapides, l'IA crée du chaos.

**Mitigation** :
- CI verte **obligatoire** avant merge (Phase 2)
- TDD + mutation testing modules critiques
- Adversarial guard L0+L1 (existant plateforme)
- Review humaine obligatoire pour code prod
- Petits batches (definition of done granulaire)

### R12 — Single LLM provider

**Mitigation** :
- Multi-provider déjà en code (`platform/llm/client.py`)
- Fallback chain Azure OpenAI → Anthropic → MiniMax → local
- Test mensuel du basculement
- Cache prompts pour réduire dépendance

### R14 — Hetzner indisponibilité

**Mitigation** :
- Backups snapshots quotidiens (+1 €/mois)
- Restore documenté (`ops/RUNBOOK.md`)
- À 5 clients : envisager 2e VM (cluster) ou migration K8s managé

## Risques marque / commercial

### R7 — Confusion agence / SaaS

**Mitigation** :
- Doctrine claire en home page : *"AI-native digital product studio"*
- Pas de pricing public (jusqu'à 5 clients)
- Pas de bouton "signup" jusqu'à 10 clients

### R11 — Conflit licence

**Mitigation** :
- ADR-006 révisé : **propriétaire interne** (pas AGPL) tant que SaaS pas envisagé
- Skills/workflows individuels peuvent être MIT/Apache (à part)
- Code client : cession totale (clause MSA)
- Avocat SG consulté Phase 0

### R16 — Concurrence Devin / Factory / Lovable

**Mitigation** :
- Différenciation : **studio + plateforme + APAC**, pas IDE
- Argument anti-Devin : *"on ne remplace pas vos ingénieurs, on augmente votre delivery"*
- Argument anti-Lovable : *"on ne vend pas du prototype, on livre du production-grade avec rapport qualité"*
- Wedge IMDA = barrière locale APAC (concurrents US peu présents)

### R17 — IMDA NAIIP eligibility mal interprétée

**Description** : croire qu'Architekt peut bénéficier des subventions SME alors qu'on est vendor (côté offre).

**Mitigation** :
- Lire `docs/GTM.md` (clarifications)
- Architekt = **vendor** d'IA pour SMEs (pas SME bénéficiaire)
- Cible : être **pre-approved IMDA Solutions** vendor → clients Architekt récupèrent subvention

## Risques opérationnels

### R18 — Sync La Poste casse

**Mitigation** :
- Test dry-run avant merge Phase 0
- Garder branding Macaron dans `_LAPOSTE/` (sync exclusion)
- Documenter qui maintient le script (CTO)

### R19 — Mutation testing théâtre qualité

**Mitigation** :
- ADR-003 nuancé : obligatoire modules critiques seulement
- Seuils progressifs (50 → 70 → 80 %)
- Pas de mutation testing sur UI/glue/utilities
- Revue trimestrielle : si > 30 % temps CI sur mutation → réduire portée

## Process de revue

- **Hebdo** : check 3 risques P1 (R1, R2, R3, R5, R8)
- **Fin de phase** : revue complète + nouveaux risques identifiés
- **Trimestrielle** : revue + retrait/ajout/dé-priorisation
- **Sur incident** : ajout immédiat + post-mortem

## Issues GitHub liées

Chaque risque P1 a un issue tracker `risk:*` ouvert en permanence (cf. `.github/labels.yml`).
