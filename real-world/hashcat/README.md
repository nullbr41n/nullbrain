---
description: Hashcat
---

# Hashcat

Hashcat is considered world's fastest and most advanced password recovery Utility.

### Usage I:

`hashcat -r /usr/share/hashcat/rules/best64.rule --stdout hint > password.txt`

```text
Options explained:

-r, --rules-file | File | Multiple rules applied to each word from wordlists | -r rules/best64.rule
--stdout | Do not crack a hash, instead print candidates only |
```

`hashcat -m 3200 hash password.txt --show`

```text
Options explained:

-m 3200     : Hash type (bcrypt/bowlfish)
hash        : Contains hashed key
password.txt: Contains hints
--show      : Compare hashlist with potfile; show cracked hashes
```

### Usage II:

`hashcat -m 1400 password.hash /usr/share/wordlists/rockyou.txt --force`

### Usage III:

`hashcat -m 7900 -a 0 -o found.txt crack`[Usage II:](https://app.gitbook.com/@nullbrain/s/nullbrain/~/drafts/-MYaoe288ubj13s76ZDn/real-world/hashcat#usage-ii)`.hash /usr/share/wordlists/rockyou.txt --force`



```text
Options explained:

-m 7900     : Hash type (Drupal7)
-a (num)    : 
-o (output) : Output file (e.g found.txt)
hash        : Contains hashed key (crack.hash)
password.txt: Contains hints
--show      : Compare hashlist with potfile; show cracked hashes
```

### Error:

```text
* Device #1: Not a native Intel OpenCL runtime. Expect massive speed loss.
             You can use --force to override, but do not report related errors.
No devices found/left.
```

Solution: `hashcat -m 1400 password.hash /usr/share/wordlists/rockyou.txt --force`

