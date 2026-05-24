# ADR-013 : Client IP and AI-generated code policy

- **Statut** : Proposé
- **Date** : 2026-05-24
- **Décideurs** : CPO, CTO, conseil juridique SG

## Contexte

Le code généré par les agents IA Architekt pose des questions juridiques :

1. **Qui possède le code généré ?** (Architekt, le client, ou personne)
2. **Quelle propagation des licences open-source ?** (si AGPL dépendance, contamine ?)
3. **Quel droit moral d'auteur ?** (en SG le code IA = sans auteur humain unique)
4. **Quelles obligations de transparence IA vis-à-vis du client ?**

## Décision

### Propriété (cession totale au client)

- Tout code généré dans le workspace projet client est **cédé au client** à la livraison.
- Clause MSA : "All deliverables, including AI-generated code, are assigned to Client upon final payment."
- Architekt conserve le droit d'utiliser **patterns génériques** (pas du code spécifique métier client) pour entraîner ses propres skills.

### Open-source supply chain

- Architekt vérifie les licences des dépendances (via SBOM, cf. ADR-012)
- Refuse intégration de dépendances **AGPL** dans code client (sauf accord explicite)
- Préfère **MIT / Apache-2.0 / BSD / ISC**
- Documente licences dans `NOTICE.md` à la livraison

### Transparence IA

- Architekt **divulgue** au client que le code est généré par IA
- Liste des modèles utilisés (Anthropic Claude, OpenAI GPT, etc.) documentée
- Audit log agents disponible à la demande
- Client peut demander **opt-out IA** sur certains modules (Architekt utilise alors développement humain → surcoût négocié)

### Données client

- Les données client ne sont **jamais** envoyées pour fine-tuning à un LLM provider
- Les prompts contenant des données client utilisent **API providers avec data residency garantie** (Azure OpenAI EU / SG, Anthropic enterprise)
- Logs anonymisés (cf. ADR-019)

### Garanties

- 30 jours hotfix offert post-livraison (bugs critiques)
- Pas de garantie sur évolutions futures (offre Run séparée)
- Pas de garantie sur exactitude AI-generated content (clause "human review required for production")

## Conséquences

### Positives
- Sécurise les contrats B2B APAC
- Aligne avec EU AI Act + futures lois SG sur l'IA
- Différenciation vs concurrents qui floutent le sujet

### Négatives
- Process plus lourd (audit log + opt-out)
- Limitation supply chain (refus AGPL)

## Sources

- Singapore Model AI Governance Framework 2.0
- EU AI Act (Article 13 transparence, 28 obligations)
- US Copyright Office 2023 — code IA pure = pas protégé
- OWASP LLM Top 10 (data poisoning, exfiltration)
