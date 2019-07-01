
## Pexpect 

* is a Pure Python Expect-like module
* is a Python module for spawning child applications and controlling them automatically. 
* is used for automating interactive applications such as ssh, ftp, passwd, telnet, etc.

---

## install Pexpect using pip

```shell
$ pip install pexpect
```

* pexpect.spawn() and pexpect.run() are only available on POSIX
* Because they rely on Unix pseudoterminals (ptys). 
* Use Cygwin on Windows.

Note:
This will only display in the notes window.

---
## API Overview

* spawn class
```python
class pexpect.spawn(command, args=[], 
        timeout=30, maxread=2000, 
        searchwindowsize=None, logfile=None, 
        cwd=None, env=None, ignore_sighup=False, 
        echo=True, preexec_fn=None, 
        encoding=None, codec_errors='strict', 
        dimensions=None, use_poll=False)

expect(pattern, timeout=-1, searchwindowsize=-1, async_=False, **kw)

```

---
## API Overview

* run function
```python
pexpect.run(command, timeout=30, 
        withexitstatus=False, events=None, 
        extra_args=None, logfile=None, 
        cwd=None, env=None, **kwargs)
```


---

## API Overview
```python
#! /usr/bin/python3

import pexpect

def main():
    child = pexpect.spawn("sh")
    child.expect("#")
    print(child.before)
    print(child.after)

    child.sendline("pwd")
    child.expect("#")
    print(child.before)
    print(child.after)
    child.close()

if __name__ == "__main__":
    main()
```
+++
## API Overview
```
root@aliyunHost:~/workspace/test# ./pe_test.py
b' pwd\r\n/root/workspace/test\r\n'
b'#'
root@aliyunHost:~/workspace/test#

```
+++
## API Overview

```sh
root@aliyunHost:~/workspace/test# sh
# pwd
/root/workspace/test
# exit
root@aliyunHost:~/workspace/test#

```


---
##  
```bash
root@aliyunHost:~/workspace/test# ssh demo@test.rebex.net
Password:
Welcome to Rebex Virtual Shell!
For a list of supported commands, type 'help'.
demo@ETNA:/$
demo@ETNA:/$ ls
aspnet_client
pub
readme.txt
demo@ETNA:/$
demo@ETNA:/$ pwd
/
demo@ETNA:/$
demo@ETNA:/$ exit
Disconnecting...
Connection to test.rebex.net closed.
root@aliyunHost:~/workspace/test#

```

---

```python
#! /usr/bin/python3

import pexpect as pe

def main():
    child = pe.spawn("ssh demo@test.rebex.net", timeout=30)
    result = child.expect([pe.EOF, pe.TIMEOUT, "Password"], 30)
    if result == 2:
        print("enter password ...")
        child.sendline("password")
        p0 = child.expect([pe.EOF, pe.TIMEOUT, "demo.*$"], 30)
        if p0 == 2:
            print("Login successful ...")
            child.sendline("pwd")
            p1 = child.expect([pe.EOF, pe.TIMEOUT, "demo"], 30)
            print("pwd " + str(p1) + "...")
            print(child.before)
            print(child.after)
            child.sendline("ls")
            p2 = child.expect([pe.EOF, pe.TIMEOUT, "demo"], 30)
            print("ls  " + str(p2) + "...")
            print(child.before)
            print(child.after)
        else:
            print("Login failed" + str(prompt))
    else:
        print("ssh connect failed")

    child.close()
    print("Bye bye")

if __name__ == "__main__":
    main()

```
