# test.py
import unittest
from mock import patch, MagicMock
from apps.foo import foo

class MyTest(unittest.TestCase):

    @patch("foo.Bar.biz") # not -> @patch("bar.Bar.biz")
    def test_foo(self, mock_biz):
        self.assertFalse(mock_biz.called)

        foo()

        self.assertTrue(mock_biz.called)
        self.assertEqual(mock_biz.call_count, 1)
        self.assertIsInstance(mock_biz, MagicMock)