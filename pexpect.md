
### Pexpect 
* is a Pure Python Expect-like module
* is a Python module for spawning child applications and controlling them automatically. 
* is used for automating interactive applications such as ssh, ftp, passwd, telnet, etc.

---

### install via pip
```shell
$ pip install pexpect
```

* pexpect.spawn() and pexpect.run() are only available on POSIX
* Because they rely on Unix pseudoterminals (ptys). 
* Use Cygwin on Windows.

Note:
This will only display in the notes window.

---
### API Overview

* spawn class
```python
class pexpect.spawn(command, args=[], 
        timeout=30, maxread=2000, 
        searchwindowsize=None, logfile=None, 
        cwd=None, env=None, ignore_sighup=False, 
        echo=True, preexec_fn=None, 
        encoding=None, codec_errors='strict', 
        dimensions=None, use_poll=False)
```
```python
expect(pattern, timeout=-1, searchwindowsize=-1, async_=False, **kw)
```

---
### API Overview

* run function
```python
pexpect.run(command, timeout=30, 
        withexitstatus=False, events=None, 
        extra_args=None, logfile=None, 
        cwd=None, env=None, **kwargs)
```


---
### API Overview
```python
#! /usr/bin/python3

import pexpect as pe
import sys
import time

def main():
    child = pe.spawn("ssh nj", timeout=30, encoding='utf-8')
    child.logfile_read = sys.stdout
    prompt = "root@NewJersey.*#"
    result = child.expect([prompt, pe.EOF, pe.TIMEOUT], 10)
    if result == 0:
        time.sleep(3)
        child.sendline("uname")
        p0 = child.expect([prompt, pe.EOF, pe.TIMEOUT], 3)

        if p0 == 0:
            print("Login successful ...")

            time.sleep(3)
            child.sendline("pwd")
            p1 = child.expect([prompt, pe.EOF, pe.TIMEOUT], 3)

            time.sleep(3)
            child.sendline("ls")
            p2 = child.expect([prompt, pe.EOF, pe.TIMEOUT], 3)
        else:
            print("Login failed" + str(p0))
    else:
        print("ssh connect failed[{0}]".format(result))

    child.close()
    print("Bye bye")

if __name__ == "__main__":
    main()

```
Note:
Beware of + and * at the end of patterns will always get a minimal match (non greedy). 

---
### API Overview
```bash
root@aliyunHost:~/workspace/test# ./pe_ssh.py
Welcome to Ubuntu 16.04.6 LTS (GNU/Linux 4.15.0-29-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

9 packages can be updated.
0 updates are security updates.

New release '18.04.2 LTS' available.
Run 'do-release-upgrade' to upgrade to it.


Last login: Tue Jul  2 13:34:02 2019 from 106.15.185.130
root@NewJersey:~# uname
Linux
root@NewJersey:~# Login successful ...
pwd
/root
root@NewJersey:~# ls
ca  shadowsocks-liber.config.json  streisand_ss.cap  todo.md  workspace
root@NewJersey:~# Bye bye
root@aliyunHost:~/workspace/test#

```

---
### API Overview
![ssh to nj](./images/pexpect_ssh_nj.svg)



---
* child.before: all data before the match
* child.after: the data that was matched
* child.match: the re.MatchObject used in the re match
* timeout is the time allowed for the spawning.
* maxread is the size of the buffer, the default is 2000.

Note:
If the spawned process is called child,
then to look for the end of the line:
child.expect(’\r\n’)
Why so? Each line in TTY devices ends with a CR/LF combination.

---
Reference:
* [Pexpect Documentation](https://pexpect.readthedocs.io/en/stable/index.html)
* [Python Regular expression operations](https://docs.python.org/3/library/re.html)
* [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
* [pip documentation](https://pip.pypa.io/en/stable/user_guide/)