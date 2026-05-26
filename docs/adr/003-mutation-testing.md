# ADR-003 : Mutation testing (pragmatic CI gate)

- **Statut** : Accepté (wave P1)
- **Date** : 2026-05-25
- **Référence** : `scripts/ci/run_mutmut.sh`, `scripts/ci/mutation_gate.sh`, job `mutation` dans `.github/workflows/ci.yml`

## Contexte

Le coverage classique ne garantit pas que les tests détectent les régressions. Le mutation testing mute le code et vérifie que la suite échoue. Un objectif **global 50 %** sur `platform/` est reporté (coût CPU + surface 156 agents).

## Décision (scope wave P1)

| Cible | Fichier | Tests | Seuil minimal |
|-------|---------|-------|----------------|
| Garde-fous adversarial | `platform/agents/adversarial.py` (focus `check_l0`, `check_l2` via tests dédiés) | `tests/test_adversarial_l0.py`, `tests/test_adversarial_l2.py` | **15 %** |
| Clé API | `platform/auth/api_key.py` | `test_get_platform_api_key_*` | **10 %** |

- **Outil** : `mutmut==2.4.5` (compatible `--paths-to-mutate` ; évite le conflit stdlib `platform/` avec mutmut 3 en stats).
- **CI** : timeout **900 s** par cible ; `--max-children=2` réservé à mutmut 3+ (non activé tant que le linking stats n’est pas fiable).
- **Score** : `tués / (tués + survivants)` depuis `.mutmut-cache` (SQLite) ; mutants `untested` exclus.
- **Job** : `continue-on-error: true` sur le job ; l’étape **Mutation gate** exécute `mutation_gate.sh` et **échoue** si le seuil n’est pas atteint (visible dans le résumé Actions).

## Exécution locale

```bash
cd /workspace
pip install mutmut==2.4.5 pytest pytest-asyncio
export PLATFORM_ENV=test PLATFORM_LLM_PROVIDER=demo

bash scripts/ci/run_mutmut.sh api_key
bash scripts/ci/run_mutmut.sh adversarial   # ~3–15 min selon machine
```

Afficher les survivants : `env -u PYTHONPATH mutmut results` puis `mutmut show <id>`.

## Conséquences

- Gate honnête sur deux modules critiques sans bloquer tout le monorepo.
- Améliorer le score adversarial → renforcer tests L0/L2 ou réduire la surface mutée (pragma / extraction) avant de viser 50 % global.
