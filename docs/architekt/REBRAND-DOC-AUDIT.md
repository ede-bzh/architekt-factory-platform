# Audit documentation — rebrand Architekt

**Statut** : vague E terminée (2026-05-24) — remplacement intégral dans le dépôt, sans alias legacy.

## Livré

| Vague | Périmètre | Statut |
|-------|----------|--------|
| A–D | UI, `ARCHITEKT_API_KEY`, thème, tests branding | ✅ |
| E | `architekt_platform`, user Docker `architekt`, Helm `architekt/`, métriques `architekt_*` | ✅ |
| Doc | Wiki Deployment EN/FR, `CLAUDE.md`, ADR-001, runbook vague E | ✅ |

## Gates CI

- `tests/test_doc_no_macaron_user_facing.py` — interdit Macaron / La Poste dans docs user-facing
- `tests/test_architekt_branding.py` — templates HTML
- `tests/test_wave_e_runtime.py` — détection package conteneur
- `tests/test_no_legacy_external_refs.py` — références externes La Poste (fichiers trackés)

## Vérification locale

```bash
rg -i 'macaron' --glob '!node_modules/**' --glob '!scripts/rebrand_macaron_to_architekt.py' --glob '!tests/test_*'
```

Les occurrences restantes dans `tests/` sont des patterns interdits ou noms de tests — attendu.
