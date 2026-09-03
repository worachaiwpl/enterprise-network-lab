# Enterprise Network Lab

A hands-on network engineering project built in EVE-NG, going beyond CCNA fundamentals to model patterns used in real enterprise networks: redundant edge and core layers, dynamic routing, gateway and link redundancy, a real firewall, 802.1X authentication, and config automation.

This is a companion project to [`ccna-labs`](https://github.com/worachaiwpl/ccna-labs), which covers the CCNA fundamentals (VLANs, NAT, static/multi-site routing, site-to-site VPN, ACLs) in Cisco Packet Tracer. This repo picks up from there and rebuilds on EVE-NG, using real vendor images instead of a simulator, to cover what Packet Tracer can't: EtherChannel, HSRP, a real firewall, and 802.1X/RADIUS.

See [`roadmap.md`](./roadmap.md) for the full milestone plan, target topology, and IP addressing scheme.

## What this project covers

| Milestone | Topic | Status |
|---|---|---|
| 01 | OSPF (replacing static routing) | ⬜ In progress |
| 02 | HSRP — redundant gateway on the core layer | ⬜ Planned |
| 03 | EtherChannel (LACP) — link aggregation | ⬜ Planned |
| 04 | STP / RSTP — loop prevention on redundant links | ⬜ Planned |
| 05 | Firewall (FortiGate / ASAv) — replacing router ACLs | ⬜ Planned |
| 06 | RADIUS (802.1X) — port-based authentication | ⬜ Planned |
| 07 | Network automation (Netmiko) — scripted config instead of manual CLI | ⬜ In progress, threaded through every milestone |

## Design highlights

- **Redundant HQ edge** — dual ISP uplinks into a single edge router with failover routing
- **Redundant core** — two Layer 3 switches running HSRP so a core switch failure doesn't take down the gateway
- **Redundant access layer** — two access switches with LACP-bonded uplinks to the core, protected from loops by STP
- **Branch office over VPN** — a smaller, single-uplink branch site connected to HQ over an IPsec tunnel
- **Automation-first** — base device configuration is pushed with Python (Netmiko) rather than typed manually, starting from the very first lab

Full topology diagram and IP addressing table are in `roadmap.md`.

## Tools used

- EVE-NG (Community Edition)
- Cisco IOS / IOL images
- Python + Netmiko
- FortiGate or Cisco ASAv (from milestone 05 onward)

## Repo structure

Each milestone folder contains:
- `topology.png` — the relevant slice of the network for that lab
- `configs/` — device running-configs
- `notes.md` — what was built, why, and any troubleshooting encountered

## About this project

This is being built incrementally, one working milestone at a time, as part of ongoing network engineering practice. Each stage is tested and documented before moving to the next — the goal is a portfolio that shows real troubleshooting and design reasoning, not just copied configs.
