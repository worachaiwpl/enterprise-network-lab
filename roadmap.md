# Enterprise Network Simulation — Project Roadmap

A long-running EVE-NG project built alongside CCNA study, growing from a simple HQ/Branch topology into a more realistic enterprise design. Built incrementally — each milestone is a complete, working lab before the next one starts.

**Note on rebuild:** Milestones 1–5 were originally built in Cisco Packet Tracer and stay archived as-is in the repo — they prove the fundamentals. Milestone 6 onward (OSPF, HSRP, EtherChannel, STP, and everything in Phase 2) is a fresh build in EVE-NG on the topology shown in the diagram, because Packet Tracer can't reliably run EtherChannel, real firewall images, or 802.1X/RADIUS.

## Guiding principle

Every milestone must:
1. Build on the previous one (never restart from scratch)
2. End in a working, testable state (ping/traceroute proof, `show` command output)
3. Get committed to GitHub with its own folder, config files, and notes.md
4. Include at least one troubleshooting case in its notes

## Automation thread (runs alongside every milestone, not just at the end)

Originally automation was planned as a single Phase 2 milestone. Instead, it's threaded through the whole rebuild using **Netmiko** (Python), starting from the very first base-config step:

| When | What automation does |
|---|---|
| Before topology build | Set up Python + Netmiko, confirm the host machine can reach EVE-NG management network |
| Milestone 2 (base IP) | Script pushes base interface IPs to every device instead of typing manually |
| Milestones 6–9 (OSPF, HSRP, EtherChannel, STP) | Configured manually first (to build real understanding), then a script backs up each device's running-config automatically after the lab passes |
| Milestone 12 | Level up to Jinja2 templates for config generation, then migrate the same workflow to Ansible |

This keeps automation visible in the portfolio from lab 1 onward, rather than as one isolated late-stage project.

---

## Phase 1 — CCNA exam topics (core network layer)

Goal: a working multi-site network covering everything CCNA tests, built on real hardware-style topology instead of a single flat router.

| # | Milestone | Status | Adds |
|---|---|---|---|
| 1 | VLAN segmentation + inter-VLAN routing | ✅ Done | Router-on-a-Stick, 3 VLANs |
| 2 | NAT / PAT | ✅ Done | Internet access for internal hosts |
| 3 | Multi-site static routing | ✅ Done | HQ – ISP – Branch, default routes |
| 4 | Site-to-site VPN (IPsec) | ✅ Done | Encrypted tunnel HQ ↔ Branch |
| 5 | Extended ACL | ✅ Done | Department-level access control |
| 6 | **OSPF** | ⬜ Next | Replace static routes, multi-area if time allows |
| 7 | **HSRP** | ⬜ Planned | Redundant gateway on core layer |
| 8 | **EtherChannel (LACP)** | ⬜ Planned | Aggregated, redundant links between switches |
| 9 | **STP / RSTP** | ⬜ Planned | Loop prevention across redundant switch links |

**Phase 1 exit criteria:** two redundant core switches, two access switches with redundant uplinks, OSPF routing between HQ/Branch/ISP, VPN and NAT still working on top of the new routing.

---

## Phase 2 — Beyond CCNA (portfolio differentiators)

Goal: add the pieces that separate a CCNA-only portfolio from one that looks like it belongs in a real NOC.

| # | Milestone | Status | Adds |
|---|---|---|---|
| 10 | Firewall (FortiGate or ASAv) | ⬜ Planned | Replace router ACLs with zone-based policy + VPN moved to firewall |
| 11 | RADIUS (802.1X) | ⬜ Planned | Port-based authentication before a device can join the LAN |
| 12 | Network automation (Python/Netmiko) | ⬜ Planned | Script-driven config push instead of manual CLI |

Stretch goals if there's appetite after #12: TACACS+ for admin access control, syslog server, SNMP monitoring (LibreNMS), WLC + AP for wireless with WPA2-Enterprise.

---

## Target topology (Phase 1 exit state)

See the network diagram shared alongside this document. Summary of the design:

- **HQ site**: dual-ISP edge router → core switch pair (HSRP) → two access switches (EtherChannel uplinks, STP for loop safety) → VLANs 10/20/30 (Sales/IT/HR)
- **Branch site**: single ISP link → branch router (NAT + VPN endpoint) → flat LAN
- **Routing**: OSPF between HQ, ISP, and Branch (replacing the static/default routes used in milestones 1–5)
- **VPN**: IPsec tunnel between HQ and Branch, unaffected by the routing protocol change

## IP addressing scheme

| Segment | Subnet |
|---|---|
| HQ – Sales (VLAN 10) | 10.1.10.0/24 |
| HQ – IT (VLAN 20) | 10.1.20.0/24 |
| HQ – HR (VLAN 30) | 10.1.30.0/24 |
| HQ – Management (VLAN 99) | 10.1.99.0/24 |
| Core-SW1 ↔ Core-SW2 (HSRP peer link) | 10.1.254.0/30 |
| Branch LAN (VLAN 100) | 10.2.100.0/24 |
| HQ ↔ ISP-A (WAN) | 203.0.113.0/30 |
| HQ ↔ ISP-B (WAN) | 203.0.114.0/30 |
| Branch ↔ ISP (WAN) | 203.0.115.0/30 |

## Repo structure convention

This project lives in its own repo, separate from the original `ccna-labs` repo (which holds the Packet Tracer fundamentals — VLAN, NAT, multi-site routing, VPN, ACL — and stays untouched):

```
enterprise-network-lab/
├── README.md
├── roadmap.md              ← this file
├── automation/              ← Netmiko scripts, used from milestone 1 onward
├── 01-ospf/
├── 02-hsrp/
├── 03-etherchannel/
├── 04-stp/
├── 05-firewall/
├── 06-radius-8021x/
└── 07-network-automation/
```

## How to use this document

Update the status column as each milestone finishes (⬜ → ✅). Keep this file at the repo root so anyone browsing the project — including you, six months from now — can see the plan and progress at a glance.
