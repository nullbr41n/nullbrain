---
description: Hashcat
---

# Hashcat

Hashcat is considered world's fastest and most advanced password recovery Utility.

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

