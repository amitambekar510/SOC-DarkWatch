# Phase 4 — Scale to All Clients

**Goal:** Roll out across the full SOC client base and establish stable, ongoing operations.

**Total actions:** 13
**Exit gate:** Stable, monitored, recurring operations across all clients with tracked metrics.

**Previous:** [Phase 3 — Integration (MISP + ELK SIEM)](phase-3-integration.md)

---

| # | Action Item | Reference URL | Owner | Status |
|---|---|---|---|---|
| 1 | Onboard each remaining client (repeat authorization + scoping step per client) | — internal | | Not started |
| 2 | Configure SpiderFoot scan targets for every onboarded client | [SpiderFoot Docs](https://www.spiderfoot.net/documentation/) | | Not started |
| 3 | Set scan cadence per client tier (e.g., critical clients weekly, others bi-weekly) | — internal | | Not started |
| 4 | Monitor false-positive rates across all clients; continue tuning modules | — internal | | Not started |
| 5 | Map coverage gaps — note what free tools miss (private forums, Telegram, closed marketplaces) | — internal | | Not started |
| 6 | Evaluate paid feeds for gap coverage — cost/benefit review | [SOCRadar](https://socradar.io/) · [Flare](https://flare.io/) · [SpyCloud](https://spycloud.com/) | | Not started |
| 7 | Build a recurring client reporting cadence (monthly summary reports) | — internal | | Not started |
| 8 | Conduct quarterly runbook/playbook review and update | — internal | | Not started |
| 9 | Onboard and train any new analysts joining the SOC team | — internal | | Not started |
| 10 | Track ongoing metrics: mean time to detect, mean time to notify, true/false positive ratio | — internal, dashboard in Kibana | | Not started |
| 11 | Review and refresh legal/compliance policy annually | — internal (Legal/Compliance) | | Not started |
| 12 | Rotate/refresh lab VM snapshots and tool versions periodically (patch management) | [Ubuntu Security Notices](https://ubuntu.com/security/notices) · [Kali Updates](https://www.kali.org/blog/) | | Not started |
| 13 | Conduct a post-scale retrospective — capture lessons learned, update SOPs | — internal | | Not started |

---

**Previous phase:** [Phase 3 — Integration](phase-3-integration.md) · **Back to:** [Project Index](README.md)
