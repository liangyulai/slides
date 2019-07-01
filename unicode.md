## An introduction of unicode in Python

* [Python 2 codecs](https://docs.python.org/2/library/codecs.html)
* [Python 3 codecs](https://docs.python.org/3/library/codecs.html)
* [Pyhton 2 unicode](https://docs.python.org/2/howto/unicode.html)
* [Python 3 unicode](https://docs.python.org/3/howto/unicode.html)


--

```
kirin@kawagarbo:~/workspace/repo$ python2
Python 2.7.15rc1 (default, Nov 12 2018, 14:31:15)
[GCC 7.3.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys.getdefaultencoding()
'ascii'
>>> exit()
```

--

```
kirin@kawagarbo:~/workspace/repo$ python3
Python 3.6.5 (default, Apr  1 2018, 05:46:30)
[GCC 7.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys.getdefaultencoding()
'utf-8'
>>> exit()
kirin@kawagarbo:~/workspace/repo$

```

---
### reference
* [The Unicode Standard](https://www.unicode.org/standard/standard.html)
* [](http://www.unicode.org/charts/)
* [UTF-8 encoding table and Unicode characters](https://www.utf8-chartable.de/unicode-utf8-table.pl?utf8=0x)
* [Github: Cpython](https://github.com/python/cpython)
* [Github: typeshed](https://github.com/python/typeshed)
* [Github: mypy](https://github.com/python/mypy)
* [mypy-lang.org](http://www.mypy-lang.org/)
* [PEP 484 -- Type Hints](https://www.python.org/dev/peps/pep-0484/)

---

Note:

```
https://stackoverflow.com/questions/3001177/how-do-i-grep-for-all-non-ascii-characters

You can use the command:

grep --color='auto' -P -n "[\x80-\xFF]" file.xml

This will give you the line number, and will highlight non-ascii chars in red.

In some systems, depending on your settings, the above will not work, so you can grep by the inverse

grep --color='auto' -P -n "[^\x00-\x7F]" file.xml

```


---
Note:
```
Retrieving python module path

import a_module
print a_module.__file__

Will actually give you the path to the .pyc file that was loaded, at least on Mac OS X. So I guess you can do

import os
path = os.path.dirname(amodule.__file__)

You can also try

path = os.path.abspath(amodule.__file__)

To get the directory to look for changes.

```