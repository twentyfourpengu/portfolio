# Network Infrastructure Design for a Mid-Sized Company

**Type:** Workshop deliverable (presentation)  
**Role:** Network / Infrastructure Designer  
**Context:** End-to-end network design for a growing mid-sized company

---

## Overview

A complete design for a company network that has to support core services
(web, email, VoIP, file sharing, databases), secure remote access, and room to
grow — without letting security slow down daily operations. Each design decision
is presented as a trade-off comparison with a clearly marked chosen option.

## What it covers

- **Architecture:** three-tier (core / distribution / access) vs. collapsed-core,
  and why the three-tier design was chosen for scalability and redundancy.
- **Addressing & segmentation:** classless **VLSM** addressing with
  function-based VLANs (servers, workstations, VoIP, wireless, VPN pool), sized to
  actual host needs with room reserved for growth.
- **Switching & interfaces:** 802.1Q VLANs, voice VLANs (LLDP-MED), port security
  with sticky MAC binding; copper vs. fiber interface choices per use case.
- **Security (defense in depth):** perimeter firewall + ACLs vs. next-gen firewall
  (DPI/IPS), and local credentials vs. centralized **AAA (RADIUS/TACACS+) + MFA**.
- **Wireless & remote access:** WPA3-Enterprise wireless and a client-to-site VPN
  (IPsec/WireGuard) vs. SSH-tunnel + RDP, compared on security, scalability and UX.
- **Troubleshooting:** a structured OSI-model method with the right tool per layer
  (ping/traceroute, Nmap, Wireshark).

## Why this matters for security work

Understanding how a network is segmented, secured and monitored is exactly the
ground a penetration tester or analyst operates on — VLAN boundaries, ACLs,
firewall placement, remote-access paths and wireless posture are all attack
surface. This workshop shows I can read and reason about that environment from the
defender's side, which makes offensive work more targeted.

## Key concepts

Three-tier switching, VLSM, 802.1Q VLANs, voice VLAN, port security, stateful vs.
next-gen firewalls, AAA, MFA, WPA3-Enterprise, client-to-site VPN, OSI-based
troubleshooting.

## File

- [`Network_Infrastructure_Design.pdf`](./Network_Infrastructure_Design.pdf)

> **Note to self (fix before publishing):** on the wireless slide, the "chosen"
> WPA3-Enterprise column lists SAE/Dragonfly and Enhanced Open (OWE). Those belong
> to WPA3-Personal / Open. WPA3-Enterprise uses 802.1X/EAP and adds an optional
> 192-bit mode (AES-GCMP-256) — align this with the AAA + MFA section. Also,
> Nmap scanning is active, not passive.
