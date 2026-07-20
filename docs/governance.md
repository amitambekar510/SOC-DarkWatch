# Governance, Ground Rules & Tool Reference

## Ground Rules

These apply from Phase 1 onward and should be formalized into policy before any live client engagement (Phase 2 onward):

- All dark web access happens from the isolated VM/Tails setup only — never from analyst work laptops or any device connected to the production network
- Analysts never purchase, download, or interact with illegal content or marketplaces — passive observation and indicator collection only
- Every session is documented (analyst, date/time, purpose, tools used, findings) for legal/audit trail
- Legal/compliance sign-off is required before this capability goes live for any actual client, given the jurisdictional and liability considerations of dark web access
- Any exposure finding involving sensitive credentials, financial data, or regulated PII should be escalated at the highest severity tier regardless of source confidence
- VM snapshots are reverted to clean baseline after each high-risk session
- No client data is stored on the analyst crawling VM — findings are transferred only to the MISP/data VM after validation

## Session Log Template

| Field | Description |
|---|---|
| Analyst | Name/ID of analyst conducting the session |
| Date/Time | Start and end timestamp |
| Purpose | Client name / scan reference / investigation reason |
| Tools used | e.g., SpiderFoot, TorBot, OnionScan |
| Findings | Summary of what was found, with MISP event ID if logged |
| VM snapshot state | Confirm reverted to clean baseline post-session |

## Tool Reference Summary

| Tool | Purpose | Link |
|---|---|---|
| SpiderFoot | Automated OSINT aggregation, 200+ modules, Tor integration — primary scheduled scanner | [GitHub](https://github.com/smicallef/spiderfoot) |
| TorBot | Crawls .onion sites, maps link structures | [GitHub](https://github.com/DedSecInside/TorBot) |
| OnionScan | Flags OPSEC failures/misconfigurations on onion sites under investigation | [GitHub](https://github.com/s-rah/onionscan) |
| OnionSearch | Search engine aggregator for .onion content | [GitHub](https://github.com/megadose/OnionSearch) |
| Darkdump2 | Deep web search tool | [GitHub](https://github.com/josh0xA/darkdump) |
| Ahmia | Indexed .onion search engine (open source) | [Site](https://ahmia.fi) |
| MISP | Central indicator store and correlation platform; source of truth pushed to ELK | [misp-project.org](https://www.misp-project.org/) |
| Have I Been Pwned API | Fast first-pass breach validation for employee emails/domains | [API Docs](https://haveibeenpwned.com/API/v3) |
| Proxychains-ng | Routes tool traffic through the Tor SOCKS proxy | [GitHub](https://github.com/rofl0r/proxychains-ng) |
| Macchanger | MAC address randomization for the analyst VM | [GitHub](https://github.com/alobbs/macchanger) |
| Tails OS | Amnesic live OS for high-risk anonymous sessions | [tails.net](https://tails.net/) |

**Coverage limitation:** these free/open-source tools primarily surface public breach data and indexed onion content. Private forums, invite-only marketplaces, and Telegram-based leak channels are largely out of reach without a paid intelligence feed ([SOCRadar](https://socradar.io/), [Flare](https://flare.io/), [SpyCloud](https://spycloud.com/)) — evaluated in Phase 4.
