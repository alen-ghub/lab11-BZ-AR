# https://github.com/alen-ghub/lab11-BZ-AR
# Partner 1: Brian Zheng
# Partner 2: Alen Rodriguez

import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    # Partner 2
    def test_add(self):  # 3 assertions
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(10, 20), 30)


    def test_subtract(self):
        self.assertEqual(subtract(2, 1), 1)
        self.assertEqual(subtract(30, 20), 10)
        self.assertEqual(subtract(100, 90), 10)

    ######## Partner 1
    def test_multiply(self):  # 3 assertions
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(5, 6), 30)
        self.assertEqual(mul(-1, 4), -4)

    def test_divide(self):  # 3 assertions
        self.assertEqual(div(4, 12), 3)
        self.assertEqual(div(6, 36), 6)
        self.assertEqual(div(5, 50), 10)

    # ##########################

    ######## Partner 2

    def test_divide_by_zero(self):  # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):  # 3 assertions
        self.assertEqual(logarithm(10, 10), 1)
        self.assertEqual(logarithm(2, 1), 0)
        self.assertEqual(logarithm(2, 8), 3)

    def test_log_invalid_base(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(-1, 10)

    ######## Partner 1
    def test_log_invalid_argument(self):  # 1 assertion
        try:
            logarithm(0, 5)
            result = "No Error"
        except ValueError:
            result = "ValueError"

    def test_hypotenuse(self):  # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5.0)
        self.assertEqual(hypotenuse(6, 8), 10.0)
        self.assertEqual(hypotenuse(5, 12), 13.0)

    def test_sqrt(self):  # 3 assertions
        self.assertEqual(square_root(49), 7)
        self.assertEqual(square_root(81), 9)
        self.assertEqual(square_root(4), 2)
    ##########################


# Do not touch this
if __name__ == "__main__":
    unittest.main()
