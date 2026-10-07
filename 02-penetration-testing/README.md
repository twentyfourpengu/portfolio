# 02 — Penetration Testing Against a Vulnerable Web Application

**Role:** Junior Penetration Tester
**Type:** Unassisted, hands-on, evidence-based
**Target:** DVWA (Damn Vulnerable Web Application) on a Metasploitable2 LAMP VM — isolated on a VMware host-only network (VMnet1)

---

## Overview

This lab is supervised, hands-on practice exploiting a deliberately vulnerable web application.
It works through four vulnerability classes that appear repeatedly in real engagement reports —
**directory traversal, OS command injection, unrestricted file upload, and post-exploitation via
a reverse shell** — and chains them into remote code execution. The point is not to memorize
payloads but to build the muscle memory of how each weakness is identified, exploited, and
chained into something more dangerous, then documented for a client.

All exploitation used **real tools and real payloads** (`msfvenom`, `msfconsole`, `nc`-style
listeners). Scope was strict: only the DVWA target at the lab-provided IP, only the "low"
security level, only the four named vulnerability classes. A second VM (BadStore) on the same
network was explicitly **out of scope** and left untouched.

## Scenario

A security consultancy was contracted for a black-box web application assessment of a client's
customer-facing portal. Before going live against production, the team lead asked me to walk
through the same exploitation chain on the firm's internal training target (DVWA) to sign off
on technical readiness. The deliverable: the zipped lab folder — payloads, screenshots,
command transcripts, and a one-page report.

## Objectives

- Authenticate to a target web app and verify its security posture
- Identify directory traversal by manipulating URL parameters and reading server errors
- Exploit OS command injection with shell separators and capture command output
- Demonstrate unrestricted file upload and retrieve the file over HTTP
- Build a minimal PHP command shell and deploy it through the upload form
- Generate a PHP Meterpreter reverse shell with `msfvenom` (correct `LHOST`/`LPORT`)
- Configure a Metasploit `multi/handler` listener and establish a Meterpreter session
- Document the full exploitation chain with impact and mitigations

## Tasks Performed

| # | Task | Technique | Evidence |
|---|------|-----------|----------|
| 1 | Confirm workstation identity and target reachability | Baseline | `task01_baseline.txt`, `task01_baseline.png` |
| 2 | Authenticate to DVWA and set security to "low" | Setup | `task02_dvwa_security_low.png` |
| 3 | Read `/etc/passwd` outside the web root | **Directory Traversal** | `task03_passwd_dump.txt`, `task03_traversal_notes.txt`, screenshot |
| 4 | Run `whoami` / `id` / `hostname` via injection (multiple separators) | **OS Command Injection** | `task04_command_injection.txt`, `task04_injection_whoami.png` |
| 5 | Upload a benign file and retrieve it over HTTP | **Unrestricted File Upload** | `task05_upload_path.txt`, 2 screenshots |
| 6 | Build and deploy a minimal PHP web shell | **Web Shell / RCE** | `special.php`, `task06_shell_commands.txt`, screenshot |
| 7 | Generate a PHP Meterpreter reverse shell | **Payload Creation** | `shell.php`, `task07_msfvenom_output.txt`, screenshot |
| 8 | Configure a `multi/handler` listener | **Listener Setup** | `task08_handler.txt`, screenshot |
| 9 | Upload + trigger the reverse shell → Meterpreter session | **Reverse Shell** | `task09_session_opened.png` |
| 10 | Fingerprint the host (`sysinfo`, `getuid`) and write the report | **Post-Exploitation + Reporting** | `task10_meterpreter.txt`, report, screenshot |

## Tools

`curl` · `msfvenom` · `msfconsole` / `multi/handler` · Meterpreter · Firefox · DVWA · Metasploitable2 · Kali Linux

## Skills Demonstrated

Web exploitation (traversal, injection, upload) · web shell construction · payload generation ·
Metasploit/Meterpreter workflow · exploitation chaining · forensic evidence capture ·
client-ready reporting · remediation reasoning (input validation, allowlisting, least privilege).

> Aligned with CompTIA Security+ (SY0-701, 4.3) and PenTest+ (PT0-003, domains 3.0 & 4.0).

## Deliverables

`pentest_lab_report` · command transcripts in `evidence/` · payloads in `payloads/` · screenshots per task

## Lessons Learned

<!-- Fill in 2-3 sentences: what surprised you, what took longer than expected, what you'd do differently. -->

---

> ⚠️ **Scope & authorization:** All exploitation was performed against a deliberately vulnerable
> training target on an isolated host-only network, authorized for enrolled learners. No
> out-of-scope hosts were touched, no lateral movement beyond the initial session. The payloads
> in this folder are **non-functional against real systems** without lab-specific parameters.
