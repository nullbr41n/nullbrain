# SMB

## SMB Enumeration

### Scanning NetBIOS Service

* NetBIOS
  * Port:     139
  * Protocol: TCP/UDP
  * OSI:      Session layer
* SMB \(Netbios over TCP\)
  * Port:       445
  * protocol:   TCP
  * OSI:        session layer/Presentation Layer

`nmap -v -p 139,445 -oG smb.txt 10.11.1.1-254`

Other than nmap, you can also explore nbtscan to get NetBIOS information.

### nbtscan

`nbtscan -r 10.11.1.0/24`

[Nmap](https://aashisn.github.io/nullbrain/topics/nmap/#banner-grabbing-amp-service-enumeration)



`for i in $(cat boxes.log); do nmap -v -p 139,445 --script=smb-os-discovery $i; echo '*************'; echo "$i"; echo "****************" || true; done`

```
enum4linux -S -U 192.168.1.13

-U        get userlist
-S        get sharelist
```
