# DirtyCow

https://www.exploit-db.com/raw/40839

## Compile
`gcc -pthread dirty.c -o dirty -lcrypt`


ERROR: `gcc: error trying to exec 'cc1': execvp: No such file or directory`

Update PATH to make gcc understand where cc1 is:

`PATH=PATH$:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/lib/gcc/x86_64-linux-gnu/4.8/;export PATH`
