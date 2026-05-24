# ADR-006 : Licence du code plateforme Architekt (révisé)

- **Statut** : Proposé (révisé 2026-05-24 suite revue exécutive)
- **Date** : 2026-05-24
- **Décideurs** : CTO, CPO, conseil juridique (à consulter)

## Contexte

Le code actuel a une **incohérence** :

- `README.md` affiche **AGPL-3.0**
- `pyproject.toml` déclare **MIT**

Bloquant pour :
- Vendre des projets clients (qu'est-ce qu'on cède ?)
- Open-sourcer ou pas la plateforme
- Marque Architekt (image / juridique)

## Décision (révisée)

**Recommandation v2** : **propriétaire interne** tant que Phase 7 (SaaS) n'est pas validée.

| Composant | Licence | Raison |
|-----------|---------|--------|
| Plateforme noyau (`platform/`, `cli/`, `dashboard/`) | **Propriétaire interne** | Évite ambiguïté AGPL pour clients enterprise ; ne ferme aucune option future |
| Skills / workflows individuels (publiables) | **MIT** ou **Apache-2.0** | Permet partage sélectif ; pas un risque concurrentiel |
| Code généré pour clients (workspaces projet) | **propriété client** | Cession totale dans clause MSA (cf. ADR-013) |
| Marque "Architekt" | **trademark** déposé SG | Protection commerciale |

**Pourquoi changement vs v1 (open-core)** :
- AGPL fait peur aux clients enterprise B2B APAC (perception "viral copyleft")
- Le modèle commercial n'est pas clarifié (studio d'abord, SaaS plus tard)
- Rien ne bloque un passage à AGPL/MIT plus tard si productisation SaaS décidée
- Propriétaire interne = option par défaut **réversible**, pas une décision lourde

## Alternatives

| Option | Avantage | Inconvénient |
|--------|----------|--------------|
| **Tout MIT** | Adoption max, simple | Concurrent peut forker et revendre |
| **Tout AGPL-3.0** | Protection forte | Bloque adoption interne client (peur du copyleft) |
| **Open-core** | Équilibre | Complexité juridique, peur AGPL persiste |
| **Source-available (BSL)** | Comme MongoDB | Pas "open source" officiellement |
| **Propriétaire fermé interne (recommandé)** | Contrôle total, neutre vs clients | Pas de communauté open source |

## Action

1. **CTO + avocat SG** : valider modèle propriétaire interne (1 semaine)
2. Mettre à jour `LICENSE` racine → "All rights reserved" + permissive sur composants spécifiques
3. Aligner `pyproject.toml` `license = "Proprietary"` ou similaire
4. Aligner badge README
5. Ajouter `NOTICE` pour dépendances tierces (cf. ADR-013)
6. Contrat client type : clause cession code généré (cf. ADR-013)

## Risques

- Perception "fermé" peut freiner contributions externes (faible, on n'a pas de communauté à ce stade)
- Mitigation : composants `skills/` et `workflows/` publiables sous MIT à la demande
- Si revente envisagée : passer en AGPL au moment de Phase 7

## Conséquences si non décidé

Sans décision Phase 0 → **bloquant pour signer le 1er contrat client**.
