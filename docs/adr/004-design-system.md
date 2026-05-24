# ADR-004 : Design system standard (shadcn/ui + Radix + Tailwind v4)

- **Statut** : Proposé
- **Date** : 2026-05-24
- **Décideurs** : CDO design, Product Designer (agent), CTO

## Contexte

Tous les projets clients web d'Architekt doivent partir d'une base UI cohérente, accessible et moderne. Sans standard, chaque projet réinvente boutons, formulaires, dark mode, a11y.

## Décision

**Stack design system par défaut** :

- **shadcn/ui** (composants copiés dans le repo client, pas dépendance NPM)
- **Radix UI** (primitives a11y sous-jacentes)
- **Tailwind CSS v4** (`@theme inline` + CSS variables OKLCH)
- **Lucide icons** (cohérent avec la plateforme actuelle Feather)
- **Mode** : light + dark via classe `.dark` sur root

## Tokens Architekt (à définir Phase 0)

Convention shadcn :

```css
:root {
  --background: oklch(? ? ?);
  --foreground: oklch(? ? ?);
  --primary: oklch(? ? ?);              /* couleur de marque Architekt */
  --primary-foreground: oklch(? ? ?);
  --radius: 0.5rem;
}
.dark { /* idem inversé */ }
```

Couleur de marque Architekt : **à choisir** (cf. ADR séparé Phase 0).

## Justification

| Argument | Source |
|----------|--------|
| shadcn/ui = standard 2026 | Consensus marché, doc référence |
| Code dans le repo = pas de breaking change | Pas de dépendance externe |
| Radix UI = a11y by default (WCAG 2.2) | Conforme PDPA SG + EAA EU |
| Tailwind v4 + OKLCH = couleurs perceptuelles | Migration future facile |
| Cohérent ASEAN multi-langue | Tokens découplent UI de contenu |

## Application

### Projets clients
- Tous les projets web Next.js / Astro / Nuxt partent de `components.json` shadcn pré-configuré
- Skill `architekt-ux.md` charge cette doctrine dans les agents UX

### Plateforme Architekt elle-même
- À long terme, migrer `platform/web/templates/` vers même base
- À court terme : juste mettre à jour les **CSS variables** (purple actuel → couleur Architekt)

## Conséquences

### Positives
- Vélocité projets client (composants prêts)
- A11y baseline gratuite (Radix)
- Brand Architekt cohérente partout

### Négatives
- shadcn/ui = React → contraint Nuxt/Vue à un équivalent (`shadcn-vue` existe, à valider)

### Risques
- Si shadcn/ui dévie trop, on est dans le code → mitigé (c'est aussi la force)
