
Testing with Python unittest

|||

* 单元测试框架（unittest）
* 测试脚手架 （test fixture）
* 测试用例 （unittest 基类： unittest.TestCase）
* 测试套件 （test suite）
* 测试运行器（test runner）

Standard library documentation for unittest: 
https://docs.python.org/3.7/library/unittest.html


|||
Basic Test Structure

```python
# test_simple.py
import unittest

class SimplisticTest(unittest.TestCase):

    def test(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
```

+++

```bash
$ python3 test_simple.py

.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

+++ 
 
```bash
$ python3 test_simple.py -v

test (__main__.SimplisticTest) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```


+++

The standard workflow is:

1. Import unittest from the standard library
2. Create your own class derived from the TestCase class
3. Create the test functions(start with 'test_') into methods by adding self as the first argument
4. Use the self.assertEqual() method on the TestCase class
5. Run the tests by placing unittest.main() in your file, usually at the bottom.


|||

Test Fixtures

```python
# test_fixtures.py
import unittest

class FixturesTest(unittest.TestCase):

    def setUp(self):
        print('In setUp()')
        self.fixture = range(1, 10)

    def tearDown(self):
        print('In tearDown()')
        del self.fixture

    def test(self):
        print('in test()')
        self.assertEqual(self.fixture, range(1, 10))

if __name__ == '__main__':
    unittest.main()
```


+++

```bash
$ python3 test_fixtures.py

.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
In setUp()
in test()
In tearDown()

```

|||

```python
# unittest_fixtures.py

import random
import unittest

def setUpModule():
    print('In setUpModule()')

def tearDownModule():
    print('In tearDownModule()')

class FixturesTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('In setUpClass()')
        cls.good_range = range(1, 10)

    @classmethod
    def tearDownClass(cls):
        print('In tearDownClass()')
        del cls.good_range

    def setUp(self):
        super().setUp()
        print('\nIn setUp()')
        # Pick a number sure to be in the range. The range is
        # defined as not including the "stop" value, so make
        # sure it is not included in the set of allowed values
        # for our choice.
        self.value = random.randint(
            self.good_range.start,
            self.good_range.stop - 1,
        )

    def tearDown(self):
        print('In tearDown()')
        del self.value
        super().tearDown()

    def test1(self):
        print('In test1()')
        self.assertIn(self.value, self.good_range)

    def test2(self):
        print('In test2()')
        self.assertIn(self.value, self.good_range)

```

+++

```bash
$ python3 -u -m unittest -v unittest_fixtures.py

In setUpModule()
In setUpClass()
test1 (unittest_fixtures.FixturesTest) ...
In setUp()
In test1()
In tearDown()
ok
test2 (unittest_fixtures.FixturesTest) ...
In setUp()
In test2()
In tearDown()
ok
In tearDownClass()
In tearDownModule()

----------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

|||

Mock & MagicMock & Patch

* Mock is a flexible mock object intended to replace the use of stubs and test doubles throughout your code. 
* MagicMock is a subclass of Mock with all the magic methods pre-created and ready to use. 
* The patch() decorators makes it easy to temporarily replace classes in a particular module with a Mock object.

+++

A MagicMock instance can:

    capture the arguments that the method is called with
    count how many times it’s called
    return values that we specify
    return the same or different values each time the mocked method is called
    be made to raise errors
