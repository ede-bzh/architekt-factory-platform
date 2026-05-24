# ADR-020 : When to introduce multi-tenancy

- **Statut** : Proposé
- **Date** : 2026-05-24
- **Décideurs** : CTO, CPO

## Contexte

Le multi-tenant (1 instance plateforme servant plusieurs clients) est un sujet souvent introduit trop tôt et qui peut compromettre la sécurité et la performance d'un studio à 2 personnes.

## Décision

**Pas de multi-tenant avant déclencheurs précis.**

### Multi-tenant léger (Phase 6, à 5 clients actifs)

- Portail client = read-only
- Isolation `client_id` au niveau requête (filter SQL)
- Pas de partage de ressources critiques
- Authentification magic link

### Multi-tenant fort (Phase 7, si SaaS validé)

- Isolation DB (schema séparé ou DB séparée par tenant)
- Compute isolé (workspace dédié)
- Quotas par tenant
- Billing usage-based
- SSO enterprise (OIDC / SAML)
- RBAC fin

### Politique pré-trigger (Studio, Phase 0-5)

- **1 instance plateforme = 1 contexte interne Architekt** (= équipe Architekt utilise pour livrer les projets clients)
- **Données client = isolées par projet** (repo Git, vault, DB dédiée par projet)
- Pas de UI client direct, pas de login client

### Trigger Phase 6 (portail léger)

- ≥ 5 clients actifs
- ou ≥ 3 clients récurrents (run / TMA)
- Et : volume d'emails/DMs support > 5 / jour → portail crée vraie valeur

### Trigger Phase 7 (multi-tenant fort)

- ≥ 10 clients livrés
- ≥ 3 offres répétables avec marge stable > 50 % 6 mois
- Équipe ≥ 5 personnes (pas 2)
- Décision formelle écrite (`docs/decisions/saas-go-no-go.md`)

### Anti-patterns à éviter (en attendant)

- Ne pas pré-construire tenant isolation "au cas où"
- Ne pas ouvrir le login plateforme à des comptes externes
- Ne pas vendre la plateforme elle-même tant que studio profitable
- Ne pas accepter "self-service" partiel (tout ou rien)

## Conséquences

### Positives
- Évite complexité prématurée (multi-tenant = factor 3 effort sécu/ops)
- Focus 100 % sur delivery client
- Réduction surface attaque

### Négatives
- Pas de revenu MRR self-service
- Mitigation : Architekt Run (TMA) = MRR studio sans complexité multi-tenant

## Sources

- "Build SaaS later" — paradigme commun fondateurs experimentés 2026
- Retours d'expérience studios devenus SaaS (Linear, Webflow) : ont mis 2-3 ans en studio avant
