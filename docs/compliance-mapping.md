# Regulatory and framework applicability matrix — SOC-DarkWatch

**Status:** Interpretive mapping for control design and audit evidence. **Not a legal opinion, compliance certification, or assertion that dark-web monitoring is expressly mandated.** Verify current circulars, amendments, applicability, contractual obligations and evidence expectations with legal/compliance and the responsible auditor before claiming alignment.

| # | Reference | Scope / relevance to proposed monitoring | Potential evidence | Qualification |
|---|---|---|---|---|
| 1 | CERT-In Directions (28 Apr 2022) | Incident reporting, log retention and operational response obligations for covered entities | Incident assessment, time-stamped escalations, relevant retained logs | Monitoring is a supporting detection mechanism, **not an explicit universal dark-web monitoring requirement**; follow applicable reporting clocks and record-retention rules. |
| 2 | SEBI Cybersecurity and Cyber Resilience Framework (CSCRF), 2024 | Cyber threat intelligence, detection, response, governance for applicable SEBI-regulated entities | TI review records, SOC alerts, escalations, review sign-offs | Apply relevant entity category, phase-in, subsequent circulars and contractual obligations; dark-web monitoring is **one possible source** of intelligence. |
| 3 | RBI IT Governance / Cybersecurity directions | IT governance, risk management, incident monitoring for applicable RBI-regulated entities | Threat review SOP, detection cases, risk acceptance | Different RBI directions apply to banks, NBFCs and other entities; **no single blanket RBI dark-web mandate** is claimed. |
| 4 | Digital Personal Data Protection Act, 2023 | Personal-data safeguards, breach handling and accountability where provisions are commenced and applicable | Exposure triage, personal-data minimization, response approvals | Check phased commencement, rules and exemptions; dark-web discovery is not equivalent to proving a reportable personal-data breach. |
| 5 | NSE / BSE technology / systems audit | Exchange-specific audit expectations for applicable members and intermediaries | Control mapping, monitoring evidence, ticket closure | Requirements vary by exchange, membership type, circular and audit scope; **not a universal statutory dark-web requirement**. |
| 6 | NPCI / UPI security requirements | Participant-specific ecosystem security and incident-management requirements | Exposure intelligence review, risk treatment, audit logs | Applicable only to relevant ecosystem participants and binding circulars; do not assert a universal mandate. |
| 7 | SEBI PFUTP Regulations, 2003 | Fraudulent/unfair securities-market practices; possible context for impersonation, scams and market abuse | Escalated fraud indicators, investigation referrals | **Not a cybersecurity monitoring standard**; any connection to dark-web intelligence is indirect and case-dependent. |
| 8 | ISO/IEC 27001:2022 | ISMS risk assessment/treatment, threat intelligence, monitoring, incident response and records | Risk register, Annex A control mapping, SOP, review records | Supports selected controls such as Annex A 5.7, 5.24–5.28, 8.15–8.16 where selected in the SoA; **does not itself mandate dark-web scanning**. |
| 9 | ISO/IEC 27090 | **Reference requires validation**: verify exact publication identifier, title and relevance before use | No compliance claim until verified | **Not counted as confirmed applicable coverage.** Retained as a requested placeholder; consider whether a different ISO standard was intended. |
| 10 | MITRE ATT&CK | Threat-behavior vocabulary to contextualize validated indicators and possible related techniques | Detection mapping, analyst notes, coverage matrix | ATT&CK is a knowledge base, **not a regulation or certification**; do not map a leak mention to a technique without evidence. |
| 11 | ISO/IEC 42001:2023 | AI management-system governance when AI is used for enrichment, scoring or triage | AI use-case register, validation, human oversight | **Conditional**: no AI management-system claim if no AI system is in scope. |
| 12 | NIST CSF 2.0 | Govern, Identify, Protect, Detect, Respond, Recover risk outcomes | Governed monitoring policy, detection evidence, response and recovery actions | CSF is voluntary guidance unless adopted by contract/regulator; implementation is not a NIST certification. |

## Official reference starting points

- CERT-In: https://www.cert-in.org.in/
- SEBI circulars and regulations: https://www.sebi.gov.in/
- RBI notifications: https://www.rbi.org.in/
- MeitY / Digital India legal resources: https://www.meity.gov.in/
- NSE: https://www.nseindia.com/
- BSE: https://www.bseindia.com/
- NPCI: https://www.npci.org.in/
- ISO standard catalog: https://www.iso.org/standards.html
- MITRE ATT&CK: https://attack.mitre.org/
- NIST CSF 2.0: https://www.nist.gov/cyberframework

**Audit method:** identify your legal entity and sector; confirm each source's effective version and clause; document applicability; identify an implemented control; collect dated evidence; assign control owner; record exceptions and residual risk; obtain compliance/auditor review. Do not treat the 12-row count as twelve certifications or fulfilled mandates.
