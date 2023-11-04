# SMB

## enum


| Description|Netbios|Netbios over TCP|
| ---------|-----------|-----------|
|KNOWN|netbios| smb|
|PORT |139| 445 |
|PROTOCOL|TCP/UDP| TCP |
|OSI|OSI: Session Layer |session layer/Presentation Layer|


```mermaid
graph TD;
	A(SCAN) -->B(nmap -v -p 139,445 -oG smb.txt 10.10.10.0/24 --script=smb-os-discovery) --> D(smbclient -L 10.10.10.10)
	A -->C(nbtscan -r 10.10.10.0/24) --> D
	A -->CI(enum4linux -S -U 10.10.10.10) --> D	
	D -->|Anonymous| E[exploitable]
	D -->|shares| E[exploitable]
	E -->|Yes| F[Foothold]
	E -->|No| G[End]
```

### Anonymous

`smbclient -U guest //10.10.10.10/<share>`



```enum4linux
-U        get userlist
-S        get sharelist
```
