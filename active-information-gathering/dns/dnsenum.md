# DNSenum

`dnsenum nullbrain.com`

```text
dnsenum VERSION:1.2.6

-----   nullbrain.com   -----


Host's addresses:
__________________

nullbrain.com.                         2250     IN    A        192.128.11.85


Wildcard detection using: xdvchwpfypxe
_______________________________________

xdvchwpfypxe.nullbrain.com.            2250     IN    A        192.128.11.85


!!!!!!!!!!!!!!!!!!!!!!!!!!!!

 Wildcards detected, all subdomains will point to the same IP address
 Omitting results containing 192.128.11.85.
 Maybe you are using OpenDNS servers.

!!!!!!!!!!!!!!!!!!!!!!!!!!!!


Name Servers:
______________

dns2.registrar-servers.com.              1020     IN    A        156.154.133.200
dns1.registrar-servers.com.              634      IN    A        156.154.132.200


Mail (MX) Servers:
___________________

mail.nullbrain.com.                    2250     IN    A        192.128.11.113


Trying Zone Transfers and getting Bind Versions:
_________________________________________________


Trying Zone Transfer for nullbrain.com on dns2.registrar-servers.com ...
AXFR record query failed: REFUSED

Trying Zone Transfer for nullbrain.com on dns1.registrar-servers.com ...
AXFR record query failed: REFUSED


Brute forcing with /usr/share/dnsenum/dns.txt:
_______________________________________________



nullbrain.com class C netranges:
___________________________________

 173.45.127.0/24
 192.128.11.0/24


Performing reverse lookup on 512 ip addresses:
_______________________________________________

unresolvable name: dns2.registrar-servers.com at /usr/bin/dnsenum line 660.
unresolvable name: dns1.registrar-servers.com at /usr/bin/dnsenum line 660.
unresolvable name: dns2.registrar-servers.com at /usr/bin/dnsenum line 660.
unresolvable name: dns1.registrar-servers.com at /usr/bin/dnsenum line 660.

0 results out of 512 IP addresses.


nullbrain.com ip blocks:
___________________________


done.
```

