# Recon-ng

[Recon-ng](https://github.com/lanmaster53/recon-ng) is Metasploit like web reconnaissance framework.

Getting Started:

The Installation process is well described [here](https://github.com/lanmaster53/recon-ng/wiki/Getting-Started#installation). And in this example, we will use a docker image of Kali Linux.

## Running Kali Linux. \(with [Recon-ng files](https://github.com/lanmaster53/recon-ng.git) [mounted](https://docs.docker.com/storage/volumes/).\)

```text
 docker run -it -v ~/recon-ng:/recon-ng --net=host my_kali /bin/bash                                                             125 ↵ | at minikube ⎈ 
root@docker-desktop:/# ls -al /recon-ng/
total 80
drwxr-xr-x 14 root root   448 Jan  1 15:36 .
drwxr-xr-x  1 root root  4096 Jan  1 15:42 ..
drwxr-xr-x 12 root root   384 Jan  1 15:36 .git
-rw-r--r--  1 root root    37 Jan  1 15:36 .gitignore
-rw-r--r--  1 root root   294 Jan  1 15:36 Dockerfile
-rw-r--r--  1 root root 35141 Jan  1 15:36 LICENSE
-rw-r--r--  1 root root  1850 Jan  1 15:36 README.md
-rw-r--r--  1 root root   123 Jan  1 15:36 REQUIREMENTS
-rw-r--r--  1 root root   299 Jan  1 15:36 VERSION
-rw-r--r--  1 root root   710 Jan  1 15:36 docker-compose.yml
drwxr-xr-x  6 root root   192 Jan  1 15:36 recon
-rwxr-xr-x  1 root root  4122 Jan  1 15:36 recon-cli
-rwxr-xr-x  1 root root  2674 Jan  1 15:36 recon-ng
-rwxr-xr-x  1 root root   399 Jan  1 15:36 recon-web

root@docker-desktop:/# cd /recon-ng/
```

## Installing requirements \(using Sourecode\)

```text
root@docker-desktop:/recon-ng# pip install --upgrade -r REQUIREMENTS
bash: pip: command not found


root@docker-desktop:/recon-ng# apt-get update && apt-get install pip
........


root@docker-desktop:/recon-ng# pip install --upgrade -r REQUIREMENTS
```

## Installing \(APT\)

```text
apt-get update && apt-get install recon-ng
```

