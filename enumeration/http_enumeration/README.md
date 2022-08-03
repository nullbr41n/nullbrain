This could be post enumeration, if HTTP ports are open.

There are various tools/techniques to run http enumerations.


## Tools

- [wfuzz](../../tools/enum/web/wfuzz/README.md)
- gobuster
- [dirb](../../tools/enum/web/dirb/README.md)
- nikto
- [fuff](../../tools/enum/web/fuff/README.md)


## Techniques
 
1. Vulnerability/Exploit search
   1. [PHP](../../exploitation/PHP/README.md)
1. Sql injection?
1. Remote file inclusion
1. Local file inclusion
1. Google foo

# Information Gathering

* Programming Language
* Framework used
* Webserver
* Database used
* OS

Much of this information can be gathered from modern browsers which provide developer tools. Inspecting URL for an extension, viewing source code. Viewing source code can display versions used and any common library.

**Server & OS information** can be found from Headers \(if the default configuration is left in the webserver.\)

Other information such as if an application uses CDN or caching it may show x-powered-by, x-varnish, x-amz-cf-id etc.

In a similar way, a **sitemap** can be handy to figure out any sensitive Disallow, or at least structure of the website.

