# Audit rebrand documentation & complétude (Wave 8)

**Date** : 2026-05-25  
**Branche** : `cursor/rebrand-doc-backlog-7576`  
**Version plateforme** : `2.3.0` (`platform/VERSION` sur `main`)  
**Dépôt cible** : `ede-bzh/architekt-factory-platform`

## Synthèse

Le rebrand **UI / runtime** (Architekt, `ARCHITEKT_API_KEY`, thème, tests `test_architekt_branding.py`) est largement livré (vagues A–D, PR #10–#11). En revanche, la **documentation utilisateur et développeur** reste hétérogène : branding Macaron, dépôt `macaron-software/software-factory`, GitLab La Poste, clé `MACARON_API_KEY` sans contexte alias, versions et compteurs obsolètes, pages wiki courtes ou pages i18n hors périmètre EN/FR encore présentes.

**Décision** : traiter en profondeur via **Wave 8** (`docs/architekt/PLATFORM-BACKLOG.md`), pas par patches ponctuels non planifiés.

| Priorité | Périmètre | Occurrences indicatives (mai 2026) | Action |
|----------|-----------|-----------------------------------|--------|
| **P0** | Wiki EN/FR, README, API/Security/Deployment wiki | ~20 hits wiki + README multilingues | Rebrand + URLs `ede-bzh`, v2.3.0, 163/41/104 |
| **P1** | `CLAUDE.md` racine, `platform/CLAUDE.md`, CONTRIBUTING/CODE_OF_CONDUCT | ~40+ hits contexte dev | Réécrire pour Architekt studio ; retirer sync La Poste |
| **P2** | Infra prod (ADR-001 vague E) | `macaron_platform`, `/opt/macaron`, user Docker `macaron` | Runbook + migration planifiée, pas doc marketing |
| **P3** | Historique / ADR | ADR-001, commentaires CSS `MacaronSSE` | Garder historique explicite ; glossaire alias 6 mois |

Gate **La Poste** : `tests/test_no_legacy_external_refs.py` (fichiers trackés) — distinct du nettoyage **Macaron** dans la doc.

---

## P0 — Documentation utilisateur (wiki + README)

### Wiki `docs/wiki/` (5 fichiers, ~20 occurrences `macaron` / `laposte`)

| Fichier | Problèmes | Complétude |
|---------|-----------|------------|
| `Home.md` | « Macaron Software Factory », v2.2.0, clone `macaron-software`, tableau GitLab La Poste | Accueil OK structure, contenu legacy |
| `Home‐FR.md` | Idem + URL La Poste explicite | Idem |
| `Home‐ES.md`, `Home‐IT.md`, `Home‐PT.md`, `Home‐DE.md`, `Home‐JA.md`, `Home‐ZH.md` | Branding Macaron, clone legacy | **Hors scope i18n officiel** (ROADMAP : EN/FR seulement) — archiver ou supprimer |
| `API-Reference.md` | `MACARON_API_KEY` seul | Manque `ARCHITEKT_API_KEY`, exemples curl, codes erreur |
| `Security.md` | `MACARON_API_KEY`, user Docker `macaron` | Manque politique HITL, L2 LLM, CSP nonce (voir PR #13) |
| `Deployment-Guide.md` | Wave E : tableau `architekt_platform`, runbook, Azure rebuild/hotpatch | ✅ Livré (EN + `Deployment-Guide‐FR`) |
| `Patterns.md` | 28 lignes, tableau seul | Pas de liens patterns ↔ missions, pas de FR dédié (lien `Patterns‐FR` absent) |
| `_Sidebar.md` | Déjà « Architekt Factory » | Aligner avec Home après rebrand |

### README racine et traductions

- `README.md` : demo `sf.macaron-software.com`, clone/issues `macaron-software/software-factory`.
- `README.fr.md` (+ DE/ES/JA/KO/PT/ZH) : mêmes URLs — **P0** aligner demo Architekt + repo GitHub studio.
- Compteurs : README annonce **161** agents ; backlog Wave 6 cite **~163**, **41** workflows, **104** skills — **une source de vérité** à dériver de `agents/store.py` + `workflows/builtins.py` + skills YAML.

### Sections non renseignées ou minimales (complétude)

Pages à enrichir (cible : guide exploitable sans lire le code) :

1. **Patterns** — cas d’usage par phase mission, lien adversarial / HITL.
2. **Security** — auth, rate limit, adversarial L0–L2, secrets, CSP (réf. `docs/architekt/CSP.md` quand mergé PR #13).
3. **API-Reference** — pagination, erreurs 401/429, webhooks si applicable.
4. **Deployment-Guide** — profil OVH demo Architekt vs Azure legacy (deux colonnes).
5. **Wiki FR miroir** — chaque page EN avec équivalent FR (`Security‐FR` référencé mais absent du dépôt).
6. **`docs/architekt/`** — phases 0–7 OK ; manque index unique « où lire quoi » (lien depuis `docs/ROADMAP.md`).

---

## P1 — Contexte développeur & gouvernance

| Fichier | État |
|---------|------|
| `CLAUDE.md` (racine) | Sections `_MACARON-SOFTWARE`, `_LAPOSTE`, `sync-to-laposte`, Azure `macaron@`, `macaron_platform` |
| `platform/CLAUDE.md` | Héritage Software Factory / Macaron (si présent sur branche) |
| `CONTRIBUTING*.md`, `CODE_OF_CONDUCT*.md` | Liens macaron-software |
| `docs/AUDIT_REBRAND.md` | Audit vagues A–E ; **à compléter** par renvoi vers ce document |
| `sync-to-laposte.sh` | 32+ refs — **supprimer du dépôt** ou déplacer hors repo (déjà visé vague D) |

Tests existants sur `main` (à étendre en Wave 8) :

- `tests/test_no_legacy_external_refs.py` — La Poste uniquement.
- `tests/test_architekt_branding.py` — UI.
- `tests/test_readme_en_fr.py` — README EN/FR Architekt.

**Proposition gate doc** : `tests/test_doc_no_macaron_user_facing.py` — scan `docs/wiki/Home*.md`, `README.md`, `README.fr.md` pour interdire `macaron-software` et « Macaron Software Factory » (exceptions : bloc « Infra legacy » dans Deployment-Guide).

---

## P2 — Infra & packaging (vague E, hors doc marketing)

Conserver temporairement dans la doc **ops** avec libellé explicite « legacy prod » :

- Module Python import `macaron_platform` (mapping Docker).
- Helm chart `deploy/helm/macaron/`.
- Métriques Prometheus alias `macaron_*` → `architekt_*` (déjà partiellement fait Wave 4).
- `MACARON_API_KEY` alias 6 mois (`platform/auth/api_key.py`, ADR-001).

Ne pas renommer dans Wave 8 sans runbook RTO — seulement documenter la cible `architekt_platform`.

---

## P3 — Fichiers à ne pas « nettoyer » aveuglément

- `docs/adr/001-rebrand-architekt.md` — mentions Macaron **volontaires** (historique).
- Données de test / fixtures `_FINARY`, CSV — hors périmètre.
- `node_modules/`, caches — exclus.

---

## Plan d’exécution Wave 8 (backlog)

Voir `docs/architekt/PLATFORM-BACKLOG.md` § **Wave 8**.

Ordre recommandé :

1. Wiki **Home** + **Home‐FR** + sidebar (P0).
2. README EN/FR + tests readme (P0).
3. API-Reference + Security + Patterns contenu (P0 complétude).
4. Suppression ou `docs/wiki/archive/` pour Home‐ES/IT/PT/DE/JA/ZH (P0 i18n).
5. Réécriture `CLAUDE.md` studio Architekt (P1).
6. Extension tests doc + mise à jour `docs/AUDIT_REBRAND.md` (P1).
7. Encarts infra legacy + lien ADR-001 vague E (P2).

**Hors Wave 8** : merge PR #12 (wiki Darwin, DPA, backlog sync), PR #13 (CSP, L2 LLM doc), puis branche dédiée exécution Wave 8.

---

## Commandes de revérification

```bash
# La Poste (gate CI)
pytest tests/test_no_legacy_external_refs.py -q

# Branding UI
pytest tests/test_architekt_branding.py -q

# Inventaire doc (manuel)
rg -i 'macaron|laposte' docs/wiki README.md README.fr.md CLAUDE.md
wc -l docs/wiki/*.md
```

---

## Références

- `docs/ROADMAP.md` — vagues A–E, vague 6, **vague 8 (doc)**
- `docs/adr/001-rebrand-architekt.md`
- `docs/AUDIT_REBRAND.md` — audit UI (à synchroniser)
- `docs/architekt/PLATFORM-BACKLOG.md` — source de vérité tâches
