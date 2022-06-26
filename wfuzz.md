`export URL="http"//${IP}:<WEBPORT>/FUZZ"`



`wfuzz -c -z file,/opt/SecLists/Discovery/Web-Content/raft-large-files.txt --hc 404 "$URL"`

```
-c: color
-z: input method `file`,
--hc: hush code; supress 404s
/opt/SecLists/Discovery/Web-Content/raft-large-files.txt: list

