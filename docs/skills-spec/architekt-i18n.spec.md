# Spec : architekt-i18n

> Skill cible : `skills/architekt-i18n.md` (NOUVEAU)
> ADR référents : ADR-033, ADR-034

## Objectif

Encoder la **doctrine internationalisation Architekt** (locale, RTL, ICU, timezone, currency, fonts) pour que tout agent dev/UX livre des produits global-ready by design.

## Quand utiliser

- À l'intake (INTAKE section 6) si projet a langues alternatives ou marché secondaire
- Au choix du framework (i18n natif vs library)
- À chaque composant UI (CSS logical properties, RTL, expansion)
- Au choix de fonts si MENA
- À chaque champ formulaire (date, currency, address, phone)
- À chaque template email/notification

## Règle d'or

> Si projet a langue alternative ou marché secondaire potentiel → **i18n by default**.
> Coût d'ajout après = 3-10× coût de prévoir dès le début.

## Standards techniques (cf. ADR-034)

### Frontend

- **AUCUNE string hardcodée** — toujours `t('key')` ou équivalent
- **ICU MessageFormat** (variables, plurals, gender, dates)
- `Intl.DateTimeFormat` pour dates
- `Intl.NumberFormat` pour currency/numbers
- **CSS logical properties** (`padding-inline-start`, `inset-inline`)
- Bidirectional text testing
- Content expansion tolerance (DE +30 %, AR +25 %)
- Fonts Arabic si MENA (Noto Sans Arabic, IBM Plex Arabic, Cairo)
- URL strategy `/fr/about` ou `fr.example.com` (jamais query string)
- `<html lang="..." dir="...">`

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
- Texte multi-locale : table `translations(...)` ou JSONB
- Timestamps UTC stockés

## RTL — checklist obligatoire (Arabe, Hébreu, Urdu, Persan)

- ✅ CSS logical properties
- ✅ Tailwind v4 dir="rtl"
- ✅ Icônes flippées si directionnelles
- ✅ Number alignement (chiffres restent LTR)
- ✅ Mélange LTR/RTL testé (URL dans texte AR)
- ✅ Forms labels alignés
- ✅ Date pickers adaptés (calendrier Hijri optionnel pour KSA)

## Multi-currency

| Cas | Approche |
|-----|----------|
| Display only | API conversion (exchangerate.host) |
| Paiement multi-devise | Stripe multi-currency ou Paddle |
| Comptabilité | Stocker devise base + transaction + taux |

## Multi-timezone

- Stockage : UTC ISO 8601
- Affichage : timezone utilisateur
- Notifications : heure locale utilisateur
- Reports : préciser timezone

## Adresses, téléphones, noms

- **Adresses** : `address-format` library ou Google Places (variations pays)
- **Téléphones** : E.164 stockage, `libphonenumber` formatage
- **Noms** : champs `given_name`, `family_name`, `display_name` (pas first/last forcé)

## Pseudolocalization (test)

Utiliser pour vérifier layout :
- `Ẑẑ` (zalgo) en debug
- Lorem ipsum Arabe pour RTL
- Visual regression Playwright per-locale

## Anti-patterns

- ❌ Hardcoder strings "on traduira plus tard"
- ❌ Concaténer strings ("Hello " + name + "!") — utiliser ICU
- ❌ CSS physical (`padding-left`) sans logical equivalent
- ❌ Présumer alphabet Latin
- ❌ Stocker en timezone serveur
- ❌ Currency en number sans devise
- ❌ Date format en US par défaut globalement
- ❌ Photos casting US/EU sur site MENA/APAC

## Sources

- ADR-033 International product baseline
- ADR-034 i18n / RTL implementation standard
- `docs/I18N.md`
- Unicode CLDR, ICU
- Mozilla MDN i18n
