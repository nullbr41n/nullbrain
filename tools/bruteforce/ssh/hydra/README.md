# HYDRA

Hydra is great tool to bruteforce if we have some password list and even better if we can make it less complicated with potential users/password that is already found during enumeration.
.
 
## Command
`hydra -l <user> -P <password.list> <IP> ssh`


```
-P /usr/share/wordlists/metasploit/unix_passwords.txt
```

e.g: In above example hydra with known user/pass as combination
