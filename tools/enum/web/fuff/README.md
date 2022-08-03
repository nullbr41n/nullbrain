# Usages

``` bash
ffuf -c -w /usr/share/seclists/Discovery/Web-Content/quickhits.txt -u http://${IP}/FUZZ -t 500
```

Flags:
 - -c : colorize the output
 - -w : wordlist from localmachine
 - -u : target's URL


 ## Nested fuzz

``` bash
 ffuf -c -w /usr/share/seclists/Discovery/Web-Content/quickhits.txt -u http://${IP}/{dir_fuzzed}/FUZZ -t 500 -mc 200
 ```

 Flags:
 - -t: the number of concurrent threads
 - -mc: only display results that match a "200" HTTP status code