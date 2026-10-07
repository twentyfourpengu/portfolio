# 01 — Reconnaissance Against an Authorized Public Target

**Role:** Junior Cybersecurity Analyst
**Type:** Unassisted, hands-on, evidence-based
**Target:** `scanme.nmap.org` (connectivity / DNS) · `nmap.org` (parent domain) — authorized by the Nmap Project for educational use

---

## Overview

Reconnaissance is the first phase of any security assessment. Before any vulnerability scan,
penetration test, or third-party risk review can begin, an analyst needs to know what a target
looks like from the outside — its IP, DNS records, registration details, public-facing
technology, and what the organization has already published about itself.

This lab is deliberately scoped to **passive reconnaissance only**. Even though the Nmap
Project explicitly permits active Nmap scanning against `scanme.nmap.org`, the exercise stays
on the phase that *precedes* scanning: no port scans, no brute force, no active probes.

## Scenario

An organization uses Nmap as a standard tool and runs periodic public-information reviews of
the Nmap Project as part of its third-party-risk programme. As the junior analyst, I was asked
to build a baseline: confirm my own workstation identity, verify reachability, gather public
information, run DNS and whois reconnaissance, practice OSINT techniques, and produce a written
report tying each finding to vulnerability management or third-party risk.

## Objectives

- Identify the workstation's network identity using `ip`
- Capture connectivity data against the target and save it with shell redirection
- Query domain registration with `whois` (registrar, name servers, key dates)
- Analyze DNS records with both `nslookup` (interactive) and `dig` (non-interactive), including queries against the **authoritative** name server
- Interpret DNS record types: A, MX, NS, CNAME, SOA
- Practice search-engine operators and an OSINT lookup tool
- Correlate all findings into a structured reconnaissance report

## Tasks Performed

| # | Task | Evidence |
|---|------|----------|
| 1 | Determine the Kali workstation's network identity (`ip`) | `screenshots/task01_ip.png` |
| 2 | Capture connectivity to the target (4 ICMP echo requests, redirected to file) | `target_info.txt`, `task02_ping.png` |
| 3 | Structured website observation of nmap.org + read the scanme authorization notice | `task03_homepage.png`, `task03_scanme_notice.png` |
| 4 | Domain registration lookup with `whois` on the parent domain | `target_whois.txt`, `task04_whois.png` |
| 5 | DNS recon with `nslookup` (interactive) against the default resolver | `task05_nslookup.png` |
| 6 | Query the **authoritative** name server for A/MX/NS/CNAME/SOA | `task06_nslookup_auth.png` |
| 7 | Repeat DNS queries with `dig`, capturing all results to one file | `target_dns.txt`, `task07_dig.png` |
| 8 | Safe search-engine recon (`site:`, `filetype:`, `intitle:`, phrases, `-`) against demo targets | `task08_search1.png`, `task08_search2.png` |
| 9 | Passive fingerprinting with an approved OSINT lookup tool | `task09_osint.png` |
| 10 | Public-data awareness review on a fictional dataset | in report |
| 11 | Organize evidence into a reviewable folder structure | `task11_evidence.png` |
| 12 | Write the correlated reconnaissance report | `recon_report` |

## Tools

`ip` · `ping` · `whois` · `nslookup` · `dig` · Firefox · search-engine operators · OSINT lookup tool

## Skills Demonstrated

DNS record analysis · whois interpretation · authoritative vs. recursive DNS · OSINT
fundamentals · search-operator technique · scope discipline · evidence-based documentation ·
linking findings to vulnerability management and third-party risk.

## Deliverables

`target_info.txt` · `target_whois.txt` · `target_dns.txt` · `recon_report` · 12 named screenshots

## Lessons Learned

<!-- Fill in 2-3 sentences: what surprised you, what took longer than expected, what you'd do differently. -->

---

> **Scope & authorization:** Passive reconnaissance only, against a target explicitly approved
> for educational use. The operator's permission to scan does *not* license scanning in this lab.
