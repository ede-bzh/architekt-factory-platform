# Architekt — Global Project Readiness Checklist (Intake)

> À remplir **avant d'envoyer un devis**. Si une section est incomplète → impossible de chiffrer correctement.
> Référence : ADR-039 (Accept/reject project criteria).

## Comment utiliser

1. À chaque nouveau lead qualifié → ouvrir un doc `<lead>/intake.md` basé sur ce template
2. Compléter à partir de la discovery call (45 min)
3. Si bloquant → revenir au client (questions précises)
4. Si tout OK → passage à phase devis dans les 48h

---

## 1. Client profile

| Champ | Valeur |
|-------|--------|
| Nom société | _____ |
| Industrie | _____ |
| Région | APAC / MENA / EMEA / USA |
| Pays principal | _____ |
| Taille (employés) | _____ |
| Revenu annuel (range) | _____ |
| Phase | Startup / Scale-up / SME / Mid-market / Enterprise |
| Sponsor (nom, rôle, email) | _____ |
| Décideur final | _____ |
| Maturité technique | Faible / Moyenne / Élevée |
| Typologie cible (`docs/CLIENTS.md`) | 1-9 |

## 2. Project type

Choisir 1 type principal (cf. `docs/PROJECTS.md`) :

- [ ] A. Corporate / marketing platform
- [ ] B. Product MVP
- [ ] C. Internal business tool
- [ ] D. AI workflow automation
- [ ] E. E-commerce / headless commerce
- [ ] F. CMS / content platform
- [ ] G. Client portal
- [ ] H. Data / analytics dashboard
- [ ] I. Modernization project
- [ ] J. Security / quality audit

**Use cases précis** : _____

## 3. Stack decision

Référence : `docs/STACK-MATRIX.md`.

| Champ | Valeur |
|-------|--------|
| Stack par défaut (matrice) | _____ |
| Alternative justifiée | _____ + raison |
| Hosting region | _____ |
| Third-party services connus | _____ |
| Stack imposée par client ? | Oui / Non — si oui, Tier A/B/C ? |

## 4. Security level

Référence : `docs/SECURITY.md`.

| Champ | Valeur |
|-------|--------|
| Niveau requis | L0 / L1 / L2 / L3 |
| Données sensibles ? | Oui / Non — quelles catégories ? |
| Auth requise | Oui / Non — quel provider ? |
| RBAC complexité | Aucun / Basique / Fin |
| Contrôles spécifiques | _____ |
| Review owner sécurité | _____ |

## 5. Compliance assumptions

Référence : `docs/COMPLIANCE.md`.

| Champ | Valeur |
|-------|--------|
| Cadres applicables | GDPR / PDPA SG / UAE PDPL / Saudi PDPL / CCPA / SOC2-ready / HIPAA / autre |
| DPA requis ? | Oui / Non |
| Data residency | _____ |
| Rétention / suppression | _____ |
| Breach notification | _____ |
| Sub-processors restrictions | _____ |

## 6. Internationalization

Référence : `docs/I18N.md`, `docs/UX-REGIONAL.md`.

| Champ | Valeur |
|-------|--------|
| Langues | _____ |
| RTL requis ? | Oui / Non (auto si Arabe) |
| Timezone(s) | _____ |
| Currency(ies) | _____ |
| Date/number formats | _____ |
| Address formats | _____ |
| Région UX dominante | APAC / MENA / EMEA / USA |
| Messageries à intégrer | WhatsApp / LINE / WeChat / aucune |

## 7. Delivery model

| Champ | Valeur |
|-------|--------|
| Async-first accepté ? | Oui / Non |
| Support window | _____ |
| Points hebdo ? | Oui / Non — quel jour ? |
| Critères d'acceptation écrits ? | Oui / Non |
| Deadline imposée ? | _____ |
| Démos intermédiaires ? | Hebdo / Bi-hebdo |

## 8. Economics

| Champ | Valeur |
|-------|--------|
| Modèle | Forfait / T&M (cap) / Hybride |
| Marge cible Architekt | ≥ ____% |
| Budget LLM | ____ SGD |
| Budget infra | ____ SGD/mois |
| Opportunité maintenance (Run) ? | Oui / Non — engagement potentiel |
| Pénalités demandées | Oui / Non |
| Bonus performance ? | Oui / Non |

## 9. IP, AI & confidentialité

| Champ | Valeur |
|-------|--------|
| Architekt-MSA acceptable ? | Oui / Non / À négocier |
| Cession totale code à livraison ? | Confirmé / À discuter |
| Transparence usage IA OK ? | Confirmé / À discuter |
| Opt-out IA sur certains modules ? | Demandé / Non |
| NDA requis ? | Oui / Non |
| Confidentialité spéciale ? | _____ |

## 10. Décision Architekt

| Champ | Valeur |
|-------|--------|
| Acceptable ? | Oui / Non / Conditionnel |
| Offre Architekt cible | Launch / MVP / Portal / Internal Tool / AI Workflow / Commerce / Modernize / Audit / Run |
| Conditions à valider avant signature | _____ |
| Risques identifiés | _____ |
| Devis prévu pour le | _____ |

## Critères de refus systématique

Cocher si **un** est vrai → **refuser** :

- [ ] Pas de PO / sponsor identifié côté client
- [ ] Budget < seuil bas de l'offre cible (-30 %)
- [ ] Délai imposé incompatible avec scope (refuser plutôt que sur-promettre)
- [ ] Stack imposée hors Tier A/B (sauf signature Tier C avec premium)
- [ ] Domaine régulé sans budget compliance (santé régulé HIPAA, banque licenciée, défense, gambling)
- [ ] Conflit IP / clause AI non négociable
- [ ] Client refuse security/quality gates
- [ ] Client refuse pricing transparent
- [ ] Client veut autonomie IA sans human approval
- [ ] Multi-tenant SaaS complexe demandé avant validation marché
- [ ] Trop de systèmes tiers dont Architekt ne contrôle rien
- [ ] Pas de critères d'acceptation possibles à définir
- [ ] Anti-client (cf. `docs/CLIENTS.md` liste anti-clients)
- [ ] Conflit avec valeurs Architekt (à documenter)

## Critères d'acceptation (tous doivent être OK)

- [ ] Sponsor exécutif identifié
- [ ] Budget validé dans fourchette offre
- [ ] Scope cadrable en ≤ 3 jours (Discovery payée si > 1 j)
- [ ] Stack dans Tier A ou B
- [ ] Conditions IP/AI compatibles avec MSA Architekt
- [ ] Async-first accepté (pas de 24/7 sans Phase 6+)
- [ ] Security gates acceptés
- [ ] Quality Report accepté comme livrable standard

## Approbation interne

| Rôle | Nom | Approbation | Date |
|------|-----|-------------|------|
| CPO | _____ | Oui / Non | _____ |
| CTO | _____ | Oui / Non | _____ |

Une fois validé → ouvrir issue GitHub `[CLIENT] <nom>` + créer projet plateforme + envoyer devis dans 48 h.
