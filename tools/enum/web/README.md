## WFUZZ

### Fuzz Files
`export URL="http"//${IP}:8080/FUZZ"`
`wfuzz -c -z file,/opt/SecLists/Discovery/Web-Content/raft-large-files.txt --hc 404 "$URL"`


### Fuzz Directories
`export URL="http"//${IP}:8080/FUZZ/"`
`wfuzz -c -z file,/opt/SecLists/Discovery/Web-Content/raft-large-directories.txt --hc 404 "$URL"`


```
-c: color
-z: input method `file`,
/opt/seclist/xxxx: list
--hc: hush code
```
