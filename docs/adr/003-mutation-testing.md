# ADR-003 : Mutation testing comme indicateur qualité réel des tests

- **Statut** : Proposé
- **Date** : 2026-05-24
- **Décideurs** : CTO, CAIO, Software Engineer (agent)

## Contexte

Le code coverage classique (% de lignes exécutées) **ment** : un test sans assertion donne 100% de coverage. Pour vendre des projets enterprise en Asie, Architekt doit pouvoir prouver la **qualité réelle** de sa suite de tests.

Le **mutation testing** introduit de petites mutations dans le code et vérifie que les tests les détectent. Score &gt; 80 % = suite de tests sérieuse.

## Décision

**Mutation testing obligatoire** sur tout projet Architekt, avec outil par stack :

| Stack | Outil | Seuil "break" CI |
|-------|-------|------------------|
| JS / TS | **Stryker Mutator** | 60% |
| Python | **mutmut** | 60% |
| Java | **PIT (Pitest)** | 60% |
| Rust | `cargo-mutants` | 60% (si projet Rust) |

**Mode d'exécution** :
- PRs : `--incremental` (mutants des fichiers changés uniquement)
- Nightly : run complet
- Cible **80%** atteinte progressivement (mois 1 = 50%, mois 3 = 70%, mois 6 = 80%)

## Justification

| Argument | Détail |
|----------|--------|
| Coverage ne suffit pas | 100% coverage avec tests vides = possible |
| Standard 2026 | Stryker (JS/TS), mutmut (Py), PIT (Java) = matures, en CI |
| Différenciant commercial | Peu d'agences l'utilisent → argument vente enterprise |
| Aligne avec adversarial guard | Garde-fou "no fake tests" déjà dans la plateforme |
| Reboucle TDD | Mutant survivant = test manquant → renforce TDD |

## Intégration plateforme

1. Ajouter `mutation_test` comme tool dans `platform/tools/build_tools.py` (wrapper Stryker/mutmut/PIT).
2. Phase QA des workflows : appel `mutation_test` après `test`.
3. Agent QA reçoit le rapport, doit ajouter tests pour tuer les mutants survivants.
4. Gate adversarial L2 : si score &lt; seuil → veto.

## Exemple configuration Stryker (projet pilote Architekt site)

```js
// stryker.conf.js
module.exports = {
  packageManager: 'npm',
  reporters: ['html', 'clear-text', 'progress'],
  testRunner: 'vitest',
  coverageAnalysis: 'perTest',
  mutate: ['src/**/*.ts', '!src/**/*.test.ts'],
  thresholds: { high: 80, low: 60, break: 50 },
  incremental: true,
};
```

## Conséquences

### Positives
- Qualité réelle mesurable, communicable au client
- Différenciant GTM Architekt vs agences classiques
- Cohérent avec doctrine TDD existante

### Négatives
- Mutation testing coûteux en CPU (mitigé par mode incrémental)
- Courbe d'apprentissage agents (à intégrer dans `skills/architekt-tech.md`)

### Risques
- Si seuil trop strict trop tôt → frustration
- Mitigation : seuil progressif (50 → 70 → 80% sur 6 mois)
