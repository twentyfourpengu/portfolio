Reconnaissance Report
Analyst: Lan Anh Chung
Date: 29.09.26
Assigned target: scanme.nmap.org (parent domain nmap.org )

1. Target information
Target hostname: scanme.nmap.org
Parent domain: nmap.org
Target IP address (from ping/dig): 45.33.32.156
Authoritative DNS servers: linode.com
Operator authorization notice (summarized):

3. Kali network identity
Kali IP address: 192.168.1.178
Interface: eth0
Subnet: /24

4. Connectivity results
Target reached (Y/N):Y
Packets transmitted:4
Packets received:4
Packet loss (%): 0
Average round-trip time: 18.979/19.102/19.168/00.72

5. Website findings
Project / site display name: Nmap the Network Mapper
Page types observed on nmap.org : homepage, download page, documentation_ reference guide, changelog/installation guide
Visible technologies: seclists.org
Authorization notice summary (from scanme.nmap.org ):The operator (Fyodor) explicitly allows users to scan this machine to learn how to use Nmap or to test their Nmap installation. However, users are strictly requested not to overload the system (limit to a few scans per day), not to run automated exploit tools or SSH brute-force attacks against it, and not to waste bandwidth.
Other public-facing information: nmap has been developed for over 20 years by gorden lyon

6. Whois findings (for nmap.org )
Registrar: Gandi SAS
Name servers: ns1.linode.com,ns2.linode.com,ns3.linode.com,ns4.linode.com,ns5.linode.com
Creation date: 1999-01-18
Updated date: 2026-04-10
Expiration date: 2029-01-18
Other relevant fields: clientTransferProhibited
7. DNS findings
Default resolver (from nslookup):192.168.1.1
A record: 45.33.32.156
MX record(s): nmap.org has five MX records, all pointing to Google Workspace mail servers (queried directly from the authoritative server ns1.linode.com):
  - Priority 1: aspmx.l.google.com
  - Priority 5: alt1.aspmx.l.google.com
  - Priority 5: alt2.aspmx.l.google.com
  - Priority 10: aspmx2.googlemail.com
  - Priority 10: aspmx3.googlemail.com
NS record(s): nmap.org is served by five authoritative name servers, all operated by Linode:
  - ns1.linode.com
  - ns2.linode.com
  - ns3.linode.com
  - ns4.linode.com
  - ns5.linode.com
CNAME record (or "none returned"):none
SOA record:Primary NS: ns1.linode.com; responsible mailbox: hostmaster.nmap.com (i.e. hostmaster@nmap.com); serial number: 2021000018. Refresh 14400 s, retry 14400,expire 1209600 s (14 days), minimum TTL 3600 s. Record TTL: 3600 
Notes on differences between nslookup and dig results:

7. Search reconnaissance findings
Query 1:`site:example.com` / `site:` / web page (HTML) / ex. "Only the 'Example Domain' homepage was indexed" oder "No results"
Query 2:`site:example.org filetype:pdf` / `site:` + `filetype:` / PDF or "no results"/ ex. "No PDFs indexed"
Query 3:`site:example.com intitle:"Example Domain"` / `site:` + `intitle:` + quoted phrase / web page / ex. "Homepage matched by title"
Query 4:`site:example.com -inurl:www` / `site:` + minus operator / web page oder "no results"

8. OSINT lookup findings (for nmap.org )
Hosting provider:Linode LLC
Server technology: Apache HTTP server
First-seen date: 11. Januar 1998
Related hostnames: scanme.nmap.org, insecure.org, seclists.org, sectools.org, ncap.com
Other technologies: OpenSSL, Mailman,SVN/Git

9. Public data awareness observations
Categories of public information identified: 
Why each category matters: 
  - Email addresses: enable phishing/spear-phishing, and address patterns allow guessing further addresses.
  - Job titles: enable pretexting and CEO fraud by showing who holds finance, IT or HR roles.
  - Phone numbers: enable vishing and pretexting calls.
  - Social media profiles: personal details help craft convincing lures and guess passwords or security answers.

Suggested ways to reduce exposure:
  - Email addresses: publish role-based addresses, use SPF/DKIM/DMARC, provide awareness training.
  - Job titles: publish minimal org charts, require call-back and four-eyes verification for sensitive requests.
  - Phone numbers: publish central numbers instead of direct lines, train staff on suspicious calls.
  - Social media: apply a social media policy, tighten privacy settings, avoid security questions with public answers, enforce MFA.
    
10. Key risks
Risk1: Email is handled by Google Workspace. If SPF, DKIM or DMARC are weak, the domain could be spoofed in phishing against organizations that trust Nmap Project communications.
Risk 2: DNS is hosted by Linode and the target host runs at Linode. The project depends on one third-party provider, so an outage or compromise there affects availability and integrity of the domain.
Risk 3: Public information (registration data, DNS records, website details, OSINT fingerprints) gives an attacker a map of the infrastructure.

11. Recommended next steps
Verify the Nmap Project's published release-signing process before approving the Nmap binary for internal distribution
Add Linode and Google Workspace to the third-party register and confirm their compliance attestations are current,
If Nmap is used inside internal scans, document the segmentation/authorization controls that govern its use.

12. Evidence list
target_info.txt
target_whois.txt
target_dns.txt
screenshots/ task01_ip.png
task02_ping.png
task03_homepage.png
task03_scanme_notice.png
task04_whois.png
task05_nslookup.png
task06_nslookup_auth.png
task07_dig.png
task08_search1.png
task08_search2.png
task09_osint.png
task11_evidence.png
recon_report.docx
