---
name: Architekt UX
description: Design system Architekt — shadcn/Radix/Tailwind v4, WCAG 2.2 AA vérifié (ADR-004, ADR-014)
tags: [ux, architekt, shadcn, wcag, design-system]
metadata:
  category: ux
  triggers: [ui, component, design-system, a11y, tailwind]
---

# Architekt UX

## Objectif

Encoder la **doctrine UX/UI Architekt** : design system standard, accessibilité WCAG 2.2 AA vérifiée — pas "shadcn = conforme par magie".

## Quand utiliser

- Setup projet web (components.json shadcn)
- Création/modification composants UI
- Revue design avant go-live
- Customisation tokens / dark mode

## Stack design system (ADR-004)

- **shadcn/ui** — composants copiés dans le repo client (pas dépendance NPM)
- **Radix UI** — primitives a11y
- **Tailwind CSS v4** — `@theme inline` + CSS variables OKLCH
- **Lucide icons**
- **Light + dark** via classe `.dark` sur root

Tokens via CSS variables shadcn (`--background`, `--primary`, `--radius`, etc.).

## WCAG 2.2 AA — minimum (ADR-014)

| Niveau | Quand |
|--------|-------|
| **AA** | Tous projets web (défaut) |
| **AAA** | Sur demande client (premium) |

### Outils CI

- **axe-core** Playwright — bloque PR si nouveau fail
- **Pa11y** — scan hebdo
- **Lighthouse a11y** ≥ 95 (gate pre-prod)
- Audit manuel clavier + screen reader (VoiceOver/NVDA) sur parcours critiques

### Checklist manuelle minimum

- Focus visible (outline non supprimé)
- Contraste texte ≥ 4.5:1 (3:1 texte large)
- Labels formulaires associés
- `alt` images (ou `alt=""` décoratif)
- Landmarks ARIA, skip links si page longue
- `prefers-reduced-motion` respecté
- Zoom 200% sans casse layout

## Règles composants

- Custom shadcn → vérifier focus, contraste, ARIA roles
- Pas de contenu transmis par couleur seule
- Content expansion prévu (DE +30%, AR +25%) — cf. skill i18n
- React Aria si composant complexe non couvert Radix

## Anti-patterns

- ❌ Présumer shadcn = WCAG conforme sans test
- ❌ Supprimer outline focus "pour le design"
- ❌ Couleur seule pour états erreur/succès
- ❌ Composants custom sans audit axe-core
- ❌ Ignorer navigation clavier

## Sources

- ADR-004 Design system standard
- ADR-014 Accessibility WCAG 2.2 AA
- W3C WCAG 2.2, ARIA Authoring Practices 1.2
- EU Accessibility Act 2025
