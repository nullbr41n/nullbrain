OS: <e.g Ubuntu>
Web-Technology: <e.g PHP>

IP: <e.g 192.168.1.10>

# Suspected user during enum 
USERS:
<john (Confirmed)>
<robert (suspected)>

CREDENTIALS (ANY):
<john - MyNameIsJohn>
<robert - >

Mysql:
ROOT UNAUTHORIZED ACCESS:
=========================================================================
Community Attack Vectors (To-Try List):
<e.g 22 SSH → >
<e.g 80 HTTP → Fuzzing Directories/Files → View the source luke (manual analysis in the browser) → Nikto  >
<e.g * SQLi  >
<e.g Warning: mysql_num_rows(): supplied argument is not a valid MySQL result resource in /var/www/checklogin.php on line 28 >


<e.g 139,445 CIFS/netbios_ssn →  lightweight conncetion to SMB. >


=========================================================================
NMAP RESULTS:
<PASTE NMAP RESULT>


=========================================================================
Web Services Enumeration:

[ + NIKTO ]

[ + WFUZZ ]

FILES: / (Web Root)
                                            


DIRECTORIES: / (Web Root)
                                                             

=========================================================================
OTHER:


=========================================================================
PRIV-ESC:
uname
release


 ~$ find / -perm -u=s -type f 2>/dev/null

~$ find / -perm -g=s -type f 2>/dev/null
 
=========================================================================
Proof:

User: (local.txt)


Root: (proof.txt)

`date`

`ifconfig`

=========================================================================


Take Away Concepts:
