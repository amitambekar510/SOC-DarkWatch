# Architecture & Infrastructure Reference

## Single OS / Single Server Feasibility

Yes — this capability can run on a single physical or virtual server for Phases 1–3. It should **not** run on a single flat OS installation. The dark web crawling activity and the SIEM/MISP data store must sit in logically separated VMs on that same server, so a compromised or flagged crawling session has no path to the MISP database or ELK integration layer holding real client data.

**Recommendation:** one server, minimum two VMs (analyst crawling VM + server/data VM), on a dedicated VLAN isolated from the production SOC network.

## Recommended Operating Systems

| Role | OS | Reference |
|---|---|---|
| Server host (MISP + integration layer) | Ubuntu Server 24.04 LTS | [Download](https://ubuntu.com/download/server) |
| Analyst crawling VM | Kali Linux (snapshot before every session) | [Download](https://www.kali.org/get-kali/) |
| High-risk / anonymous sessions | Tails OS (separate boot media, never networked to the server) | [Install Guide](https://tails.net/install/) |

## Minimum Server Specification

Sized for a single server hosting the hypervisor, the analyst VM, and the MISP/integration VM concurrently (Phases 1–3):

| Component | Specification |
|---|---|
| CPU | 8–16 vCPU (Xeon or EPYC class) |
| RAM | 32–64 GB |
| Storage | 1 TB SSD/NVMe (NVMe preferred for MISP database performance) |
| Hypervisor | [Proxmox VE](https://www.proxmox.com/en/proxmox-virtual-environment/get-started) or [VMware ESXi](https://www.vmware.com/products/esxi-and-esx.html) — VirtualBox acceptable for Phase 1 lab only |
| Network interfaces | Minimum 2 NICs — management + isolated Tor/VPN egress |
| Network placement | Dedicated VLAN, isolated from production SOC network |

## FortiGate Firewall — Required Whitelisting

### Outbound (source: isolated dark-web-lab VLAN only)

| Purpose | Destination / Rule |
|---|---|
| Tor traffic | FortiGate Application Control "Tor" signature, or scope outbound 443/9001 to this VLAN (Tor relay IPs are dynamic — static IP whitelisting won't hold) |
| VPN provider | Specific IP/port per provider (commonly UDP 1194 for OpenVPN) |
| Package/tool repos | `archive.ubuntu.com`, `security.ubuntu.com`, `pypi.org`, `files.pythonhosted.org`, `github.com`, `raw.githubusercontent.com`, `codeload.github.com` |
| MISP feeds | `circl.lu` and any subscribed MISP community feed sources ([MISP feeds reference](https://www.misp-project.org/feeds/)) |
| Breach validation | `haveibeenpwned.com` (API) |
| Time sync | NTP servers — critical for MISP/log correlation accuracy |

### Inbound

- Deny all inbound by default
- Allow management access (SSH/HTTPS) only from the designated SOC admin subnet or jump host, MFA enforced

### Segmentation Policy

- Isolated VLAN → Internet (Tor/VPN/repos): **allow**
- Isolated VLAN → internal SOC/production network: **deny by default**, except a tightly scoped rule for MISP-to-ELK event push on a specific port
- Full logging enabled on this policy set for audit and compliance trail

[FortiGate VLAN/Firewall Policy Docs](https://docs.fortinet.com/product/fortigate/)
