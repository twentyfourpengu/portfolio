## Incident Detection Report
## 1. Analyst information
Name: Lan Anh Chung
Date: 01.10.26
Cohort: 270726

## 2. Target information
Target host: DC-Server22
Target IP: 10.10.10.10.
Wazuh agent ID for DC10:  

## 3. Workstation identity
Kali hostname: kali
Kali IP: 10.10.10.128 
Reachability to DC10 confirmed at: 15:04

## 4. Password list 
Source dictionary: /ir_detection_lab
Total lines: 25
Line number of `Pa$$w0rd`: 1

## 5. Hydra brute-force attack (Task 4) 
Command issued: hydra -l Administrator -P passlist.txt smb2://10.10.10.10 | tee task04_hydra_output.txt
Attempts before success: 1
Time to first valid result: ~1
Recovered credentials: Administrator / Pa$$w0rd

## 6. Wazuh alerts — brute-force phase (Task 5) - 
Rule 60122 — count, level, description: 30, 5, Logon Failure
Rule 92652 — level, description, MITRE tactic, MITRE technique: 6, Successful Remote Logon Detected, Defense Evasion, Pass the Hash

## 7. MITRE mapping analyst note (Task 6) 
One paragraph: does Wazuh's default technique mapping for Rule 92652 accurately describe what hydra did over RDP? Why or why not

## 8. Share-mount attempts (Tasks 7 and 8) 
Invalid attempt — command: sudo mount -t cifs "//10.10.10.10/C"/mnt/dc10-o'username=Jaime,password=Pa$$w0rd', error: mount error(13): Permission denied, Time: 11:38
Valid attempt — command: sudo mount -t cifs "//10.10.10.10/C"/mnt/dc10-o'username=Administrator,password=Pa$$w0rd', observed folders: Program Files, Recovery, Users, Windows, ProgramData, Program Files (x86), System Volume Information, Time:11:39

## 10. Log clearing and Wazuh detection (Tasks 10 and 11)
Local time of log clear on DC10: 11:48 PM 
Wazuh Rule ID detected: 11:58
Rule level and MITRE technique: 5, Defense Evasion

## 11. Detection timeline 
| Time | Source | Action | Wazuh Rule ID | 
|---|---|---|---|
| 10:53 | Kali | hydra RDP attack start | — | 
| 11:10 | Wazuh | first 60122 alert | 60122 |
| 11:10 | Wazuh | 92652 success alert | 92652 |
| 11:28 | Kali | failed share mount (Jaime) | — | 
| 11:30 | Wazuh | 60122 alert (mount failure) | 60122 |
| 11:31 | Kali | successful share mount (Administrator) | — |
| 11:45 | Wazuh | 60106 alert (mount success) | 60106 |
| 11:48 | DC10 | Security log cleared | — | 
| 11:58 | Wazuh | log-clear alert | 63103 | 

## 12. Key risks identified
_Risk 1_The DC10 Administrator account was brute-forced with a weak dictionary password, and no account-lockout policy stopped the repeated attempts.
_Risk 2_ The DC10 Administrator account was brute-forced with a weak dictionary password, and no account-lockout policy stopped the repeated attempts.
_Risk 3_ The Windows Security log on DC10 could be cleared (Event 1102, MITRE T1070), letting an attacker erase local evidence of their activity.

## 13. Recommended next steps
_Recommendation 1_ Enforce strong passwords, an account-lockout policy, and MFA on all privileged accounts.
_Recommendation 2_Reduce the attack surface: disable unneeded services and restrict RDP/WinRM/SMB admin access to defined management hosts.
_Recommendation 3_ Turn the confirmed Wazuh rules (60122, 92652, T1070 log-clearing) into active real-time SOC alerts, including a "many failures → success" correlation rule.

## 14. Why centralized logging matters
Centralized logging means the evidence outlives the endpoint. even after DC10's local log was cleared, Wazuh still held the full record, because the events were forwarded before deletion and are beyond the attacker's reach. 

## 15. Evidence list 
task01_kali_identity.txt 
passlist.txt 
Task04_hydra_output.txt
Task07_mount_invalid.txt
Task08_mount_valid.txt
ir_detection_report.md
screenshots/task01_terminal.png
screenshots/task02_wordlist_grep.png
screenshots/task03_wazuh_dc10_filter.png
screenshots/task04_hydra_success.png 
screenshots/task05_rule_60122.png
screenshots/task05_rule_92652.png
screenshots/task06_mitre_technique.png
screenshots/task08_share_listing.png
screenshots/task09_rule_60122_mount.png
screenshots/task09_rule_60106_mount.png
screenshots/task10_dc10_log_cleared.png
screenshots/task11_wazuh_log_cleared.png
