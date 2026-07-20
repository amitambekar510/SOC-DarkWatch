# SOC-DarkWatch

**An open-source Dark Web Monitoring capability for SOC teams — built on free/open-source OSINT tooling, integrated with ELK SIEM and FortiGate firewall infrastructure.**

Detects exposed credentials, leaked data, and brand/executive mentions on the dark web, and routes confirmed findings through a standard SOC alerting and client-notification workflow. Designed as a phased, reproducible build plan that any SOC team can adopt — from lab setup through full multi-client production rollout.

## Why This Project

Most dark web monitoring capability is locked behind expensive commercial platforms. This project documents a complete, phased path to standing up an equivalent capability using free and open-source tools — SpiderFoot, TorBot, OnionScan, OnionSearch, and MISP — integrated into a real SOC pipeline (ELK for detection/alerting, FortiGate for network segmentation and egress control).

## Stack

| Layer | Tooling |
|---|---|
| SIEM | ELK Stack |
| Firewall | FortiGate |
| Correlation / threat intel | MISP |
| OSINT scanning | SpiderFoot |
| Dark web crawling | TorBot, OnionSearch, Darkdump2 |
| Site validation | OnionScan |
| Anonymity layer | Tor, Tails OS, Proxychains-ng, Macchanger, OpenVPN |

## Architecture Summary

| Layer | Recommendation |
|---|---|
| Server host OS | Ubuntu Server 24.04 LTS |
| Analyst crawling VM | Kali Linux (snapshot before every session) |
| High-risk sessions | Tails OS (separate boot media, air-gapped from server) |
| Hypervisor | Proxmox / VMware ESXi (VirtualBox for lab-only) |
| Minimum server spec | 8–16 vCPU, 32–64 GB RAM, 1 TB SSD/NVMe, 2 NICs, dedicated VLAN |
| Firewall | FortiGate — isolated VLAN, outbound-only allowlist, deny-all inbound except MFA'd management access |

See [`docs/architecture.md`](docs/architecture.md) for full server sizing and FortiGate whitelisting rules.

## Index — Phases

| Phase | File | Focus | Actions |
|---|---|---|---|
| 1 | [`phase-1-lab-setup.md`](phase-1-lab-setup.md) | Lab Setup & Team Training | 26 |
| 2 | [`phase-2-pilot.md`](phase-2-pilot.md) | Pilot (1 Client) | 17 |
| 3 | [`phase-3-integration.md`](phase-3-integration.md) | Integration (MISP + ELK) | 13 |
| 4 | [`phase-4-scale.md`](phase-4-scale.md) | Scale to All Clients | 13 |
| — | [`docs/architecture.md`](docs/architecture.md) | Server, OS, firewall reference | — |
| — | [`docs/governance.md`](docs/governance.md) | Ground rules & tool reference | — |

**Total action items: 69**

Each phase file contains a checklist table with: action item, reference URL (where applicable), owner, and status columns — check items off as you progress.

## How to Use This Repo

1. Work through phases sequentially — each phase file lists its exit gate at the top; don't start the next phase until the current one's gate is met.
2. Assign an owner to each action item (edit the Owner column directly in each `.md` file).
3. Update Status as `Not started` / `In progress` / `Done` / `Blocked`.
4. Legal/compliance sign-off (Phase 1) is a hard gate before any live client data is touched in Phase 2.

## Repo Structure

```
.
├── README.md                    # this file — index + overview
├── phase-1-lab-setup.md
├── phase-2-pilot.md
├── phase-3-integration.md
├── phase-4-scale.md
└── docs/
    ├── architecture.md          # OS, server spec, FortiGate rules
    └── governance.md            # ground rules + tool reference table
```

## Disclaimer

This repository is for educational and legitimate defensive security (blue team) purposes only. All dark web access described here assumes an isolated lab environment, documented authorization for any monitored domain, and legal/compliance review before use against real client or organizational data. Do not use these tools or techniques to access illegal content or interact with illicit marketplaces.

## License

MIT — see [LICENSE](LICENSE)
