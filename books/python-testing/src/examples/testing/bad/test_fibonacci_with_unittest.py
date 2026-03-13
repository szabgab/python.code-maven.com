import unittest
from fibonacci import fib

class TestFibo(unittest.TestCase):

    def test_fib(self):
        self.assertEqual(fib(7), 8)
        self.assertEqual(fib(10), 34)
        self.assertEqual(fib(42), 165580141)

