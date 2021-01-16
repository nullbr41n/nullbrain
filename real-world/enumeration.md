# Enumeration

### Learn Target Machine IP

`TM='10.10.10.209'`

### Quick Scan

`ports=$(nmap -p- --min-rate=1000 -T4 $TM | grep '^[0-9]' | cut -d '/' -f 1 | tr '\n' ',' | sed s/,$//)`

### Detailed scan

`nmap -sC -sV -p$ports $TM`

### Options Explained:

| Options | Explanation |
| :--- | :--- |
| -p- | to scan ports from 1 through 65535. |
| --min-rate | Nmap will try to keep the sending rate at or above 1000 packets per second. |
| -T | paranoid/sneaky/polite/normal/aggressive/insane |
| -T4 | Prohibits the dynamic scan delay from exceeding 10 ms for TCP ports. |
|  | -T4 when scanning reasonably modern and reliable networks. |
| grep '^\[0-9\]' | Grep numbers |
| cut -d '/' -f1 | cut input by delimeter / & print only first field. |
| tr '\n' ',' | tr \(short for translate\) deletes newline characters from stdin input, and writes , to stdout. |
| sed s/,$// | remove ',' in the end of line. |
| -sC | equivalent to --script=default |

