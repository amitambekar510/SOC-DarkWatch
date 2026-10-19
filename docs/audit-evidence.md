# SOC-DarkWatch — audit evidence checklist

This is a **preparation template**, not proof of implementation. Each record needs a control owner, effective date, review cadence and reviewer sign-off.

| ID | Evidence artifact | What to record | Status |
|---|---|---|---|
| DW-01 | Monitoring scope and authorization | Approved domains/brands, legal basis, monitoring boundaries, owner | Not started |
| DW-02 | Existing security tool inventory | SIEM, firewall, TI, ticketing, compute and current license scope | Not started |
| DW-03 | Threat monitoring SOP | Authorized sources, cadence, analyst steps, validation criteria | Not started |
| DW-04 | Network isolation evidence | Approved firewall policy, egress review, lab separation | Not started |
| DW-05 | Source coverage and limitations | Free-source blind spots, rate limits, confidence and provenance | Not started |
| DW-06 | Synthetic detection demonstration | Fictional indicator through review, enrichment, SIEM and case | Not started |
| DW-07 | Operational scan/review records | Time, owner, scope, source, result, exception | Not started |
| DW-08 | Finding validation | Evidence provenance, false-positive checks, confidence and severity | Not started |
| DW-09 | Case escalation and response | Ticket ID, timestamps, assignee, response and closure | Not started |
| DW-10 | Remediation verification | Password resets or other actions, approved redacted proof | Not started |
| DW-11 | Access, privacy and retention | Least privilege, redaction, secure storage, retention approval | Not started |
| DW-12 | Governance and management review | KPI report, training, exceptions, risk acceptance, sign-off | Not started |
| DW-13 | Applicability and control mapping | Exact applicable regulation, version, clause and evidence link | Not started |

## Recommended sample case schema

```json
{
  "case_id": "DEMO-DW-0001",
  "data_classification": "SYNTHETIC",
  "finding_type": "possible-credential-exposure",
  "monitored_asset": "example.invalid",
  "source_category": "authorized-public-source",
  "observed_at_utc": "2026-10-01T10:00:00Z",
  "validation_status": "unconfirmed",
  "confidence": "low",
  "triage_owner": "SOC-demo",
  "ticket_reference": "DEMO-CASE-1",
  "response_status": "awaiting-review",
  "evidence_reference": "redacted-demo-only"
}
```

Never publish real credentials, breach dumps, personally identifiable data or unredacted client information. Maintain an internal, access-controlled evidence repository; public GitHub examples should remain fictional. Maintain an explicit audit gap log: missing artifacts must stay marked **Not started / In progress / Blocked** rather than being silently counted as compliant.
