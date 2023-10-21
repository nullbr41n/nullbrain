# Nmap

## TLDR; 

```text
TARGET_MACHINE='<ip_address>'
ports=$(nmap -p- --min-rate=1000 -T4 ${TARGET_MACHINE} | grep '^[0-9]' | cut -d '/' -f 1 | tr '\n' ',' | sed s/,$//)
nmap -sC -sV -p$ports ${TARGET_MACHINE}
```


NOTE:
- Running 2 nmap against same host can cause weird results.
- Drop probes could cause increase in delays and hint to not hammer box.
- If required to run reglardless of status use option `-Pn`
- If output required in file use option `-oN filename.txt`

### Nmap-nse

Example:

  `locate -r nse$ | grep -i <service|e.g nfs>`

  e.g: `nmap --script "nfs-*" $IP -oN enum/mountable_shares.log`
	
  `sudo mount -v -t nfs $IP:/var/nfsshare ./nfs-my-local-dir`

As in example of NFS, things to notice would be e.g: `no_root_squash`


## Scanning

### Stealth/SYN Scanning

`nmap -ss <ip_address>`

### TCP Scanning

`nmap -sT <ip_address>`

### UDP Scanning

`nmap -sU <ip_address>`

### TCP/UDP Scanning

`nmap -sS -sU <ip_address>`

### Network Scanning/Sweeping

`nmap -sn <First ip_address>-last octate of range`

### Common ports scanning/Sweeping

`nmap -sT -A --top-ports=20 <First ip_address>-<last octate of range> -oG top-port-scanning.txt`

## Nmap with Grep

`nmap -v -sn <ip_address> -oG net-scan.txt` `grep Up net-scan.txt | cut -d" " -f 2`

## OS fingerprint

`nmap -o <ip_address>`

## Banner Grabbing & Service Enumeration

`nmap -sV -sT -A <ip_address>`

## Scanning for the NetBIOS Service

nmap -v -p 139,445 -oG smb.txt 10.11.1.1-254

## Scripting Engine \(NSE\)

[NSE](https://github.com/demoninhead/nullbrain/tree/c0b04300469ec045e6e53341ed9577bcb660b803/nmap_scripting_engine/index.md)

### Nmap SMB NSE Scripts

```text
ls -1 /usr/share/nmap/scripts/smb*
/usr/share/nmap/scripts/smb-brute.nse
/usr/share/nmap/scripts/smb-double-pulsar-backdoor.nse
/usr/share/nmap/scripts/smb-enum-domains.nse
/usr/share/nmap/scripts/smb-enum-groups.nse
/usr/share/nmap/scripts/smb-enum-processes.nse
/usr/share/nmap/scripts/smb-enum-services.nse
/usr/share/nmap/scripts/smb-enum-sessions.nse
/usr/share/nmap/scripts/smb-enum-shares.nse
/usr/share/nmap/scripts/smb-enum-users.nse
```

NSE scripts are located in the /usr/share/nmap/scripts directory.

### Scripts

1. smb-os-discovery: attempts to connect to the SMB service on a target system and determine its operating system:
2. dns-zone-transfer:

### [Nmap Vulnerability Scanning](../vulnerability-scanning/nmap.md)



More Nmap Examples: https://twitter.com/nullbr41n/status/1530459789670621184
