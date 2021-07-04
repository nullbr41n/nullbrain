---
description: Recon Tools & Frameworks
---

# Recon

## Acquisitions: good to know what it acquired

### ASN Enumeration: \[bgp.he.net\]

#### **ASN**: A top level number given to org when network is big enough..and shows all ips org have.

* Tools:
  * ASNLookup
  * bgp.he.net
  * amass

#### Using amass:

`docker build -t amass` [`https://github.com/OWASP/Amass.git`](https://github.com/OWASP/Amass.git) `(docker run amass intel -asn ASN_NUM,1,2,3)`

Reverse WHOIS: whoxy.com \(lets you search\).

* Good for API
* Free Credits

**DOMLink**: recursively go through all whoxy output

**Ad/Analytics Relationships**: Builtwith.com

**Google-Fu** "&lt;some search string&gt;" inurl:&lt;domain&gt;

**Shodan**: Infrastructure spider. domain scanning. Free API.

### Finding Subdomains: linked and js discovery:

* Linked Discovery

  * gospider
  * hakrawler

* Subdomain Enumeration: 
  * subdomainizer
  * subscraper

#### Google FU:

 _exclusion example: site:&lt;rootdomain&gt; -www.&lt;rootdomain&gt;_

\(e.g: minus out subdomains; i.e pull out of some sub-domain\)

#### Subdomain Scraping: Amass amass -d &lt;domain&gt;

* Tools
  * subfinder: 
  * github-subdomains.py
  * shosubgo \(golang\)

Subdomain Bruting

#### Amass:

amass enum -brute -d &lt;domain&gt; -src

amas enum brute -d &lt;domain&gt; -rf resolvers.txt -w bruteforce.list

#### suffleDNS:

