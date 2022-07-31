## pty

- `python -c 'import pty; pty.spawn("/bin/bash")'`

This mean, interactive terminal spawned via python. 

PTY: A pty is a pseudotty, a device entry that acts like a terminal to the process reading and writing there, but is managed by something else.

Now then TTY: In UNIX, /dev/tty* is any device that acts like a "teletype", i.e: a terminal. (Called teletype because that's what we had for terminals in those benighted days.)
