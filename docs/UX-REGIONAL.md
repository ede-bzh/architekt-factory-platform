# Architekt — Considérations UX par région

> Attentes UX par grande région. À internaliser pour tout projet international.

## APAC

### Caractéristiques
- **Mobile-first** quasi-obligatoire (>70 % trafic mobile dans la plupart des marchés)
- Multilingue (EN + langues locales : ZH, JA, KO, TH, ID, MY)
- **Performance** critique (réseaux variables, devices lower-end)
- Messageries dominantes selon marché :
  - SG/MY : **WhatsApp**
  - HK/TW : **WhatsApp + LINE**
  - JP : **LINE**
  - CN : **WeChat** (et son écosystème mini-programs)
  - TH : **LINE**
  - VN : **Zalo** + Messenger

### Design preferences
- Densité d'information acceptée (vs Europe minimaliste)
- Icônes + texte (vs icônes seules)
- Trust markers : awards, partenaires, presse

### À intégrer
- Boutons CTA WhatsApp / LINE / WeChat selon marché
- Tarification claire en monnaie locale (SGD, JPY, etc.)
- Témoignages locaux (pas que US/EU)
- Hours de support en timezone locale

## MENA

### Caractéristiques
- **Premium visual expectations** pour secteurs luxury, gouvernement, hospitality
- **Arabe + Anglais** dual-language (sometimes triple FR pour Maghreb)
- **RTL** par défaut si arabe
- Trust markers très importants (logos clients, awards, certifications)
- **WhatsApp** souvent critique pour relation commerciale

### Design preferences
- Esthétique riche, motifs géométriques OK
- Couleurs : or, bleu profond, vert deep souvent associés haut de gamme
- Typographie : fonts dédiées Arabe (Noto Sans Arabic, IBM Plex Sans Arabic, Cairo)
- Photos : casting culturellement adapté (vs stock photos US)

### À intégrer
- Switcher AR/EN visible (top right)
- WhatsApp Business CTA dans header
- Prix en AED / SAR / EGP / etc. (pas USD par défaut)
- Mentions légales conformes (UAE PDPL, KSA PDPL)
- Calendrier Hijri optionnel pour KSA

## EMEA (Europe)

### Caractéristiques
- **Accessibilité** legally enforced (EAA 2025) — WCAG 2.2 AA minimum
- **Privacy transparency** (cookie consent, "Why we collect")
- **Cookie consent banner** obligatoire
- Pages légales claires (Mentions légales, CGV, Politique de confidentialité, Cookies)
- Design **restrained, trustworthy** (vs US conversion-aggressive)

### Design preferences
- Minimalisme apprécié
- Typographie sobre (Inter, IBM Plex, system fonts)
- Couleurs : sobres, professionnelles
- Trust : ISO, GDPR-compliant badges, "Made in France/Germany/etc."

### À intégrer
- Cookie banner conforme (Klaro, Cookiebot, CookieFirst, ou maison)
- Footer riche : mentions légales, contact RGPD, DPO, etc.
- Multi-langue souvent attendu (FR + EN minimum)
- Modes de paiement : SEPA, iDEAL (NL), Bancontact (BE), Klarna

## USA

### Caractéristiques
- **Conversion-focused** (CTAs gros, sticky, partout)
- **Fast onboarding** (signup → demo en < 30 sec)
- **Strong proof points** : logos clients gros, témoignages vidéo, ROI chiffré
- **Clear ROI** dans le messaging
- SaaS-style UX attendu (signup, pricing public, free trial)

### Design preferences
- Big bold typography (Display fonts, gros chiffres)
- Couleurs vives + accents (vs sobriété européenne)
- Animations / micro-interactions
- Sections "as seen on" / "trusted by" prominent

### À intégrer
- **Pricing public** (pas "contact us" sauf enterprise)
- Free trial / freemium signup
- Live chat (Intercom, Drift, Front)
- "Book a demo" CTA partout
- Newsletter signup
- Comparaison vs concurrents (matrix table)

## Matrice synthèse UX

| Aspect | APAC | MENA | EMEA | USA |
|--------|------|------|------|-----|
| Mobile-first | ✅✅✅ | ✅✅ | ✅ | ✅✅ |
| Multilingue | ✅✅ | ✅✅✅ (AR+EN) | ✅✅ | ⚠️ |
| RTL | ❌ | ✅✅✅ | ❌ | ❌ |
| Accessibilité (WCAG strict) | ⚠️ | ⚠️ | ✅✅✅ | ✅✅ |
| Cookie consent | ⚠️ | ⚠️ | ✅✅✅ | ⚠️ (CA seulement) |
| Conversion-aggressive | ⚠️ | ✅ | ❌ | ✅✅✅ |
| Pricing public | ⚠️ | ❌ (souvent custom) | ⚠️ | ✅✅✅ |
| Trust markers (awards/clients) | ✅✅ | ✅✅✅ | ✅ | ✅✅ |
| Messageries (WhatsApp, etc.) | ✅✅✅ | ✅✅ | ⚠️ | ❌ |
| Performance ultra-rapide | ✅✅✅ | ✅ | ✅ | ✅✅ |
| Design premium attendu | ⚠️ | ✅✅✅ | ✅ | ✅ |

## Application Architekt

Pour chaque projet international, l'agent UX charge :

1. `docs/UX-REGIONAL.md` (ce fichier)
2. Section correspondant aux régions cibles
3. Vérifie checklist par région dans audit UX phase Hardening
4. Documente choix dans `<projet>/docs/ux/regional-decisions.md`

## Sources

- Nielsen Norman Group — Asian markets UX research
- IBM Design — Arabic / RTL guidelines
- GDS UK Design System — accessibility patterns
- Atlassian Design — i18n best practices
- Retours terrain Architekt 2026
