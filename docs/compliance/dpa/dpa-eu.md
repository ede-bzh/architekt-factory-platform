# Data Processing Agreement — European Union (GDPR)

> **Disclaimer:** This document is a **template placeholder** for Architekt internal use only. It does **not** constitute legal advice. Have qualified counsel review before execution. See [`docs/COMPLIANCE.md`](../../COMPLIANCE.md) for regional baselines.

**Architekt** — Software Factory Platform  
Template: `docs/compliance/dpa/dpa-eu.md` | Framework: EU General Data Protection Regulation (GDPR) — Article 28 processor terms

---

## 1. Parties

| Role | Entity | Contact |
|------|--------|---------|
| **Data Controller** | `[CONTROLLER_LEGAL_NAME]` | `[CONTROLLER_DPO_EMAIL]` |
| **Data Processor** | **Architekt** (`[ARCHITEKT_LEGAL_ENTITY]`) | `[ARCHITEKT_DPO_EMAIL]` |

**Effective date:** `[EFFECTIVE_DATE]`  
**EU establishment / representative (if applicable):** `[EU_REPRESENTATIVE_ART_27]`  
**Agreement term:** Co-terminous with `[MSA_REFERENCE]`.

---

## 2. Scope

**Subject matter:** Processing of personal data by Architekt on behalf of the Controller under GDPR Article 28.

**Duration:** Term of the main agreement and wind-down per Section 5 (Retention).

**Categories of data subjects:** `[EMPLOYEES, CUSTOMERS, USERS — specify]`

**Nature and purpose of processing:**

- `[PURPOSE — e.g., AI-assisted software engineering platform services]`
- `[PURPOSE — e.g., storage and orchestration of project artifacts and agent sessions]`

**Lawful basis:** Determined by Controller (`[CONTRACT / LEGITIMATE_INTEREST / CONSENT — Art. 6]`). Architekt acts solely as Processor.

**GDPR Article 28 requirements (placeholder checklist):**

- [ ] Written instructions documented (this DPA + MSA)
- [ ] Confidentiality commitments for authorized personnel
- [ ] Subprocessor flow-down per Section 3
- [ ] Assistance with data subject rights (Section 5)
- [ ] Assistance with DPIA / prior consultation where applicable: `[DPIA_REFERENCE]`
- [ ] Delete/return data at end of services (Section 5)

**Default hosting:** EU region (`[e.g., AWS eu-west-1, Azure West Europe, Hetzner FSN]`) unless otherwise agreed.

---

## 3. Subprocessors

Controller provides **`[GENERAL / SPECIFIC]`** authorization for subprocessors listed in Annex `[SUBPROCESSOR_ANNEX]`.

| Subprocessor | Processing activity | Location | Safeguards |
|--------------|---------------------|----------|------------|
| `[SUBPROCESSOR_1]` | `[hosting]` | `[EU / EEA]` | `[DPA in place]` |
| `[SUBPROCESSOR_2]` | `[LLM inference]` | `[non-EEA if any]` | `[SCC Module + TIA]` |

**International transfers (Chapter V):** Transfers to third countries use **EU Standard Contractual Clauses (SCCs)** — `[MODULE_2_CONTROLLER_TO_PROCESSOR / MODULE_3_PROCESSOR_TO_PROCESSOR]` dated `[SCC_DATE]`, supplemented by **Transfer Impact Assessment (TIA)**: `[TIA_REFERENCE]`.

**Subprocessor changes:** `[NOTICE_DAYS]` days' prior notice. Controller may object within `[OBJECTION_DAYS]` days on GDPR grounds.

**Flow-down:** Architekt ensures subprocessors are bound by equivalent Article 28 obligations.

---

## 4. Data Categories

| Category | Personal data elements | Special categories (Art. 9) |
|----------|------------------------|----------------------------|
| Account | Name, email, user ID, org | No |
| Usage | Session logs, feature usage, API calls | No |
| Content | Project files, prompts, agent outputs | `[Only if contains personal data]` |
| Technical | IP address, user agent, timestamps | No |
| `[CUSTOM]` | `[describe]` | `[YES/NO — Art. 9 basis if yes]` |

**Data minimization (Art. 5(1)(c)):** Architekt processes only personal data necessary for the documented purposes.

**Prohibited processing:** Special categories and criminal data excluded unless expressly scoped: `[EXCLUSIONS]`.

---

## 5. Retention

| Data | Retention period | End-of-service |
|------|------------------|----------------|
| Active workspace data | Contract term | Return or delete within `[DELETION_DAYS]` days |
| LLM traces / observability | `[TRACE_RETENTION — e.g., 90 days]` | Anonymized or deleted |
| Security audit logs | `[LOG_RETENTION]` | Per legal/regulatory minimum |
| Backups | `[BACKUP_RETENTION]` | Encrypted rolling deletion |

**Data subject rights:** Architekt assists Controller with requests for access, rectification, erasure, restriction, portability, and objection within **`[REQUEST_SLA]`** business days.

**Certification of deletion:** Available upon request after termination.

---

## 6. Security Measures

Per GDPR Article 32, Architekt implements appropriate TOMs including:

- Pseudonymization and encryption where appropriate
- Ongoing confidentiality, integrity, availability, and resilience
- Restore availability and access after incident
- Regular testing and evaluation (CI security scans, pip-audit, bandit)
- Access controls, RBAC, bearer authentication
- Parameterized SQL; XSS mitigations (Jinja2 autoescape, CSP)
- Rate limiting (PG-backed, survives restart)
- SBOM (CycloneDX) attached to releases

**Annex II (TOMs):** Detailed in `[SECURITY_ANNEX_REFERENCE]`.

**Personnel:** All staff with data access under confidentiality agreements.

---

## 7. Breach Notification

**Personal data breach (Art. 33 / 34):** Breach of security leading to accidental or unlawful destruction, loss, alteration, unauthorized disclosure, or access.

**Processor obligations (Art. 33(2)):**

1. Notify Controller **without undue delay** after becoming aware — target **`[NOTIFICATION_HOURS — max 24]`** hours.
2. Provide: nature of breach, DPO contact, likely consequences, measures taken/proposed.
3. Provide further information as it becomes available.

**Controller notification to authority:** Within **72 hours** of awareness where required (Art. 33). Architekt assists.

**Data subject notification (Art. 34):** Controller decision; Architekt provides support.

**Incident contact:** `[SECURITY_INCIDENT_EMAIL]`

---

## 8. Audit

**Demonstration of compliance (Art. 28(3)(h)):** Architekt makes available all information necessary and allows for audits.

**Audit mechanism:**

- Documentary review on request (security policies, subprocessors, TOMs)
- On-site or remote audit up to **`[AUDIT_FREQUENCY — e.g., once per year]`** with `[NOTICE_DAYS]` days' notice
- Third-party certification (`[ISO 27001 / SOC 2 Type I/II]`) may substitute where accepted by Controller

**Supervisory authority:** Architekt cooperates with audits by competent EU supervisory authority where legally required.

**Costs:** Each party bears own costs unless attributable to Processor material breach.

---

## Annex references (placeholder)

| Annex | Content |
|-------|---------|
| A | Subprocessors list |
| B | Technical and organizational measures (TOMs) |
| C | Standard Contractual Clauses (if applicable) |
| D | Transfer Impact Assessment summary |

---

## Signatures

| | Data Controller | Architekt (Processor) |
|---|-----------------|----------------------|
| **Name** | `[SIGNATORY_NAME]` | `[SIGNATORY_NAME]` |
| **Title** | `[TITLE]` | `[TITLE]` |
| **Date** | `[DATE]` | `[DATE]` |
