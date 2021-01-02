# Recon-ng \[Usage\]

Recon-ng is module based, similar to Metasploit \(if you have some experience using the Metasploit framework\).

| Command | Purpose | Example |
| :--- | :--- | :--- |
| marketplace search &lt;string&gt; | Module search | `marketplace search github` |
| marketplace info &lt;string&gt; | Learn more about module | `marketplace info recon/repositories-vulnerabilities/github_dorks` |
| marketplace install &lt;string&gt; | Installing module using marketplace | `marketplace install recon/repositories-vulnerabilities/github_dorks` |
| modules load &lt;string&gt; | Load installed module | `modules load recon/domains-hosts/google_site_web` |

| Subcommands | Purpose |
| :--- | :--- |
| info | Display detail of the loaded module. |
| options set SOURCE &lt;string&gt; | Set our target domain. |
| run | Run the module. |
| back | Return to the main recon-ng prompt |
| show | Show stored data |

