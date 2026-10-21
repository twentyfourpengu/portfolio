# Reconnaissance Report

- **Analyst:** Lan Anh Chung
- **Date:** 2026-09-29
- **Assigned target:** `scanme.nmap.org` (parent domain `nmap.org`)

---

## 1. Target information

- **Target hostname:** `scanme.nmap.org`
- **Parent domain:** `nmap.org`
- **Target IP address (from ping/dig):** `45.33.32.156`
- **Authoritative DNS servers:** `ns1.linode.com` – `ns5.linode.com`

## 2. Kali network identity

- **Kali IP address:** `192.168.1.178`
- **Interface:** `eth0`
- **Subnet:** `/24`

## 3. Connectivity results

- **Target reached:** Yes
- **Packets transmitted:** 4
- **Packets received:** 4
- **Packet loss:** 0 %
- **Round-trip time (min / avg / max):** 18.979 / 19.102 / 19.168 ms

## 4. Website findings

- **Project / site display name:** Nmap – the Network Mapper
- **Page types observed on `nmap.org`:** homepage, download page, documentation / reference guide, changelog / installation guide
- **Visible technologies:** `seclists.org`
- **Other public-facing information:** Nmap has been developed for over 20 years by Gordon Lyon.

**Authorization notice summary (from `scanme.nmap.org`):**

> The operator (Fyodor) explicitly allows users to scan this machine to learn how to use Nmap or to test their Nmap installation. However, users are strictly requested not to overload the system (limit to a few scans per day), not to run automated exploit tools or SSH brute-force attacks against it, and not to waste bandwidth.

## 5. Whois findings (for `nmap.org`)

- **Registrar:** Gandi SAS
- **Name servers:** `ns1.linode.com`, `ns2.linode.com`, `ns3.linode.com`, `ns4.linode.com`, `ns5.linode.com`
- **Creation date:** 1999-01-18
- **Updated date:** 2026-04-10
- **Expiration date:** 2029-01-18
- **Other relevant fields:** `clientTransferProhibited`

## 6. DNS findings

- **Default resolver (from nslookup):** `192.168.1.1`
- **A record:** `45.33.32.156`
- **CNAME record:** none returned

### MX records

All five MX records point to Google Workspace mail servers (queried directly from the authoritative server `ns1.linode.com`):

- **Priority 1:** `aspmx.l.google.com`
- **Priority 5:** `alt1.aspmx.l.google.com`
- **Priority 5:** `alt2.aspmx.l.google.com`
- **Priority 10:** `aspmx2.googlemail.com`
- **Priority 10:** `aspmx3.googlemail.com`

### NS records

`nmap.org` is served by five authoritative name servers, all operated by Linode:

- `ns1.linode.com`
- `ns2.linode.com`
- `ns3.linode.com`
- `ns4.linode.com`
- `ns5.linode.com`

### SOA record

- **Primary NS:** `ns1.linode.com`
- **Responsible mailbox:** `hostmaster.nmap.com` (= hostmaster@nmap.com)
- **Serial number:** `2021000018`
- **Refresh:** 14400 s
- **Retry:** 14400 s
- **Expire:** 1209600 s (14 days)
- **Minimum TTL:** 3600 s
- **Record TTL:** 3600 s

### Differences between nslookup and dig

- **Source of the answer:** nslookup queried the default resolver (`192.168.1.1`) and returned a *Non-authoritative answer*, i.e. a cached response passed on by the local router/ISP resolver. Querying `ns1.linode.com` directly returned the authoritative answer from the zone itself.
- **Level of detail:** nslookup only shows the requested records in a short format. dig shows the full DNS response, split into QUESTION, ANSWER, AUTHORITY and ADDITIONAL sections, plus header flags, query time, responding server and message size.
- **Authority indicator:** dig displays the `aa` (authoritative answer) flag when the response comes from an authoritative server, which makes it easy to verify where the data originated. nslookup only indicates this with the *Non-authoritative answer* note.
- **TTL values:** dig shows the TTL for every record. When querying a caching resolver, the TTL counts down from the original value (here 3600 s); from the authoritative server it shows the full configured TTL.
- **Record content:** the records themselves (A, MX, NS, SOA) were consistent across both tools, so no discrepancies or stale cache entries were observed.
- **Conclusion:** nslookup is useful for quick lookups, while dig is better suited for reconnaissance because it shows where an answer came from and the full context of the response.

## 7. Search reconnaissance findings

**Query 1**  – operator: site:  

Query: site: example.com (entered with a space after the colon)  
Result: Google returned an AI Overview describing example.com as an IANA-reserved domain for examples and documentation, followed by the Example Domain homepage (https://example.com) and a Wikipedia article about the domain.  
Observation: Because of the space after the colon, Google did not apply site: as an operator and treated the input as normal search terms. This is confirmed by the Wikipedia result, which is not hosted on example.com. The correct syntax is site:example.com without a space.  

**Query 2** – operators: site: + filetype: + intitle:  

Query: site:example.com filetype:pdf intitle:report  
Result: No results – the search did not match any documents.  
Observation: No PDF files with "report" in the title are indexed for example.com. This is expected, as the domain only hosts a single placeholder page.  


## 8. OSINT lookup findings (for `nmap.org`)

- **Hosting provider:** Linode LLC
- **Server technology:** Apache HTTP Server
- **First-seen date:** 1998-01-11
- **Related hostnames:** `scanme.nmap.org`, `insecure.org`, `seclists.org`, `sectools.org`, `ncap.com`
- **Other technologies:** OpenSSL, Mailman, SVN/Git

## 9. Public data awareness observations

**Categories of public information identified:** TODO

### Why each category matters

- **Email addresses:** enable phishing / spear-phishing; address patterns allow guessing further addresses.
- **Job titles:** enable pretexting and CEO fraud by showing who holds finance, IT or HR roles.
- **Phone numbers:** enable vishing and pretexting calls.
- **Social media profiles:** personal details help craft convincing lures and guess passwords or security answers.

### Suggested ways to reduce exposure

- **Email addresses:** publish role-based addresses, use SPF/DKIM/DMARC, provide awareness training.
- **Job titles:** publish minimal org charts, require call-back and four-eyes verification for sensitive requests.
- **Phone numbers:** publish central numbers instead of direct lines, train staff on suspicious calls.
- **Social media:** apply a social media policy, tighten privacy settings, avoid security questions with public answers, enforce MFA.

## 10. Key risks

1. **Email spoofing:** Email is handled by Google Workspace. If SPF, DKIM or DMARC are weak, the domain could be spoofed in phishing against organizations that trust Nmap Project communications.
2. **Single-provider dependency:** DNS is hosted by Linode and the target host runs at Linode. The project depends on one third-party provider, so an outage or compromise there affects availability and integrity of the domain.
3. **Infrastructure mapping:** Public information (registration data, DNS records, website details, OSINT fingerprints) gives an attacker a map of the infrastructure.

## 11. Recommended next steps

1. Verify the Nmap Project's published release-signing process before approving the Nmap binary for internal distribution.
2. Add Linode and Google Workspace to the third-party register and confirm their compliance attestations are current.
3. If Nmap is used inside internal scans, document the segmentation/authorization controls that govern its use.

## 12. Evidence list

```
.
├── report.md
├── target_info.txt
├── target_whois.txt
├── target_dns.txt
└── screenshots/
    ├── task01_ip.png
    ├── task02_ping.png
    ├── task03_homepage.png
    ├── task03_scanme_notice.png
    ├── task04_whois.png
    ├── task05_nslookup.png
    ├── task06_nslookup_auth.png
    ├── task07_dig.png
    ├── task08_search1.png
    ├── task08_search2.png
    ├── task09_osint.png
    └── task11_evidence.png
```
