import unittest
from fibonacci import fib

class TestFibo(unittest.TestCase):

    def test_1(self):
        self.assertEqual(fib(1), 0)

    def test_7(self):
        self.assertEqual(fib(7), 8)

    def test_10(self):
        self.assertEqual(fib(10), 34)

    def test_42(self):
        self.assertEqual(fib(42), 165580141)

