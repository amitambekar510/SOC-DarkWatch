# Phase 2 — Pilot (1 Client)

**Goal:** Prove the end-to-end process on a single low-risk client before scaling to the full client base.

**Total actions:** 17
**Exit gate:** Documented false-positive rate, a working triage runbook, and SOC leadership sign-off to proceed.

**Previous:** [Phase 1 — Lab Setup & Team Training](phase-1-lab-setup.md)

---

| # | Action Item | Reference URL | Owner | Status |
|---|---|---|---|---|
| 1 | Select one pilot client (low-risk, strong existing relationship) | — internal | | Not started |
| 2 | Obtain written client authorization / rules-of-engagement for monitoring their domain | — internal legal template | | Not started |
| 3 | Gather pilot scope: domains, employee emails, brand keywords, executive names | — internal | | Not started |
| 4 | Configure SpiderFoot scan targets for the pilot client | [SpiderFoot Scan Setup Docs](https://www.spiderfoot.net/documentation/#scanning) | | Not started |
| 5 | Enable relevant SpiderFoot modules (breach data, dark web search, HaveIBeenPwned, etc.) | [SpiderFoot Modules List](https://www.spiderfoot.net/documentation/#modules) | | Not started |
| 6 | Run the first scheduled scan (weekly cadence to start) | [SpiderFoot CLI/Scheduling Docs](https://www.spiderfoot.net/documentation/) | | Not started |
| 7 | Review raw output; separate signal from noise | — internal analyst review | | Not started |
| 8 | Pivot on each hit using TorBot/OnionSearch to investigate the source | [TorBot GitHub](https://github.com/DedSecInside/TorBot) · [OnionSearch GitHub](https://github.com/megadose/OnionSearch) | | Not started |
| 9 | Validate onion site legitimacy/OPSEC using OnionScan where relevant | [OnionScan GitHub](https://github.com/s-rah/onionscan) | | Not started |
| 10 | Cross-check flagged emails/credentials via the Have I Been Pwned API | [HIBP API v3 Docs](https://haveibeenpwned.com/API/v3) | | Not started |
| 11 | Log confirmed findings into a tracking sheet or test MISP instance (tagged by client) | [MISP Project](https://www.misp-project.org/) | | Not started |
| 12 | Build a first-draft triage runbook (real exposure vs. noise checklist) | — internal, see [`docs/governance.md`](docs/governance.md) | | Not started |
| 13 | Define severity tiers: Critical / High / Medium / Low | — internal | | Not started |
| 14 | Draft a client notification template for confirmed findings | — internal | | Not started |
| 15 | Run the pilot for 2–4 weeks, tracking false-positive rate | — internal | | Not started |
| 16 | Collect analyst feedback and tune scan modules/keywords accordingly | — internal | | Not started |
| 17 | Present pilot results to SOC leadership for go/no-go decision on scaling | — internal | | Not started |

---

**Next:** [Phase 3 — Integration (MISP + ELK SIEM)](phase-3-integration.md)
