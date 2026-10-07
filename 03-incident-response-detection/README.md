# 03 — Incident Response: Detection with Wazuh

**Role:** Junior SOC Analyst
**Type:** Unassisted, hands-on, evidence-based
**Target:** `DC10` (Windows Server, Domain Controller) — monitored host on an isolated nested-VM lab network

---

## Overview

This lab shows how a SOC analyst detects suspicious activity using a centralized SIEM. Using
**Wazuh** (open-source SIEM/XDR), I observed how attacker actions on a monitored Windows server
produce alerts in near real-time, and how those alerts map to the **MITRE ATT&CK** framework.

I played both sides. From a Kali workstation I simulated two attacker behaviors — an RDP
password-guessing attack with `hydra`, and attempts to mount a Windows admin share with both
invalid and valid credentials — then pivoted to the Wazuh dashboard to confirm each alert fired,
capture its Rule ID, and interpret the associated tactic and technique. Finally I cleared the
Windows Security log on the target and confirmed Wazuh still recorded the deletion.

The point is not to "hack" the target. It's to understand, from the defender's seat, what
attacker activity looks like in a SIEM, which rules catch it, and how to read those rules to
drive an incident response.

## Scenario

As a junior SOC analyst on day shift, I was given a guided exercise on the lab tenant before
handling production alerts. The goal: get comfortable with (1) what common attacker activity
looks like when it hits the SIEM, (2) how to read Wazuh Rule IDs and MITRE ATT&CK mappings, and
(3) why centralized logging matters when an attacker tries to cover their tracks. Deliverable:
a short triage report plus screenshots of the Wazuh alerts for each phase.

## Objectives

- Authenticate to a Wazuh dashboard and filter Security events to a single agent
- Execute an authenticated password-guessing attack with `hydra` against RDP
- Identify the Rule IDs for failed and successful logons and capture their MITRE mappings
- Mount a Windows admin share with invalid and valid credentials and observe the alerts
- Correlate host activity to SIEM alerts by Rule ID and timestamp
- Detect, from inside Wazuh, that a Windows Security log was cleared
- Explain why centralized logging defeats local log-clearing as anti-forensics
- Document the full detection chain in a triage report

## Tasks Performed

| # | Task | Detection / Technique | Evidence |
|---|------|-----------------------|----------|
| 1 | Verify the Kali workstation and reach the target | Baseline | `task01_kali_identity.txt`, `task01_terminal.png` |
| 2 | Prepare the password list (place lab password at a known line) | Attack prep | `passlist.txt`, `task02_wordlist_grep.png` |
| 3 | Authenticate to Wazuh and filter to the DC10 agent | SIEM scoping | `task03_wazuh_dc10_filter.png` |
| 4 | Run an RDP password-guessing attack with `hydra` | **Brute Force (T1110)** | `task04_hydra_output.txt`, `task04_hydra_success.png` |
| 5 | Identify brute-force alerts — Rule **60122** (failed), **92652** (suspicious success) | Alert triage | `task05_rule_60122.png`, `task05_rule_92652.png` |
| 6 | Examine + critically assess the MITRE mapping for Rule 92652 | Analyst verification | `task06_mitre_technique.png` |
| 7 | Mount `\\DC10\C$` with **invalid** credentials (Jaime) | Failed logon | `task07_mount_invalid.txt` |
| 8 | Mount `\\DC10\C$` with **valid** credentials (Administrator) | Successful logon | `task08_mount_valid.txt`, `task08_share_listing.png` |
| 9 | Correlate mounts to alerts — Rule **60122** (fail) vs **60106** (success), **T1078** | Correlation | 2 screenshots |
| 10 | Clear the Windows Security log on DC10 (Event ID 1102) | **Indicator Removal (anti-forensics)** | `task10_dc10_log_cleared.png` |
| 11 | Confirm Wazuh detected the log-clearing — Rule ~**63103**, **T1070** | SIEM resilience | `task11_wazuh_log_cleared.png` |
| 12 | Write the incident detection report (timeline, ≥2 techniques) | Reporting | `ir_detection_report.md` |

## Tools

Wazuh (SIEM/XDR dashboard) · `hydra` · `mount.cifs` (cifs-utils) · Event Viewer · Kali Linux · Windows Server

## Skills Demonstrated

SIEM authentication and event filtering · interpreting attack-tool output · alert triage by
Rule ID, Level, Description · MITRE ATT&CK mapping **and critical verification** ·
cross-referencing host activity to detections · recognizing log-clearing as anti-forensics ·
articulating the value of centralized logging · structured triage reporting for Tier-2 hand-off.

## Key MITRE ATT&CK Techniques Observed

- **T1110** — Brute Force (RDP password guessing)
- **T1078** — Valid Accounts (share mount with valid credentials)
- **T1070** — Indicator Removal / Clear Windows Event Logs

## Deliverables

`ir_detection_report.md` · `passlist.txt` · `hydra` and mount output files · screenshots per phase

## Lessons Learned

<!-- Fill in 2-3 sentences: e.g. where Wazuh's default MITRE mapping needed analyst judgement, what centralized logging would have saved. -->

---

> **Scope & authorization:** All activity targeted the lab-provided DC10 server only, on an
> isolated instructor-authorized network. No Wazuh rules/config were modified (read-only
> investigator), and the only destructive step — clearing the Security log — was an intended
> part of the exercise to prove the SIEM still captured it.
