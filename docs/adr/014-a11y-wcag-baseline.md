# ADR-014 : Accessibility baseline WCAG 2.2 AA

- **Statut** : Proposé
- **Date** : 2026-05-24
- **Décideurs** : CDO design, Designer, CTO

## Contexte

shadcn/ui + Radix donne les bases d'accessibilité, mais **certains composants nécessitent corrections WCAG/focus/contraste** (2026). Présumer "shadcn = a11y conforme" est faux.

## Décision

**WCAG 2.2 niveau AA est le minimum livré sur tous les projets web Architekt.**

### Niveaux

| Niveau | Quand |
|--------|-------|
| **AA** | Par défaut sur tous projets |
| **AAA** | Sur demande client (premium pricing) |

### Outils et process

- **axe-core** en CI Playwright (bloque PR si nouveau fail)
- **Pa11y** scan CLI (rapport hebdo)
- **Audit manuel** : navigation clavier complète + screen reader (VoiceOver / NVDA) sur parcours critiques avant go-live
- **Lighthouse a11y** ≥ 95 (gate)
- **Audit composants shadcn** : si custom, vérifier focus visible, contraste 4.5:1, ARIA labels, role attributes

### Checklist manuelle minimum

- [ ] Tous les boutons et liens accessibles au clavier (Tab + Enter)
- [ ] Focus visible (outline non supprimé)
- [ ] Contraste texte ≥ 4.5:1 (3:1 pour texte large)
- [ ] Images ont `alt` (ou `alt=""` si décoratives)
- [ ] Formulaires ont `label` associé
- [ ] Pas de contenu uniquement transmis par couleur
- [ ] Navigation cohérente (landmarks ARIA)
- [ ] Skip links si page > 3 sections
- [ ] Animations respectent `prefers-reduced-motion`
- [ ] Texte zoomable jusqu'à 200 % sans casse

### Stack par défaut a11y

- shadcn/ui (base Radix)
- React Aria si composant complexe non couvert
- `@axe-core/react` en dev
- Storybook a11y addon si library composants

## Conséquences

### Positives
- Conformité légale (EAA EU 2025, UK Equality Act, SG DDA)
- Marché élargi (10-15 % utilisateurs)
- Argument vente B2B / secteur public

### Négatives
- Effort additionnel (~10 % temps front-end)
- Mitigation : checklist standard + automatisation CI

## Sources

- W3C WCAG 2.2 (oct. 2023)
- W3C ARIA Authoring Practices 1.2
- Audit indépendant shadcn/ui 2026 (composants nécessitant corrections)
- EU Accessibility Act 2025
