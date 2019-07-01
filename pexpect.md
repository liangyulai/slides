
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
class pexpect.spawn(command, args=[], timeout=30, maxread=2000, searchwindowsize=None, logfile=None, cwd=None, env=None, ignore_sighup=False, echo=True, preexec_fn=None, encoding=None, codec_errors='strict', dimensions=None, use_poll=False)
```

* run function
```python
pexpect.run(command, timeout=30, withexitstatus=False, events=None, extra_args=None, logfile=None, cwd=None, env=None, **kwargs)
```

```shell
root@aliyunHost:~/workspace/test# sh
#
# pwd
/root/workspace/test
#
# exit
root@aliyunHost:~/workspace/test#
root@aliyunHost:~
```
+++
## API Overview
```shell
root@aliyunHost:~
root@aliyunHost:~# python3
Python 3.6.7 (default, Oct 22 2018, 11:32:17)
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import pexpect
>>>
>>> child = pexpect.spawn("sh")
>>> child.expect("#")
0
>>> child.sendline("pwd")
4
>>> child.expect("#")
0
>>> print(child.before)
b' pwd\r\n/root\r\n'
>>> print(child.after)
b'#'

```
+++
## API Overview
```python
#! /usr/bin/python3

import pexpect

def main():
    child = pexpect.spawn("sh")
    child.expect("#")
    child.sendline("pwd")
    child.expect("#")
    print(child.before)
    print(child.after)

if __name__ == "__main__":
    main()
```
+++
## API Overview
```
root@aliyunHost:~/workspace/test# ./test_p.py
b' pwd\r\n/root/workspace/test\r\n'
b'#'
root@aliyunHost:~/workspace/test#

```
+++
## API Overview





---
##  

ssh demo@test.rebex.net

Note:
