# Data Processing Agreement — United States (SCC-Oriented Processor)

> **Disclaimer:** This document is a **template placeholder** for Architekt internal use only. It does **not** constitute legal advice. Have qualified counsel review before execution. See [`docs/COMPLIANCE.md`](../../COMPLIANCE.md) for regional baselines.

**Architekt** — Software Factory Platform  
Template: `docs/compliance/dpa/dpa-us.md` | Framework: US B2B processor terms with **EU SCC Module 2/3** alignment for cross-border transfers and **CCPA/CPRA**-ready service provider language

---

## 1. Parties

| Role | Entity | Contact |
|------|--------|---------|
| **Business / Controller** | `[CONTROLLER_LEGAL_NAME]` | `[CONTROLLER_PRIVACY_CONTACT]` |
| **Service Provider / Processor** | **Architekt** (`[ARCHITEKT_LEGAL_ENTITY]`) | `[ARCHITEKT_PRIVACY_CONTACT]` |

**Effective date:** `[EFFECTIVE_DATE]`  
**Primary jurisdiction:** `[US_STATE — e.g., California]`  
**Agreement term:** Co-terminous with `[MSA_REFERENCE]`.

---

## 2. Scope

**Subject matter:** Processing of personal information by Architekt on behalf of the Business in connection with `[SERVICE_DESCRIPTION]`.

**Duration:** Term of the services agreement and any post-termination obligations in Section 5.

**Processing purposes (limited to):**

- `[PURPOSE_1 — e.g., software delivery platform operations]`
- `[PURPOSE_2 — e.g., agent workflow execution and artifact storage]`

**US privacy alignment (placeholder):**

- **CCPA/CPRA service provider:** Architekt processes personal information only for business purposes specified in the contract; does not sell or share personal information; does not retain, use, or disclose PI outside the direct business relationship except as permitted by CPRA §1798.140(ag).
- **Other state laws:** Baseline aligned to CCPA (Colorado CPA, Connecticut CTDPA, Virginia VCDPA, etc.) unless `[STATE_SPECIFIC_ADDENDUM]` applies.
- **HIPAA:** Not in scope unless separate **BAA** executed: `[BAA_REFERENCE — default: N/A, Architekt declines HIPAA until equipped]`.

**Instructions:** Architekt processes personal information only on documented instructions from the Business.

**Default hosting:** US region (`[e.g., US East, US West]`) unless EU/other residency agreed separately.

---

## 3. Subprocessors

Architekt may use subprocessors with equivalent contractual protections.

| Subprocessor | Service | Location | Transfer mechanism |
|--------------|---------|----------|-------------------|
| `[SUBPROCESSOR_1]` | `[cloud infrastructure]` | `[US region]` | N/A (domestic) |
| `[SUBPROCESSOR_2]` | `[LLM provider]` | `[US / non-US]` | `[SCC Module 3 + TIA if non-US]` |

**EU SCC integration (cross-border):** Where personal data of EEA/UK/Swiss data subjects is processed, the parties incorporate **EU Commission Standard Contractual Clauses**:

- Module: `[MODULE_2 (C2P) / MODULE_3 (P2P)]`
- Docking clause: `[YES/NO]`
- TIA reference: `[TIA_DOCUMENT]`

**Notification:** `[NOTICE_DAYS]` days before subprocessor changes. Business may object on reasonable privacy grounds.

**List:** `[SUBPROCESSOR_LIST_URL_OR_ANNEX]`

---

## 4. Data Categories

| Category | Examples | Sensitive PI (CPRA) |
|----------|----------|---------------------|
| Identifiers | Name, email, account ID | No |
| Commercial | Subscription tier, billing contact | No |
| Internet / electronic | IP, logs, device data | No |
| Professional | Job title, project role | No |
| Content | Code, docs, agent conversation logs | `[May contain PI — classify]` |
| `[CUSTOM]` | `[describe]` | `[YES/NO]` |

**Consumers / data subjects:** `[EMPLOYEES, END USERS, CUSTOMERS — define]`

**Sale / share:** Architekt **does not sell** personal information and **does not share** for cross-context behavioral advertising.

**Minors:** Processing of data from children under 13 excluded unless `[COPPA_ADDENDUM]` executed.

---

## 5. Retention

| Data type | Retention | Deletion |
|-----------|-----------|----------|
| Active service data | Contract term | Export + delete within `[DELETION_DAYS]` days of termination |
| Observability / LLM traces | `[TRACE_RETENTION]` | Automated purge |
| Security logs | `[LOG_RETENTION]` | Rolling deletion |
| Backups | `[BACKUP_RETENTION]` | Encrypted overwrite |

**Retention limitation:** Personal information retained only as long as necessary for the contracted purposes.

**Consumer rights support:** Architekt assists Business with access, deletion, correction, and portability requests (CCPA §1798.100 et seq.) within **`[REQUEST_SLA]`** business days.

**Certification:** Written confirmation of deletion available upon request.

---

## 6. Security Measures

Architekt maintains administrative, technical, and physical safeguards appropriate for B2B SaaS and **SOC 2-ready** posture:

- Encryption in transit (TLS) and at rest for production data
- Access controls, API authentication, least privilege
- Vulnerability management (pip-audit, dependency updates via Dependabot)
- Static analysis (bandit) and secret scanning in CI
- Audit logging of mutations and agent tool invocations
- Incident response procedures documented in `[INCIDENT_RUNBOOK]`
- SBOM (CycloneDX) per release for supply chain transparency

**SOC 2 mapping (preparatory):** Security, Availability, Processing Integrity, Confidentiality, Privacy — see `docs/COMPLIANCE.md`.

**Subprocessor oversight:** Due diligence and contractual flow-down of equivalent safeguards.

---

## 7. Breach Notification

**Security incident:** Unauthorized access, acquisition, use, or disclosure of personal information.

**Processor obligations:**

1. Notify Business without unreasonable delay, target within **`[NOTIFICATION_HOURS — e.g., 24]`** hours of confirmation.
2. Provide: incident description, categories of PI affected, approximate count, remediation steps, contact for follow-up.
3. Cooperate with Business's obligations under applicable state breach notification laws (e.g., California Civil Code §1798.82).

**Regulatory / consumer notification:** Business determines required notifications. Architekt provides reasonable assistance.

**No waiver of privilege:** Incident communications may be designated confidential and subject to common interest privilege where applicable.

**Contact:** `[SECURITY_INCIDENT_EMAIL]`

---

## 8. Audit

**Compliance documentation:** Architekt provides information reasonably necessary to demonstrate compliance, including subprocessors list and security program summary.

**Audit rights:**

- Annual audit or inspection upon **`[NOTICE_DAYS]`** days' written notice, up to **`[AUDIT_FREQUENCY — e.g., once per year]`**
- Remote audit preferred; on-site by mutual agreement
- Third-party audit report (`[SOC 2 Type I/II when available]`) may satisfy request

**Remediation:** Material deficiencies remediated within `[REMEDIATION_DAYS]` days with written corrective action plan.

**CCPA audit (CPRA):** Business may take reasonable steps to ensure Architekt uses PI consistent with Business's instructions, including contractual audit rights per CPRA service provider requirements.

---

## Signatures

| | Business (Controller) | Architekt (Service Provider) |
|---|----------------------|------------------------------|
| **Name** | `[SIGNATORY_NAME]` | `[SIGNATORY_NAME]` |
| **Title** | `[TITLE]` | `[TITLE]` |
| **Date** | `[DATE]` | `[DATE]` |
