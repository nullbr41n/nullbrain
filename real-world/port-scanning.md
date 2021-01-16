# Port Scanning

```text
TARGET_MACHINE='<ip_address>'
ports=$(nmap -p- --min-rate=1000 -T4 ${TARGET_MACHINE} | grep '^[0-9]' | cut -d '/' -f 1 | tr '\n' ',' | sed s/,$//)
nmap -sC -sV -p$ports ${TARGET_MACHINE}
```

