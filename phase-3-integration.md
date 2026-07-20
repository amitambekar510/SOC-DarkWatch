# Phase 3 — Integration (MISP + ELK SIEM)

**Goal:** Turn the manual pilot process into an automated, repeatable SOC pipeline, fully integrated with the existing ELK stack.

**Total actions:** 13
**Exit gate:** A simulated finding flows automatically from scan to client notification with no manual steps missed.

**Previous:** [Phase 2 — Pilot (1 Client)](phase-2-pilot.md)

---

| # | Action Item | Reference URL | Owner | Status |
|---|---|---|---|---|
| 1 | Stand up a MISP instance on the Ubuntu Server host (dedicated VM) | [MISP Install/Download Docs](https://www.misp-project.org/download/) | | Not started |
| 2 | Configure MISP taxonomies/tags for dark web exposure categories | [MISP Taxonomies](https://www.misp-project.org/taxonomies.html) | | Not started |
| 3 | Build the automation link: SpiderFoot output → MISP (script or API) | [MISP Automation/API Docs](https://www.misp-project.org/openapi/) | | Not started |
| 4 | Configure ELK (Filebeat/Logstash) to ingest MISP indicators | [Elastic Filebeat](https://www.elastic.co/beats/filebeat) · [Logstash](https://www.elastic.co/logstash) | | Not started |
| 5 | Build a per-client dashboard in Kibana | [Kibana Dashboards Docs](https://www.elastic.co/guide/en/kibana/current/dashboard.html) | | Not started |
| 6 | Configure severity-based alert rules in ELK | [Elastic Alerting Docs](https://www.elastic.co/guide/en/kibana/current/alerting-getting-started.html) | | Not started |
| 7 | Integrate alerting with the existing ticketing system (auto-create ticket on confirmed hit) | — internal, depends on ticketing platform in use | | Not started |
| 8 | Define SLA matrix per severity (e.g., Critical = notify client within 4 hours) | — internal | | Not started |
| 9 | Build/automate the client notification workflow | — internal | | Not started |
| 10 | Run an end-to-end test: simulate a finding and verify it flows scan → MISP → ELK → ticket → notification | — internal QA | | Not started |
| 11 | Document the full workflow in a runbook/internal wiki page | — internal | | Not started |
| 12 | Train the full SOC team on the integrated pipeline | — internal | | Not started |
| 13 | Set up scheduled scan automation (cron/scheduler) ready for multi-client scale | [cron Manual](https://man7.org/linux/man-pages/man5/crontab.5.html) | | Not started |

---

**Next:** [Phase 4 — Scale to All Clients](phase-4-scale.md)
