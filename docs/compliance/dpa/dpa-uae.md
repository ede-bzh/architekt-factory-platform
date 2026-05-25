# Data Processing Agreement — United Arab Emirates (PDPL)

> **Disclaimer:** This document is a **template placeholder** for Architekt internal use only. It does **not** constitute legal advice. Have qualified counsel review before execution. See [`docs/COMPLIANCE.md`](../../COMPLIANCE.md) for regional baselines.

**Architekt** — Software Factory Platform  
Template: `docs/compliance/dpa/dpa-uae.md` | Framework: UAE Federal Decree-Law No. 45/2021 (PDPL)

---

## 1. Parties

| Role | Entity | Contact |
|------|--------|---------|
| **Data Controller** | `[CONTROLLER_LEGAL_NAME]` | `[CONTROLLER_DPO_EMAIL]` |
| **Data Processor** | **Architekt** (`[ARCHITEKT_LEGAL_ENTITY]`) | `[ARCHITEKT_DPO_EMAIL]` |

**Effective date:** `[EFFECTIVE_DATE]`  
**Governing jurisdiction:** `[UAE_EMIRATE / DIFC / ADGM as applicable]`  
**Agreement term:** Co-terminous with `[MSA_REFERENCE]`.

---

## 2. Scope

**Subject matter:** Processing of personal data by Architekt as Processor on behalf of the Controller for `[SERVICE_DESCRIPTION]`.

**Duration:** Term of the services agreement plus any agreed transition period.

**Nature and purpose of processing:**

- `[PURPOSE_1 — e.g., multi-agent software delivery platform]`
- `[PURPOSE_2 — e.g., mission orchestration and project artifacts]`

**PDPL alignment (placeholder):**

- Processing based on documented, granular consent or other lawful basis as determined by Controller.
- Data subject rights supported: access, rectification, erasure, portability (as applicable under PDPL).
- **Data residency:** For UAE clients in regulated sectors, hosting in UAE or approved GCC region: `[HOSTING_REGION — e.g., Azure UAE North, AWS Bahrain, G42 Cloud]`.

**Controller instructions:** Architekt processes personal data only per Controller's documented instructions and applicable UAE law.

---

## 3. Subprocessors

| Subprocessor | Service | Location | PDPL transfer basis |
|--------------|---------|----------|---------------------|
| `[SUBPROCESSOR_1]` | `[e.g., IaaS]` | `[UAE / GCC / specify]` | `[adequacy / contractual safeguards]` |
| `[SUBPROCESSOR_2]` | `[e.g., LLM API]` | `[region]` | `[TIA / approval reference]` |

**Cross-border transfers:** Transfers outside the UAE require restrictions and specific mechanisms under PDPL. Document approved mechanism: `[TRANSFER_MECHANISM — e.g., UAE-approved SCC equivalent, regulatory approval ref]`.

**Prior authorization:** `[GENERAL / SPECIFIC]` authorization model for subprocessors as agreed in Annex `[SUBPROCESSOR_ANNEX]`.

**Notification:** `[NOTICE_DAYS]` days' notice before changes; Controller may object on PDPL-related grounds.

**Subprocessor list:** `[SUBPROCESSOR_LIST_URL_OR_ANNEX]`

---

## 4. Data Categories

| Category | Examples | Sensitive / special |
|----------|----------|---------------------|
| Identity | Name, email, employee ID | No |
| Professional | Role, department, project membership | No |
| Content | Source code, specifications, agent transcripts | `[PII embedded: YES/NO]` |
| Technical | Logs, session metadata, IP | No |
| `[SECTOR_SPECIFIC]` | `[e.g., financial, government identifiers]` | `[specify PDPL category]` |

**Data subjects:** `[EMPLOYEES / CUSTOMERS / CITIZENS — define per engagement]`

**Localization note:** Interfaces for UAE public-facing deployments support **Arabic (RTL)** per Architekt regional UX baseline.

**Excluded data:** `[PROHIBITED — e.g., health records, minors' data without explicit scope]`

---

## 5. Retention

| Data type | Retention | Post-termination |
|-----------|-----------|------------------|
| Production workspace | Contract term | Export + delete within `[DELETION_DAYS]` days |
| Agent / audit logs | `[LOG_RETENTION]` | Anonymized or deleted per schedule |
| Backups | `[BACKUP_RETENTION]` | Encrypted, rolling overwrite |

**PDPL principle:** Data retained only as long as necessary for the specified purpose. Controller may request early deletion subject to legal hold.

**Return / destruction:** Upon termination, Architekt returns or securely destroys personal data and certifies deletion unless retention is required by UAE law.

---

## 6. Security Measures

Architekt maintains technical and organizational measures appropriate to PDPL and sector expectations, including:

- Encryption at rest and in transit for production environments
- Access control, least privilege, and authenticated API access
- Network segmentation and security headers on web surfaces
- SQL injection prevention (parameterized queries)
- Secrets externalized; no hardcoded credentials in codebase
- SBOM generation and dependency vulnerability scanning per release
- Incident response runbook aligned with `[INCIDENT_RUNBOOK_REF]`

**Sector overlays:** Additional controls for `[FINANCE / GOVERNMENT / TELECOM]` as specified in Annex `[SECTOR_ANNEX]`.

**DPO coordination:** Architekt DPO contact: `[ARCHITEKT_DPO_EMAIL]`; Controller DPO: `[CONTROLLER_DPO_EMAIL]`.

---

## 7. Breach Notification

**Personal data breach:** Any incident leading to accidental or unlawful destruction, loss, alteration, unauthorized disclosure, or access to personal data.

**Processor duties:**

1. Notify Controller without undue delay, target within **`[NOTIFICATION_HOURS — e.g., 24]`** hours of awareness.
2. Provide incident summary, affected data categories, approximate volume, containment steps, and remediation plan.
3. Preserve evidence and cooperate with Controller and UAE supervisory authority notifications.

**Regulatory notification:** Controller determines obligations toward the UAE Data Office / relevant authority. Architekt provides timely assistance.

**Emergency contact:** `[SECURITY_INCIDENT_EMAIL]` | `[UAE_LOCAL_CONTACT_IF_APPLICABLE]`

---

## 8. Audit

**Compliance evidence:** Architekt provides documentation of security measures, subprocessors, and processing activities upon reasonable request.

**Audit rights:**

- Up to **`[AUDIT_FREQUENCY — e.g., annually]`** audit or equivalent third-party attestation.
- `[ON_SITE_NOTICE_DAYS]` days' written notice for on-site reviews in `[AUDIT_LOCATION]`.
- Scope limited to systems processing Controller personal data.

**Certifications:** Where available, Architekt may provide `[ISO 27001 / SOC 2 / local attestation]` reports to satisfy audit requirements.

**Remediation:** Material gaps identified during audit to be remediated within `[REMEDIATION_DAYS]` days with a corrective action plan.

---

## Signatures

| | Data Controller | Architekt (Processor) |
|---|-----------------|----------------------|
| **Name** | `[SIGNATORY_NAME]` | `[SIGNATORY_NAME]` |
| **Title** | `[TITLE]` | `[TITLE]` |
| **Date** | `[DATE]` | `[DATE]` |
