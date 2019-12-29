# test_simple.py
import unittest

class simpleClass(unittest.TestCase):

    def test(self):
        self.assertTrue(True)
    
    def not_run(self):
        self.assertFalse(True)

if __name__ == '__main__':
    unittest.main()