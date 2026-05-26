# Data Processing Agreement — Singapore (PDPA)

> **Disclaimer:** This document is a **template placeholder** for Architekt internal use only. It does **not** constitute legal advice. Have qualified counsel review before execution. See [`docs/COMPLIANCE.md`](../../COMPLIANCE.md) for regional baselines.

**Architekt** — Software Factory Platform  
Template: `docs/compliance/dpa/dpa-singapore.md` | Framework: Singapore Personal Data Protection Act (PDPA)

---

## 1. Parties

| Role | Entity | Contact |
|------|--------|---------|
| **Data Controller** | `[CONTROLLER_LEGAL_NAME]` | `[CONTROLLER_DPO_EMAIL]` |
| **Data Processor** | **Architekt** (`[ARCHITEKT_LEGAL_ENTITY]`) | `[ARCHITEKT_DPO_EMAIL]` |

**Effective date:** `[EFFECTIVE_DATE]`  
**Agreement term:** Co-terminous with the main services agreement `[MSA_REFERENCE]`.

---

## 2. Scope

**Subject matter:** Processing of personal data by Architekt on behalf of the Controller in connection with `[SERVICE_DESCRIPTION]`.

**Duration:** For the term of the services agreement and any post-termination wind-down period defined therein.

**Nature and purpose of processing:**

- `[PURPOSE_1 — e.g., agent orchestration, project workspace hosting]`
- `[PURPOSE_2 — e.g., LLM-assisted development workflows]`

**PDPA alignment (placeholder):**

- Processing limited to purposes notified to data subjects and consistent with consent or other applicable basis.
- Purpose limitation and notification obligations documented in `[PRIVACY_NOTICE_REFERENCE]`.
- Default hosting region for Singapore clients: **Singapore** (see ADR-035 data residency).

**Controller instructions:** Architekt processes personal data only on documented instructions from the Controller, including as set out in this DPA and the main agreement.

---

## 3. Subprocessors

Architekt may engage subprocessors subject to written authorization and equivalent data protection obligations.

| Subprocessor | Service | Location | Data handled |
|--------------|---------|----------|--------------|
| `[SUBPROCESSOR_1]` | `[e.g., cloud hosting]` | `[Singapore / region]` | `[categories]` |
| `[SUBPROCESSOR_2]` | `[e.g., LLM provider]` | `[region]` | `[categories]` |

**Cross-border transfers (PDPA):** Transfers outside Singapore require notification to data subjects and protections substantially comparable to PDPA. Document transfer mechanism: `[TRANSFER_MECHANISM]`.

**Change notification:** Architekt will notify the Controller at least `[NOTICE_DAYS]` days before adding or replacing a subprocessor. Controller may object on reasonable grounds within `[OBJECTION_DAYS]` days.

**Current list:** Maintained at `[SUBPROCESSOR_LIST_URL_OR_ANNEX]`.

---

## 4. Data Categories

| Category | Examples | Special categories |
|----------|----------|-------------------|
| Identity & contact | Name, email, org role | `[YES/NO — specify]` |
| Account & auth | User IDs, access logs | No |
| Project & content | Code, docs, agent outputs | `[specify if PII embedded]` |
| Technical | IP address, device metadata | No |
| `[CUSTOM_CATEGORY]` | `[describe]` | `[YES/NO]` |

**Data subjects:** Controller employees, contractors, and end users as defined in `[DATA_SUBJECT_DEFINITION]`.

**Prohibited data:** Architekt does not accept processing of `[PROHIBITED_CATEGORIES — e.g., NRIC without explicit scope]` unless expressly agreed in writing.

---

## 5. Retention

| Data type | Retention period | Deletion method |
|-----------|------------------|-----------------|
| Active project data | Duration of contract + `[GRACE_DAYS]` days | Secure deletion / export to Controller |
| Audit & security logs | `[LOG_RETENTION — e.g., 90 days]` anonymized where feasible | Automated purge |
| Backups | `[BACKUP_RETENTION — e.g., 30 days]` rolling | Overwrite on cycle |

**PDPA retention limitation:** Personal data is retained no longer than necessary for the stated purposes. Upon termination, Architekt will delete or return personal data within `[DELETION_DAYS]` days unless law requires retention.

**Data subject requests:** Architekt assists the Controller with access and correction requests within `[REQUEST_SLA]` business days.

---

## 6. Security Measures

Architekt implements technical and organizational measures that are **reasonable and appropriate** under PDPA, including:

- Encryption in transit (TLS 1.2+) and at rest for production data stores
- Role-based access control and API authentication (`MACARON_API_KEY` / bearer tokens)
- Parameterized queries; no dynamic SQL concatenation
- Security headers (HSTS, CSP, X-Frame-Options)
- Adversarial output guards and prompt-injection mitigations (L0/L1)
- Rate limiting and audit logging of API mutations
- Regular dependency scanning (pip-audit, SBOM per release)

**Annex reference:** Detailed controls in `[SECURITY_ANNEX_OR_SOC2_READINESS_DOC]`.

**Personnel:** All Architekt personnel with access are bound by confidentiality obligations.

---

## 7. Breach Notification

**Definition:** A breach of security leading to accidental or unlawful destruction, loss, alteration, unauthorized disclosure of, or access to personal data.

**Processor obligations:**

1. Notify Controller without undue delay and within **`[NOTIFICATION_HOURS — e.g., 24]`** hours of becoming aware of a personal data breach.
2. Provide available details: nature of breach, categories and approximate number of records, likely consequences, measures taken or proposed.
3. Cooperate with Controller's assessment and any notification to the PDPC or affected individuals as required.

**Controller obligations:** Controller remains responsible for regulatory notification under PDPA. Architekt provides reasonable assistance.

**Contact for incidents:** `[SECURITY_INCIDENT_EMAIL]`

---

## 8. Audit

**Documentation:** Architekt makes available information necessary to demonstrate compliance with this DPA, including security summaries and subprocessors list.

**Audits:**

- Controller may request audit evidence up to **`[AUDIT_FREQUENCY — e.g., once per year]`**.
- On-site audits require **`[ON_SITE_NOTICE_DAYS]`** days' notice and are limited to `[BUSINESS_HOURS]` during normal business operations.
- Architekt may satisfy audit requests via third-party reports (e.g., SOC 2 Type I when available) in lieu of on-site inspection where acceptable to Controller.

**Costs:** Each party bears its own audit costs unless breach or material non-compliance is found.

---

## Signatures

| | Data Controller | Architekt (Processor) |
|---|-----------------|----------------------|
| **Name** | `[SIGNATORY_NAME]` | `[SIGNATORY_NAME]` |
| **Title** | `[TITLE]` | `[TITLE]` |
| **Date** | `[DATE]` | `[DATE]` |
