# Linux

## Filesystem Hierarchy

[Filesystem Hierarchy Standard](https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard)

```text
/ – The Root Directory

/bin – Essential User Binaries

These Binaries must be present when the system is mounted in single-user mode.

/sbin- system administration programs (fdisk, mkfs, sysctl, etc)

/etc - configuration flies /tmp- temporary files (typically deleted on boot)

/usr/bin - applications (apt, neat, nmap, etc.) /usr/share- application support and data files

Not essential for single-user mode.
```

## Package Management

Kali Linux usages advanced package tool \(apt\).

## Customizing the Bash Environment

The HISTIGNORE variable is particularly useful for filtering out basic commands that are run frequently, such as Is, exit, history, bg, etc:

`export HISTIGNORE="&:ls:[bf]g:exit:history"`

The HISTCONTROL variable defines whether or not to remove duplicate commands, commands that begin with spaces from the history, or both.

`export HISTCONTROL=ignoredups`

HISTTIMEFORMAT controls date and/or timestamps in the output of the history command.

`export HISTTIMEFORMAT='%F %T'`

