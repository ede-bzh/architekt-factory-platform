# Audit rebrand Architekt — vérification factuelle

Date de vérification : commit `cursor/architekt-rebrand-cleanup-7576` (HEAD au moment de l’audit).

Méthode : commandes shell + `pytest` sur le dépôt (pas d’affirmation sans preuve).

## Vagues ROADMAP

| Vague | Statut | Preuve |
|-------|--------|--------|
| A — Identité & hygiène | **OK** | `platform/branding.py`, templates/manifest/sw sans « Software Factory » (107 tests `test_architekt_branding.py`), code mort supprimé (`dashboard/platform/`, `orchestrator/`, `factory_bridge.py`, `platform/security.py` racine) |
| B — Documentation | **OK** | `README.md`/`README.fr.md` Architekt, `.env.example`, `docs/ROADMAP.md`, wiki EN/FR, screenshots `en`+`fr` seulement |
| C — Rationalisation | **OK** | Chiffres ~160+ agents / 41 workflows dans wiki ; `platform/SPECS.md` §14.4 |
| D — La Poste | **OK** | `tools/laposte-sync/`, `.gitlab-ci.yml` filtré par auteur Macaron |
| E — Docker `macaron_platform` | **Hors scope** | Inchangé volontairement |

## i18n UI (EN/FR)

| Contrôle | Résultat |
|----------|----------|
| `SUPPORTED_LANGS` | `("en", "fr")` dans `platform/i18n/__init__.py` |
| Fichiers locales | `en.json`, `fr.json` uniquement |
| Middleware `server.py` | EN/FR via `get_lang` + `normalize_lang` |
| API `/api/i18n/{lang}.json` | `normalize_lang()` |
| API `/api/set-lang/{lang}` | `normalize_lang()` (aligné) |
| Tests dédiés | `tests/test_i18n_en_fr.py` (15 tests) |

## Tests exécutés (verts)

```bash
pytest tests/test_i18n_en_fr.py tests/test_architekt_branding.py tests/test_api_key_alias.py -q
# 128 passed
```

## Écarts connus (hors périmètre UI strict)

Ces éléments peuvent encore mentionner Macaron / Software Factory sans casser les tests UI :

- Commentaires en tête de `platform/web/static/css/*.css`, `js/*.js` (ex. `MacaronSSE`)
- Routes backend / CLI (`cli/sf.py`, messages d’intégration Jira « Macaron »)
- `platform/CLAUDE.md`, workflows YAML historiques, infra Docker `macaron_platform`
- README multilingues archivés (`README.de.md`, etc.) — non liés dans README EN/FR

## Compteurs catalogue (mesurés)

| Ressource | Nombre |
|-----------|--------|
| Agents en base (`get_agent_store().count()`) | ~163 |
| Workflows builtin (`get_builtin_workflows()`) | 41 |
| Définitions YAML skills | 104 |

## Note sur les agents parallèles

Des sous-agents d’exploration ont parfois lu un état obsolète (cache / mauvais chemin). **Seuls les résultats reproduits par `git show HEAD:` et `pytest` sur la branche courante font foi.**
