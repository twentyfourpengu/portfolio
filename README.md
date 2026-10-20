# IT Security Portfolio — Hands-on Labs

> Practical cybersecurity labs from my training, documented as reproducible change records
> and reports. Each project follows the flow of a real work assignment:
> **Goal → Execution → Verification → Documentation.**

This repository bundles four guided hands-on labs that together cover a large part of the
attack-and-defense chain — from passive information gathering, through the exploitation of a
vulnerable web application, to attack detection in a SIEM and the hardening of Windows
endpoints.

All exercises were performed exclusively in **isolated, authorized lab environments** or
against targets **explicitly approved for educational use**

---

## Contents

| # | Project | Phase | Focus | Core Tools |
|---|---------|-------|-------|------------|
| 1 | [Reconnaissance](#1-reconnaissance--passive-information-gathering) | Recon | OSINT, DNS, whois | `ip`, `ping`, `whois`, `nslookup`, `dig` |
| 2 | [Penetration Testing](#2-penetration-testing--exploiting-a-web-app) | Exploitation (Red Team) | Web vulnerabilities, reverse shell | `curl`, `msfvenom`, `msfconsole`, DVWA |
| 3 | [Incident Response – Detection](#3-incident-response--detection-with-wazuh) | Detection (Blue Team) | SIEM, MITRE ATT&CK | Wazuh, `hydra`, `mount.cifs` |
| 4 | [Firewall Implementation](#4-firewall-implementation--host-hardening) | Hardening (Blue Team) | Host firewall, network rules | Windows Defender Firewall |
| 5 | [Honeypot](#5-honeypot--deception-based-detection) | Detection (Blue Team) | Deception, connection logging | Pentbox 1.8, Kali Linux |
| 6 | [Steganography](#6-steganography--hiding-data--steganalysis) | Exfiltration & Forensics | Data hiding, steganalysis | Python, Pillow (self-built LSB tool) |
**End-to-end narrative:** first reconnoiter → then attack → then detect the attack in the
SIEM → then harden the host so the attack no longer works.

---

## 1. Reconnaissance — Passive Information Gathering

**Role:** Junior Cybersecurity Analyst · **Target:** scanme.nmap.org / nmap.org (authorized)

Structured information gathering as the first phase of any security assessment — deliberately
limited to **passive recon** (no port scanning, no active probing).

**What I did:**
- Determined my own network identity (`ip`) and verified target reachability (`ping` with output redirected to a file)
- Analyzed domain registration via `whois` (registrar, name servers, creation/expiration dates)
- Performed DNS reconnaissance interactively (`nslookup`) and non-interactively (`dig`), including queries made directly against the **authoritative name server**
- Interpreted DNS record types: A, MX, NS, CNAME, SOA
- Practiced website observation and search-engine operators (`site:`, `filetype:`, `intitle:`, exact phrases, the `-` operator) against demo targets
- Used an OSINT lookup tool to passively fingerprint public infrastructure
- Turned findings into an analyst report and tied them to vulnerability management / third-party risk

**Skills gained:** DNS analysis, whois interpretation, OSINT fundamentals, scope discipline,
evidence-based documentation.

➡️ Details & report: [`01-reconnaissance/`](./01-reconnaissance/)

---

## 2. Penetration Testing — Exploiting a Web App

**Role:** Junior Penetration Tester · **Target:** DVWA on Metasploitable2 (host-only, isolated)

Exploitation of four vulnerability classes that appear repeatedly in real engagement reports —
and chaining them into remote code execution.

**What I did:**
- Documented a baseline and target reachability, set the DVWA security level to "low"
- **Directory Traversal:** read `/etc/passwd` outside the web root, calculating traversal depth from the server error message
- **OS Command Injection:** achieved command execution via multiple shell separators (`;`, `&&`, `|`), confirmed the web server's user context (`whoami`, `id`, `hostname`)
- **Unrestricted File Upload:** uploaded a benign file and proved it was reachable over HTTP
- Built a **PHP web shell**, deployed it through the upload, and ran commands remotely
- **Reverse Shell:** generated a PHP Meterpreter payload with `msfvenom`, configured a `multi/handler` listener, established a Meterpreter session, and fingerprinted the host (`sysinfo`, `getuid`)
- Documented the full exploitation chain with an impact statement and remediation per vulnerability

**Skills gained:** web exploitation, payload creation, Metasploit/Meterpreter, evidence
capturing, client-ready reporting, remediation reasoning (input validation, allowlisting,
least privilege).

> Aligned with CompTIA Security+ (SY0-701, 4.3) and PenTest+ (PT0-003, domains 3.0 & 4.0).

➡️ Details & report: [`02-penetration-testing/`](./02-penetration-testing/)

---

## 3. Incident Response — Detection with Wazuh

**Role:** Junior SOC Analyst · **Target:** monitored DC10 server (isolated)

A shift from the attacker's seat to the defender's: attacker actions produce near-real-time
alerts in a SIEM — the job is to detect them, map them to rule IDs, and verify them against
MITRE ATT&CK.

**What I did:**
- Authenticated to the Wazuh dashboard and filtered Security events to the DC10 agent
- Prepared a wordlist and ran an **RDP password-guessing attack** with `hydra`
- Identified the brute-force alerts (Rule ID **60122** failed logon, **92652** suspicious success) and critically assessed their MITRE mapping (T1110 family)
- Mounted the SMB admin share (`C$`) with **invalid** and **valid** credentials (`mount.cifs`) and correlated each attempt to the right alert (60122 vs. 60106, T1078 Valid Accounts)
- **Anti-forensics:** cleared the Windows Security log on DC10 (Event ID 1102) and proved Wazuh captured the deletion anyway (rule ~63103, T1070 Indicator Removal)
- Documented the full detection chain as a triage-ready report with a chronological timeline

**Skills gained:** SIEM operation, alert triage, MITRE ATT&CK mapping and critical
verification, correlating host activity to detections, understanding the value of centralized
logging.

➡️ Details & report: [`03-incident-response-detection/`](./03-incident-response-detection/)

---

## 4. Firewall Implementation — Host Hardening

**Role:** Junior IT Support Technician · **Targets:** DC10 (Windows Server 2022) & PC10 (Windows 11), isolated

Implementing an endpoint-hardening baseline with Windows Defender Firewall — following the
classic loop **find the rule → change it → verify the effect.**

**What I did:**
- Captured a baseline: ICMP and SMB working in both directions (`ping`, UNC share access)
- **Blocked inbound ICMP on DC10:** disabled the echo-request rules (ICMPv4-In / ICMPv6-In) for all profiles and verified the block (`Request timed out`)
- Created a file share on PC10 and confirmed it was reachable from DC10
- **Blocked inbound SMB / File-and-Printer-Sharing on PC10** (SMB-In, NB-Session-In, etc.) and proved the network block while local access still worked
- Cleanly restored the baseline (change hygiene) and produced a change-record report

**Skills gained:** Windows Defender Firewall with Advanced Security, rule identification by
name/protocol, profile-specific rule management, before/after evidence, working safely on a
domain controller, distinguishing host- vs. network-firewall behavior.

➡️ Details & report: [`04-firewall-implementation/`](./04-firewall-implementation/)

---


## 5. Honeypot — Deception-Based Detection

**Role:** Junior SOC Analyst · **Target:** Kali Linux honeypot (isolated lab)

Setting up a decoy service to detect and log connection attempts — flipping the defender's
perspective by making the attacker interact with a system whose only purpose is to be watched.

**What I did:**
- Deployed a **low-interaction honeypot** on port 443 using **Pentbox 1.8** on Kali Linux
- Configured it manually: opened the port, set a fake response message (`Caught You!!`), and enabled logging of intrusion attempts to a log file
- Simulated an attack by connecting to the Kali host over HTTPS (`https://<IP>`) from a browser
- Confirmed the honeypot detected and logged the access — source IP, port, and timestamp (`INTRUSION ATTEMPT DETECTED!`)
- Analyzed *why* the browser showed "Secure Connection Failed": port 443 expects a TLS handshake, but the honeypot is a plain TCP listener without encryption — yet the connection attempt was still established and recorded, which is exactly its purpose
- Documented the difference between an open TCP port and a real service, and the value of honeypots as a network early-warning system

**Skills gained:** honeypot deployment & configuration, connection logging and analysis,
understanding low-interaction deception, TCP vs. TLS/service behavior, early-warning detection
concepts.

➡️ Details & report: [`05-honeypot/`](./05-honeypot/)

---

## 6. Steganography — Hiding Data & Steganalysis

**Role:** Junior Digital Forensics Analyst · **Target:** self-built LSB tool, local test images

Closing the attack-and-defense chain on the exfiltration side: implementing a data-hiding
technique from scratch to understand it at the bit level, then switching to the forensic seat
to **make the hidden data visible** — proving that "looks identical" is not the same as
"is identical."

**What I did:**
- Explained the core idea and how it differs from cryptography: steganography hides the **existence** of a message, encryption only its **content** — and why the two are strongest combined (encrypt first, then hide)
- **Built an LSB stego tool from scratch (`stego.py`, Python + Pillow):** encodes a text message into the least-significant bits of a PNG's RGB values and reads it back, using an end-marker to delimit the payload
- Verified that the carrier image looked unchanged to the human eye, while the message was fully recoverable
- Documented the practical constraints that make the technique work or fail: **PNG only** (lossy JPEG compression destroys the payload), carrier capacity (~3 bits per pixel), and why messengers that re-compress images break the hidden data
- **Steganalysis (`vergleich.py`, Python + Pillow):** generated a difference image between the original and the stego carrier to expose exactly which pixels were modified, revealing the payload as a visible pattern
- Discussed how to make the technique less detectable (busy photographic carriers instead of flat color, spreading bits across the whole image, using only the blue channel) and the statistical/visual tells a defender looks for

**Skills gained:** LSB steganography fundamentals, bit-level data encoding, Python image
processing (Pillow), basic steganalysis via difference imaging, reasoning about covert
exfiltration channels and their detection limits.

➡️ Details & report: [`06-steganography/`](./06-steganography/)

---

---
---

## Skills Overview

**Networking & Recon:** TCP/IP, ICMP, SMB/NetBIOS, DNS (A/MX/NS/CNAME/SOA), whois, OSINT
**Offensive:** Directory Traversal, OS Command Injection, File Upload, Web Shells, Reverse Shells, Metasploit/Meterpreter, hydra
**Defensive:** SIEM (Wazuh), MITRE ATT&CK, alert triage, log analysis, host firewall hardening
**Operating Systems:** Kali Linux, Windows Server 2022, Windows 11, Metasploitable2
**Documentation:** change records, triage reports, evidence management

---

## Repository Structure

```
.
├── README.md                          # this overview
├── 01-reconnaissance/
│   ├── report.md                      # recon report                 
│   ├── screenshots/                   # target_info.txt, target_whois.txt, target_dns.txt
│   └── screenshots/
├── 02-penetration-testing/
│   ├── report.md
│   ├── payloads/                       # special.php, shell.php
│   ├── evidence/
│   └── screenshots/
├── 03-incident-response-detection/
│   ├── report.md
│   ├── evidence/                       # passlist.txt, hydra/mount output
│   └── screenshots/
└── 04-firewall-implementation/
│   ├── report.md
│   ├── commands/                       # ping output (before/after)
│   └── screenshots/
├── 05-honeypot/
│   ├── readme.md
│   ├── screenshots/                      
└── 06-steganography/
    ├── readme.md
    ├── script/                          # stego.py vergleich.py
    └── screenshots/
```

---

## Ethics & Authorization

Everything documented here was performed exclusively:

- in **isolated lab environments** (nested VMs, host-only networks with no internet access), or
- against targets **explicitly approved for educational use** by their operator
  (e.g. `scanme.nmap.org` by the Nmap Project).

**No** third-party systems were attacked, probed, or disrupted without permission. Offensive
techniques (e.g. reverse shells, brute force) are used here to understand detection and
defense. This repository contains **no working payloads or credentials targeting real
systems** — placeholder data comes from the lab instructions.

> ⚠️ Using these techniques against systems you do not own, without written authorization, is
> illegal. This portfolio exists to demonstrate learning outcomes.

---

## About Me

<!-- Customize this section: -->
Entry-level cybersecurity professional focused on blue-team work (SOC/detection, hardening)
with a solid grounding in offensive fundamentals.

- 💼 LinkedIn: https://www.linkedin.com/in/lan-anh-chung/

