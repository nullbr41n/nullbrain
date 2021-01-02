# NFS

## NFS

* Portmapper
  * Port: 111
* RPCBind
  * Port: 111

`nmap -v -p 111 10.11.1.1-254`

`nmap -sV -p 111 --script=rpcinfo 18.11.1.1-254`

### NFS NSE Scripts

`nmap -p 111 --script nfs* 10.11.1.12`

