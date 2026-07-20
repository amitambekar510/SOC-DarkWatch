# Phase 1 — Lab Setup & Team Training

**Goal:** Build the isolated environment and get every analyst comfortable using it, before touching any client data. No live client data is used in this phase — all exercises run against your own organization's domain/infrastructure only.

**Total actions:** 26
**Exit gate:** Every analyst can independently stand up the environment, validate anonymity, and run a basic SpiderFoot scan.

---

## A. Environment Build

| # | Action Item | Reference URL | Owner | Status |
|---|---|---|---|---|
| 1 | Set up a dedicated lab machine (not an analyst work laptop) | — internal procurement | | Not started |
| 2 | Provision hypervisor host (Proxmox / ESXi for production-grade segmentation) | [Proxmox VE](https://www.proxmox.com/en/proxmox-virtual-environment/get-started) · [VMware ESXi](https://www.vmware.com/products/esxi-and-esx.html) | | Not started |
| 3 | Download Ubuntu Server 24.04 LTS ISO and verify checksum (base host OS) | [Ubuntu Server Download](https://ubuntu.com/download/server) | | Not started |
| 4 | Download Kali Linux ISO and verify checksum (analyst VM) | [Kali Linux Downloads](https://www.kali.org/get-kali/) | | Not started |
| 5 | Create Kali Linux VM (min. 8 vCPU / 16GB RAM) | [Kali in VirtualBox/VMware Docs](https://www.kali.org/docs/virtualization/) | | Not started |
| 6 | Take a clean baseline snapshot of the Kali VM (revert-to-clean point) | [VirtualBox Snapshots Docs](https://www.virtualbox.org/manual/ch01.html#snapshots) | | Not started |
| 7 | Install and configure OpenVPN client on the analyst VM | [OpenVPN Community Downloads](https://openvpn.net/community-downloads/) | | Not started |
| 8 | Test VPN connection — confirm public IP has changed | [whatismyipaddress.com](https://whatismyipaddress.com/) | | Not started |
| 9 | Install Tor Browser on the analyst VM | [Tor Browser Download](https://www.torproject.org/download/) | | Not started |
| 10 | Harden Tor Browser settings (highest security level, JS disabled, no window resizing) | [Tor Browser Security Settings Guide](https://tb-manual.torproject.org/security-settings/) | | Not started |
| 11 | Install Proxychains-ng and configure `proxychains.conf` (SOCKS5 → 127.0.0.1:9050) | [proxychains-ng GitHub](https://github.com/rofl0r/proxychains-ng) | | Not started |
| 12 | Validate Proxychains + Tor routing (test with curl/whois through the chain) | [proxychains-ng README](https://github.com/rofl0r/proxychains-ng#readme) | | Not started |
| 13 | Install Macchanger; randomize MAC address before each session | [Macchanger GitHub](https://github.com/alobbs/macchanger) | | Not started |
| 14 | Prepare Tails OS on a dedicated USB for high-risk/anonymous sessions | [Tails OS Install Guide](https://tails.net/install/) | | Not started |

## B. Tool Installation

| # | Action Item | Reference URL | Owner | Status |
|---|---|---|---|---|
| 15 | Install SpiderFoot on the Ubuntu Server host (clone repo, install requirements, launch web UI) | [SpiderFoot GitHub](https://github.com/smicallef/spiderfoot) · [Docs](https://www.spiderfoot.net/documentation/) | | Not started |
| 16 | Test SpiderFoot with a scan against your own organization's domain only | [SpiderFoot Quickstart](https://www.spiderfoot.net/documentation/#quickstart) | | Not started |
| 17 | Install TorBot on the analyst Kali VM | [TorBot GitHub](https://github.com/DedSecInside/TorBot) | | Not started |
| 18 | Install OnionScan on the analyst Kali VM | [OnionScan GitHub](https://github.com/s-rah/onionscan) | | Not started |
| 19 | Install OnionSearch on the analyst Kali VM | [OnionSearch GitHub](https://github.com/megadose/OnionSearch) | | Not started |
| 20 | Install Darkdump2 on the analyst Kali VM | [Darkdump GitHub](https://github.com/josh0xA/darkdump) | | Not started |
| 21 | Confirm each tool runs cleanly and can reach the Tor network via the configured proxy chain | — internal validation | | Not started |
| 22 | Validate anonymity — check exit node IP via check.torproject.org before any real use | [Tor Connection Check](https://check.torproject.org) | | Not started |

## C. Governance & Training

| # | Action Item | Reference URL | Owner | Status |
|---|---|---|---|---|
| 23 | Create a session-logging template (analyst, date, purpose, findings, tools used) | — internal template, see [`docs/governance.md`](docs/governance.md) | | Not started |
| 24 | Draft ground rules / acceptable-use policy (isolated VM only, no marketplace interaction, mandatory documentation) | — internal policy, see [`docs/governance.md`](docs/governance.md) | | Not started |
| 25 | Obtain legal/compliance sign-off on the lab usage policy | — internal (Legal/Compliance team) | | Not started |
| 26 | Run full team training walkthrough and hands-on exercise using only internal/own-org data | — internal | | Not started |

---

**Next:** [Phase 2 — Pilot (1 Client)](phase-2-pilot.md)
