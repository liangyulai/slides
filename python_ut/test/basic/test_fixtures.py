# test_fixtures.py
import unittest

class fixturesClass(unittest.TestCase):

    def setUp(self):
        print('In setUp()')
        self.fixture = range(1, 10)

    def tearDown(self):
        print('In tearDown()')
        del self.fixture

    def test(self):
        print('a fixturesClass test case')
        self.assertEqual(self.fixture, range(1, 10))

if __name__ == '__main__':
    unittest.main()