# Incident Detection Report

## 1. Analyst information

- **Name:** Lan Anh Chung
- **Date:** 2026-10-01
- **Cohort:** 270726

## 2. Target information

- **Target host:** DC10 (hostname `DC-Server22`)
- **Target IP:** `10.10.10.10`
- **Wazuh agent ID for DC10:** TODO

## 3. Workstation identity

- **Kali hostname:** `kali`
- **Kali IP:** `10.10.10.128`
- **Reachability to DC10 confirmed at:** 15:04

## 4. Password list

- **Source dictionary:** `/ir_detection_lab/passlist.txt`
- **Total lines:** 25
- **Line number of `Pa$$w0rd`:** 1

## 5. Hydra brute-force attack (Task 4)

- **Command issued:** `hydra -l Administrator -P passlist.txt smb2://10.10.10.10 | tee task04_hydra_output.txt`
- **Attempts before success:** 1
- **Time to first valid result:** ~1 s
- **Recovered credentials:** `Administrator` / `Pa$$w0rd`

## 6. Wazuh alerts — brute-force phase (Task 5)

- **Rule 60122** — count 30, level 5, *Logon Failure*
- **Rule 92652** — level 6, *Successful Remote Logon Detected*, MITRE tactic: Defense Evasion, MITRE technique: Pass the Hash

## 7. MITRE mapping analyst note (Task 6)

> **Prompt:** Does Wazuh's default technique mapping for Rule 92652 accurately describe what hydra did? Why or why not?

TODO: write your paragraph here.

## 8. Share-mount attempts (Tasks 7 and 8)

**Invalid attempt**
- **Command:** `sudo mount -t cifs //10.10.10.10/C /mnt/dc10 -o username=Jaime,password=Pa$$w0rd`
- **Error:** `mount error(13): Permission denied`
- **Time:** 11:38

**Valid attempt**
- **Command:** `sudo mount -t cifs //10.10.10.10/C /mnt/dc10 -o username=Administrator,password=Pa$$w0rd`
- **Observed folders:** `Program Files`, `Program Files (x86)`, `ProgramData`, `Recovery`, `System Volume Information`, `Users`, `Windows`
- **Time:** 11:39

## 9. Log clearing and Wazuh detection (Tasks 10 and 11)

- **Local time of log clear on DC10:** 11:48
- **Wazuh Rule ID detected:** 63103
- **Rule level and MITRE technique:** level 5, Defense Evasion (T1070 – Indicator Removal)

## 10. Detection timeline

- **10:53** — *Kali* — hydra attack start
- **11:10** — *Wazuh* — first 60122 alert (Rule 60122)
- **11:10** — *Wazuh* — 92652 success alert (Rule 92652)
- **11:28** — *Kali* — failed share mount (Jaime)
- **11:30** — *Wazuh* — 60122 alert, mount failure (Rule 60122)
- **11:31** — *Kali* — successful share mount (Administrator)
- **11:45** — *Wazuh* — 60106 alert, mount success (Rule 60106)
- **11:48** — *DC10* — Security log cleared
- **11:58** — *Wazuh* — log-clear alert (Rule 63103)

## 11. Key risks identified

1. The DC10 Administrator account was brute-forced with a weak dictionary password, and no account-lockout policy stopped the repeated attempts.
2. SMB admin shares (e.g. `C$`) were reachable and mountable from an arbitrary host on the network, with no restriction to defined management systems.
3. The Windows Security log on DC10 could be cleared (Event 1102, MITRE T1070), letting an attacker erase local evidence of their activity.

## 12. Recommended next steps

- Enforce strong passwords, an account-lockout policy, and MFA on all privileged accounts.
- Reduce the attack surface: disable unneeded services and restrict RDP/WinRM/SMB admin access to defined management hosts.
- Turn the confirmed Wazuh rules (60122, 92652, T1070 log-clearing) into active real-time SOC alerts, including a "many failures → success" correlation rule.

## 13. Why centralized logging matters

Centralized logging means the evidence outlives the endpoint. Even after DC10's local log was cleared, Wazuh still held the full record, because the events were forwarded before deletion and are beyond the attacker's reach.

## 14. Evidence list

```
.
├── evidence/
│   ├── report.md
│   ├── task01_kali_identity.txt
│   ├── passlist.txt
│   ├── Task04_hydra_output.txt
│   ├── Task07_mount_invalid.txt
│   └── Task08_mount_valid.txt
└── screenshots/
    ├── task01_terminal.png
    ├── task02_wordlist_grep.png
    ├── task03_wazuh_dc10_filter.png
    ├── task04_hydra_success.png
    ├── task05_rule_60122.png
    ├── task05_rule_92652.png
    ├── task06_mitre_technique.png
    ├── task08_share_listing.png
    ├── task09_rule_60122_mount.png
    ├── task09_rule_60106_mount.png
    ├── task10_dc10_log_cleared.png
    └── task11_wazuh_log_cleared.png
```
