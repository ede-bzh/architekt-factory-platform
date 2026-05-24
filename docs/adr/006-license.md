# ADR-006 : Licence du code plateforme Architekt

- **Statut** : À trancher Phase 0
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

## Décision (à confirmer)

**Recommandation** : modèle **open-core** :

| Composant | Licence | Raison |
|-----------|---------|--------|
| Plateforme noyau (`platform/`, `cli/`, `dashboard/`) | **AGPL-3.0** | Empêche concurrent de revendre en SaaS sans contribuer |
| Skills, workflows, kits | **MIT** ou **Apache-2.0** | Permet adoption large par clients |
| Code généré pour clients (workspaces) | **propriété client** | Cession totale dans contrat |
| Marque "Architekt" | **trademark** déposé SG | Protection commerciale |

## Alternatives

| Option | Avantage | Inconvénient |
|--------|----------|--------------|
| **Tout MIT** | Adoption max, simple | Concurrent peut forker et revendre |
| **Tout AGPL-3.0** | Protection forte | Bloque adoption interne client (peur du copyleft) |
| **Open-core (recommandé)** | Équilibre | Complexité juridique |
| **Source-available (BSL)** | Comme MongoDB | Pas "open source" officiellement |
| **Propriétaire fermé** | Contrôle total | Pas de communauté, plus dur de recruter |

## Action

1. CTO + avocat SG : valider modèle open-core (1 semaine)
2. Mettre à jour `LICENSE` racine
3. Aligner `pyproject.toml` `license = "AGPL-3.0-or-later"`
4. Aligner badge README sur licence réelle
5. Ajouter `NOTICE` pour dépendances tierces
6. Contrat client type : clause cession code généré

## Risques

- AGPL-3.0 peut faire fuir certains clients enterprise (peur copyleft)
  → Mitigation : licence commerciale alternative payante pour ceux-là
- Modèle open-core nécessite frontière claire core vs entreprise
  → Définir dans `docs/LICENSE-MAP.md`

## Conséquences si non décidé

Sans décision Phase 0 → **bloquant pour signer le 1er contrat client**.
