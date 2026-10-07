# Firewall Implementation Lab - Change Record

Technician: Lan Anh Chung
Date: 02.10.26
Lab environment: Neue Fische bootcamp, lab cloud4 (nested VMs DC10 and PC10) 

## 1. Target hosts 
- Domain controller hostname / IP:IP: DC10 / 10.10.10.10
- Client workstation hostname / IP: PC10 / 10.10.10.20
- Domain: corp.local

## 2. Baseline state (before changes) 
- PC10 -> DC10 ping result: Success, 4/4 replies from 10.10.10.10, 0% loss
- DC10 -> PC10 ping result: Success, 4/4 replies from 10.10.10.20, 0% loss
- \\PC10\LABFILES reachable from DC10: yes

## 3. ICMP block on DC10
- Rules disabled (exact names): File and Printer Sharing (Echo Request - ICMPv4-ln),File and Printer Sharing (Echo Request - ICMPv6-ln) 
- Profiles affected: Domain, Private, Public
- Timestamp: 9:00
- Post-change ping result from PC10 -> DC10: Blocked, 4x "Request timed out", 0/4 replies, 100% loss

## 4. SMB block on PC10 
- Rules disabled (exact names): 
File and Printer Sharing (SMB-In) 
- File and Printer Sharing (NB-Session-In) 
- File and Printer Sharing (NB-Name-In) 
- File and Printer Sharing (NB-Datagram-In)
- Profiles affected: - 
- Timestamp: 9:12
- Post-change \\PC10\LABFILES browse result from DC10: Access failed with “Windows cannot access \PC10\LABFILES” 

## 5. Restoration 
- DC10 ICMP rules re-enabled: yes, all previously disabled instances
- PC10 SMB rules re-enabled: yes, all previously disabled instances
- Final ping test: Success, PC10 -> DC10 4/4 replies, 0% loss
- Final share-access test: \\PC10\LABFILES accessible from DC10 again

## 6. Key risks observed
Multiple rules can allow the same traffic. On a domain controller, the AD DS role adds its own Echo Request rules, so disabling only the File and Printer Sharing rules may leave ICMP open.
Firewall rule changes do not terminate existing connections. An already established SMB session stayed active after the block, which could give a false impression that access is denied (or, as here, that the block failed). 
Rule****ist as several instances per profile. Missing a single instance leaves the traffic open on that profile. -
Blocking ICMP reduces visibility for troubleshooting and monitoring tools that rely on ping.

## 7. Recommended next steps 
Enforce both baseline requirements centrally via Group Policy instead of local changes, so they apply consistently and cannot be reverted locally. -
 Audit all enabled inbound rules per protocol/port (e.g. ICMPv4, TCP 445, 137-139) rather than searching by rule name only. 
Document the change and restoration procedure as a standard operating procedure. 
Monitor firewall logs for blocked SMB/ICMP attempts to detect misconfigurations or scanning activity.

## 8. Lessons learned 
Always verify a firewall change with a before/after test. Without the post-change test, the additional allow rule and the persistent session would have gone unnoticed.
Disable rules instead of deleting them, so they can be restored quickly, as shown in the restoration phase. 
When testing a block, clo*****isting sessions first, otherwise the result is misleading.

## 9. Evidence list 
Firewall_lab_report.docx
- commands\task01_ping_pc10_to_dc10.txt 
- commands\task02_ping_dc10_to_pc10.txt 
- commands\task05_ping_after_block.txt 
- screenshots\task01_baseline_ping.png 
- screenshots\task02_baseline_ping_reverse.png screenshots\task03_icmp_rules_located.png 
- screenshots\task04_icmp_rules_disabled.png 
- screenshots\task05_ping_blocked.png 
- screenshots\task06_share_created.png 
- screenshots\task07_share_accessible.png 
- screenshots\task08_smb_rules_disabled.png 
- screenshots\task09_share_blocked.png 
- screenshots\task10_restored_ping.png 
- screenshots\task10_restored_share.png
