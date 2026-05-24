# Architekt Skills — Specifications

> Blueprints des 12 skills Architekt à implémenter en Phase 2.
> Chaque skill = un fichier Markdown (front-matter YAML + corps) chargé automatiquement par les agents IA selon les triggers.
> Format inspiré de `skills/tdd.md` existant.

## Liste des 12 skills

### Skills techniques (6 existants à enrichir)

| Spec | Skill cible | ADR référents |
|------|------------|---------------|
| `architekt-archi.spec.md` | `skills/architekt-archi.md` | ADR-002 |
| `architekt-tech.spec.md` | `skills/architekt-tech.md` | ADR-003 |
| `architekt-ux.spec.md` | `skills/architekt-ux.md` | ADR-004, ADR-014 |
| `architekt-data.spec.md` | `skills/architekt-data.md` | ADR-018 |
| `architekt-security.spec.md` | `skills/architekt-security.md` | ADR-012, ADR-013 |
| `architekt-sre.spec.md` | `skills/architekt-sre.md` | ADR-005, ADR-017 |

### Skills business / opérationnels (6 nouveaux)

| Spec | Skill cible | ADR référents |
|------|------------|---------------|
| `architekt-delivery.spec.md` | `skills/architekt-delivery.md` | ADR-008 |
| `architekt-product.spec.md` | `skills/architekt-product.md` | — |
| `architekt-finops.spec.md` | `skills/architekt-finops.md` | ADR-011, ADR-016 |
| `architekt-ai-governance.spec.md` | `skills/architekt-ai-governance.md` | ADR-010, ADR-019 |
| `architekt-commercial.spec.md` | `skills/architekt-commercial.md` | ADR-008 |
| `architekt-qa.spec.md` | `skills/architekt-qa.md` | ADR-003, ADR-014, ADR-015 |

## Convention de format skill

```yaml
---
name: <skill-name>
description: |
  <when to use this skill, in 1-3 sentences>
metadata:
  category: <archi | tech | ux | data | security | sre | delivery | product | finops | governance | commercial | qa>
  triggers:
    - "when ..."
    - "when ..."
---

# <Skill title>

## Use this skill when

- ...

## Do not use this skill when

- ...

## Instructions

### <Step 1>
...

### <Step 2>
...

## Examples

...

## Anti-patterns

- ...
```

## Implémentation

Les spec sont la **source de vérité produit**. Les skills réels (`skills/architekt-*.md`) seront créés en Phase 2 à partir de ces specs.

L'agent CTO + CAIO valident chaque spec avant implémentation.
