# ADR-035 : Data residency decision model

- **Statut** : Proposé
- **Date** : 2026-05-24
- **Décideurs** : CTO, CISO, conseil juridique

## Contexte

La résidence des données est une contrainte critique pour clients EU (GDPR), MENA (PDPL UAE/Saudi), gouvernement. Sans modèle de décision, risque violation contractuelle ou pénal.

## Décision

**Data residency décidée avant build, jamais après.**

### Modèle de décision (par projet, à documenter dans INTAKE)

```
1. Identifier juridiction(s) client + utilisateurs finaux
2. Identifier sensibilité données (cf. SECURITY.md niveau)
3. Appliquer matrice COMPLIANCE.md par région
4. Choisir région hébergement (ADR-017)
5. Vérifier vendors / sub-processors compatibles
6. Documenter dans ADR projet
7. DPA signé avec localisation explicite
```

### Defaults par région

| Région utilisateur final | Hébergement par défaut |
|--------------------------|------------------------|
| Singapore | SG (AWS ap-southeast-1, Azure Singapore, Hetzner) |
| ASEAN (autres) | SG ou pays utilisateur (selon volume) |
| UAE | UAE (AWS Bahrain, Azure UAE, G42) |
| Saudi Arabia | KSA (STC Cloud, Mobily, AWS quand dispo) |
| EU/EEA | EU (AWS eu-west-1, Azure West Europe, Hetzner FSN) |
| UK | UK ou EU (post-Brexit DPA TIA) |
| USA | US (AWS us-east, Azure US) |

### Anti-patterns

- ❌ Réplication globale par défaut "pour la perf"
- ❌ Hébergement US pour client UE sans SCC + TIA
- ❌ Sous-traitance vendor sans vérification juridiction
- ❌ Logs centralisés cross-region sans review

### Cas spéciaux

- Données mineurs → EU/UK strict, US COPPA si applicable
- Données financières → souvent localisation requise
- Données santé → HIPAA US / GDPR Article 9 EU
- Données gouvernement → souverain par défaut

## Conséquences

### Positives
- Conformité par construction
- Pas de migration coûteuse forcée
- Confiance client

### Négatives
- Coût hébergement potentiellement plus élevé (UAE/KSA > Cloudflare global)
- Architecture multi-region plus complexe (cf. ARCHITECTURES.md pattern 6)

## Sources
- `docs/COMPLIANCE.md`
- ADR-017 Cloud deployment decision matrix
- GDPR Article 44+ (transferts internationaux)
- UAE PDPL Articles 22+
- Saudi PDPL transferts trans-frontières
