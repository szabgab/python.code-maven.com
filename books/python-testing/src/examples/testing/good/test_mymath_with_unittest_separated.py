import unittest
import mymath

class TestMath(unittest.TestCase):

    def test_add_2_3(self):
        self.assertEqual(mymath.add(2, 3), 5)

    def test_div_6_3(self):
        self.assertEqual(mymath.div(6, 3), 2)

    def test_div_42_1(self):
        self.assertEqual(mymath.div(42, 1), 42)

    def test_add_1_1(self):
        self.assertEqual(mymath.add(-1, 1), 0)

#if __name__ == '__main__':
#    unittest.main()
