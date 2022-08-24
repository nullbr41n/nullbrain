## Verification

Other than NMAP `OS` (`-O`) & version (-`sV`) detection simple ping `ttl` can also indicate if that is windows box. Windows sets `ttl` to `128` and decrements by `1` every-time packet traverse router, whereas, linux devices sets at `64`, `128` + chances are networking devices.




```mermaid
  graph TD;
  A[NMAP] -->|Scan| B[Results]
  B --> C[PORTS]
  C -->|web/80/443| D[Web Enum]  
  C -->|dns/53| E[DNS Enum]
  C -->|smb/445| F[SMB Enum]
  C -->|ldap/389| G[ldap Enum]
  C -->|winrm/47001| H[winrm Enum]
  H --> I[winPeas]
  H --> J[bloodhound]
  J --> K[writeDACL]
  K --> L[secretsdump]
  L --> M[GoldenTicket]

click A "https://github.com/nullbr41n/nullbrain/blob/main/active-information-gathering/nmap.md" "NMAP" _blank

click E "https://github.com/nullbr41n/nullbrain/blob/main/active-information-gathering/dns/README.md" "DNS Enum" _blank

click F "https://github.com/nullbr41n/nullbrain/blob/main/active-information-gathering/enumeration/smb.md" "SMB Enum" _blank

click G "https://github.com/nullbr41n/nullbrain/blob/main/active-information-gathering/ldap.md" "ldap Enum" _blank

click H "https://github.com/nullbr41n/nullbrain/blob/main/active-directory/winrm.md" "WINRM" _blank

click I "https://github.com/nullbr41n/nullbrain/blob/main/active-directory/winrm.md#Winpeas" "winPeas" _blank

click J "https://github.com/nullbr41n/nullbrain/blob/main/active-directory/bloodhound.md" "bloodhound" _blank

click K "https://github.com/nullbr41n/nullbrain/blob/main/active-directory/writeDACL.md" "writeDACL" _blank

click L "https://github.com/nullbr41n/nullbrain/blob/main/active-directory/secretsdump.md" "secretsdump" _blank

click M "https://github.com/nullbr41n/nullbrain/blob/main/active-directory/golden_ticket_linux.md" "GoldenTicket" _blank

```