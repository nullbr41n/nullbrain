* An attempt to build enum mindmap

### assumption
- `10.10.10.10` is victim
- `XXXX` or `XXXX,XXXX` : one or many ports


### MindMap
```mermaid
graph TD;

AE[ENUM] --> BE[sudo nmap -p- 10.10.10.10]
BE -- GatheredListOfPorts --> CE[sudo nmap -p XXXX,XXX -A 10.10.10.10]
CE --> DEI[dirb http://10.10.10.10:XXXX/ -r]
CE --> DEII[gobuster dir -u http://10.10.10.10/ -w <OPTIONS> -s '<OPTIONS>' -e]
CE --> DEIII[wfuzz -c -z file,<WORDLIST> --hc 404 'http://10.10.10.10']
DEI --> EE[curl http://10.10.10.10:XXXX/<MEATS>]
DEI --> DEIQ[requires_to_be_bot?] --> EF[curl -A 'GoogleBot' http://10.10.10.10/robots.txt]

DEII --> EE[curl http://10.10.10.10:XXXX/<MEATS>]
DEII --> DEIQ[requires_to_be_bot?]
DEIII --> DEIQ[requires_to_be_bot?]

```


#### Gobuster

- Flag & options

```mermaid
graph TD;
GA[Gobuster] -- Flag: extensions --> GBX[-x php,txt,html]
GA[Gobuster] --> GFW[Flag: wordlist] --> GBWI[-w /usr/share/dirb/wordlists/common.txt]
GFW[Flag: wordlist] --> GBWII[-w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt]
GA[Gobuster] -- Flag: statuscode --> GBS[-s '200,204,301,302,307,403,500']
```


#### WFuzz

- Flag & options

```mermaid
graph TD;
WFA[Wfuzz] -- Flag: file --> WFB[file,/usr/share/seclists/Discovery/Web-Content/raft-large-files.txt]
```
