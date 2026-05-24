# ADR-043 : Incident response baseline

- **Statut** : Proposé
- **Date** : 2026-05-24
- **Décideurs** : CTO, CISO, SRE

## Contexte

Tout système en production aura des incidents. Sans process incident response baseline, perte de temps + sur-impact client + violation breach notification (72h GDPR).

## Décision

**Process incident response standard** pour tout projet Architekt.

### Sévérités

| P | Définition | Exemple |
|---|-----------|---------|
| **P1** | Service down complet ou data breach confirmé | Site offline, DB compromise |
| **P2** | Service dégradé majeur ou risque data breach | API 50 % erreurs, vuln critique exploitée |
| **P3** | Bug fonctionnel impactant clients | Feature cassée pour subset utilisateurs |
| **P4** | Bug mineur ou cosmétique | UI glitch, typo |

### SLAs (clients Run / retainer)

| Sévérité | Détection → notif | Notif → action | Action → résolution |
|----------|-------------------|----------------|---------------------|
| P1 | < 15 min | < 30 min | < 4 h |
| P2 | < 30 min | < 1 h | < 24 h |
| P3 | < 4 h | < 24 h | < 7 j |
| P4 | < 24 h | < 7 j | sprint suivant |

### Process (6 étapes)

1. **Détection** — monitoring auto, report client, alerte sécu
2. **Triage** — sévérité P1-P4, lead assigné, page si P1
3. **Containment** — isoler, freeze deploys, rotation secrets si compromise
4. **Eradication** — patch, vérifier root cause
5. **Recovery** — restore, vérifier service stable
6. **Post-mortem** — blameless, dans 7 jours, actions correctives trackées

### Documentation par projet

- `<projet>/docs/security/incident-response.md` — playbook spécifique
- `<projet>/docs/security/contacts.md` — qui appeler quand
- Astreinte : qui (Phase 4 = fondateurs ; Phase 5+ = SRE embauché ou astreinte tournante)

### Breach notification (data breach)

- GDPR : 72h à l'autorité + sujets si risque élevé
- PDPA SG : sans délai déraisonnable + sujets si risque significatif
- UAE PDPL : 72h
- Saudi PDPL : 72h
- Différer notification = pénalités accrues

### Outils

- **Status page** : statuspage.io ou self-hosted (cstate)
- **On-call** : PagerDuty / Opsgenie (Phase 5+, sinon Telegram bot)
- **Runbook** : `<projet>/docs/runbook.md`
- **Communication** : Slack/Teams interne, email client

### Drills

- Phase 4 : 1 drill par trimestre (incident simulé)
- Phase 5+ : 1 drill par mois, varier scénarios (DB corruption, secret leak, ransomware, DDoS)

## Conséquences

### Positives
- Réactivité réelle (pas improvisation)
- Conformité breach notification
- Confiance client (savoir gérer les crises)

### Négatives
- Coût astreinte
- Mitigation : pas d'astreinte 24/7 avant Phase 6+ (clients acceptent SLA business hours pour Phase 4-5)

## Sources
- Google SRE Book (Incident Management)
- NIST SP 800-61 Rev. 2 (Computer Security Incident Handling Guide)
- GDPR Article 33-34
- `docs/SECURITY.md`
