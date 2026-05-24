# ADR-034 : i18n and RTL implementation standard

- **Statut** : Proposé
- **Date** : 2026-05-24
- **Décideurs** : CTO, CDO design, Architecte

## Contexte

L'i18n et le RTL sont mal implémentés dans 80 % des projets agence. Coût d'ajouter i18n après = 3-10× coût d'avoir prévu. Pour le MENA, le RTL bâclé = refus immédiat.

## Décision

**Standards techniques i18n / RTL** (cf. `docs/I18N.md`) :

### Frontend

- **Aucune string hardcodée** — toutes via `t()` ou équivalent
- **ICU MessageFormat** (variables, plurals, gender, dates)
- Locale-aware dates (Intl.DateTimeFormat)
- Locale-aware currency (Intl.NumberFormat)
- **Layouts RTL-compatibles** (CSS logical properties)
- Bidirectional text testing
- Content expansion tolerance (DE +30 %, AR +25 %)
- Fonts Latin + Arabe quand MENA ciblé (Noto Sans Arabic, IBM Plex Arabic)
- URL strategy : `/fr/about` ou `fr.example.com` (jamais query string)
- `lang` + `dir` attributes sur `<html>`

### Frameworks par stack

| Stack | Library |
|-------|---------|
| Next.js | `next-intl` ou `next-i18next` |
| Astro | `astro-i18n` ou natif Astro 4+ |
| Nuxt | `@nuxtjs/i18n` |
| FastAPI | `babel` + `fastapi-babel` |
| NestJS | `nestjs-i18n` |
| WordPress | WPML ou Polylang |
| Shopify | Markets + Translate & Adapt |

### Backend

- Messages traduits par clé (i18next, fluent, gettext)
- Emails templates par locale
- Notifications timezone-aware
- Slugs URL : translit ASCII pour non-latin

### DB

- UTF-8 partout
- Collation locale-aware
- Texte multi-locale : table dédiée `translations(...)` ou JSONB
- Timestamps UTC stockés

## Conséquences

### Positives
- Projets MENA/EMEA livrables sans refactor
- Standards = vélocité (pas réinventer)
- Audit a11y RTL automatique

### Négatives
- Setup initial +10-15 % temps front
- Mitigation : skill `architekt-i18n.md` + templates Tier A pré-équipés

## Sources
- `docs/I18N.md`
- Unicode CLDR, ICU
- Mozilla MDN i18n
