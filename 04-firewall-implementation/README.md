# 04 — Implementing a Firewall: Controlling Host-Based Traffic on Windows

**Role:** Junior IT Support Technician
**Type:** Unassisted, hands-on, evidence-based
**Targets:** `DC10` (Windows Server 2022, Domain Controller) · `PC10` (Windows 11) — nested VMs on an isolated lab network (10.10.10.0/24)

---

## Overview

This lab is about using **Windows Defender Firewall with Advanced Security** to control inbound
network traffic on Windows endpoints. I started by validating that two hosts on the same network
could communicate freely, then progressively tightened the firewall to block specific protocols,
and verified that each policy change produced the expected behavior on the wire.

Host-based firewalls are one of the most common controls a junior technician configures, audits,
or troubleshoots. Whether a ticket says "I can't reach the file share" or a security review says
"ICMP must be denied on all servers," the same loop applies: **identify the rule, change it, and
confirm the change took effect.** This lab practices that loop in a controlled environment.

## Scenario

At a mid-sized accounting firm, the security team's new endpoint baseline required two things,
to be piloted on two staging machines before a fleet-wide rollout:

1. **Block inbound ICMP echo requests** on the domain controller, so it doesn't respond to ping sweeps from the user subnet.
2. **Block inbound SMB / file-and-printer-sharing** on client workstations, so users can't host ad-hoc shares from their own machines.

The job: validate the "before" state, apply each change, re-test after each change, restore the
baseline, and document everything so the next technician on rotation can repeat it.

## Objectives

- Verify baseline ICMP connectivity between two hosts with `ping` (both directions)
- Identify the exact inbound rules governing ICMPv4 and ICMPv6 echo requests
- Block inbound ICMP echo on DC10 for all network profiles
- Validate the change by re-running connectivity tests and observing the new behavior
- Create a Windows file share and verify it's reachable from a second host
- Disable the inbound SMB / File-and-Printer-Sharing rules to block remote share access
- Document every change with timestamped screenshots and a change-record report

## Tasks Performed

| # | Task | Change / Check | Evidence |
|---|------|----------------|----------|
| 1 | Verify baseline ICMP: PC10 → DC10 | Before state | `task01_ping_pc10_to_dc10.txt`, `task01_baseline_ping.png` |
| 2 | Verify baseline ICMP: DC10 → PC10 | Before state (reverse) | `task02_ping_dc10_to_pc10.txt`, screenshot |
| 3 | Locate the ICMP echo-request inbound rules on DC10 | Identification only | `task03_icmp_rules_located.png` |
| 4 | Disable ICMPv4-In + ICMPv6-In echo rules (all profiles) | **Block ICMP** | `task04_icmp_rules_disabled.png` |
| 5 | Re-test ping → confirm `Request timed out` | Verify block | `task05_ping_after_block.txt`, `task05_ping_blocked.png` |
| 6 | Create and share `C:\LABFILES` on PC10 | Build SMB target | `task06_share_created.png` |
| 7 | Access `\\PC10\LABFILES` from DC10 | Before state (SMB) | `task07_share_accessible.png` |
| 8 | Disable SMB-In + NB-Session-In (and related) rules on PC10 | **Block SMB** | `task08_smb_rules_disabled.png` |
| 9 | Re-test share access from DC10 → confirm network error | Verify block | `task09_share_blocked.png` |
| 10 | Restore baseline (re-enable rules) + complete the change record | Change hygiene | `task10_restored_ping.png`, `task10_restored_share.png`, report |

## Tools

Windows Defender Firewall with Advanced Security · `ping` · File Explorer / UNC paths · Command Prompt · VMware Workstation (nested VMs)

## Skills Demonstrated

Navigating Windows Defender Firewall with Advanced Security · identifying built-in inbound rules
by name and protocol · profile-specific rule management · interpreting "Request timed out" vs.
"Reply from" · creating and testing SMB shares · recognizing the multiple sub-rules behind SMB
traffic (SMB-In, NB-Session-In, NB-Datagram-In) · before/after evidence capture · working safely
on a domain controller · distinguishing host-based from network-firewall behavior · change
hygiene (restoring the environment) and handover documentation.

## Deliverables

`firewall_lab_report.docx` · `ping` command outputs (before/after) in `commands/` · 11 screenshots per task

## Lessons Learned

<!-- Fill in 2-3 sentences: e.g. how many rule instances actually had to be disabled per profile, why a timeout differs from "destination unreachable". -->

---

> **Scope & authorization:** All changes were made to local Windows Defender Firewall rules on
> the two lab-owned nested VMs (DC10 and PC10), pre-authorized for the exercise. The firewall
> service was never disabled, Group Policy was not modified, and rules were **disabled, not
> deleted**, so they could be cleanly restored afterward.
