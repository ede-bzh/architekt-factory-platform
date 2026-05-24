# ADR-033 : International product baseline

- **Statut** : Proposé
- **Date** : 2026-05-24
- **Décideurs** : CTO, CDO design

## Contexte

Architekt opère globalement (APAC + MENA + EMEA + USA). Sans baseline international à l'intake, projets bâclés sur i18n/RTL/timezone/currency → refus clients MENA et EMEA notamment.

## Décision

**Tout projet global-ready doit définir explicitement** (cf. INTAKE.md section 6, I18N.md) :

| Aspect | Obligatoire |
|--------|-------------|
| Default language | Oui |
| Supported locales | Oui |
| RTL requirement | Oui (auto-déduit si Arabe/Hébreu) |
| Timezone model | Oui (UTC stocké, locale display) |
| Currency model | Oui |
| Tax/VAT assumption | Oui |
| Date/time formatting | Oui (ICU) |
| Number formatting | Oui (Intl) |
| Address format | Oui (lib spécialisée) |
| Phone format | Oui (E.164) |
| Legal entity / country | Oui |
| Data hosting region | Oui (ADR-035) |
| Support window | Oui |

## Conséquences

### Positives
- Pas de mauvaise surprise à la livraison
- Architecture prévue dès le début (vs refactor coûteux)
- Confiance client international

### Négatives
- Effort intake plus long (acceptable)

## Sources
- `docs/I18N.md`, `docs/INTAKE.md`
- ICU CLDR
- W3C i18n Activity
