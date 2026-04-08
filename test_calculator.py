import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
def test_multiply(self): # 3 assertions
    self.assertEqual(mul(3, 4), 12)
    self.assertEqual(mul(5, 6), 30)
    self.assertEqual(mul(-1, 4), -4)

def test_divide(self): # 3 assertions
    self.assertEqual(div(12, 4), 3)
    self.assertEqual(div(36, 6), 6)
    self.assertEqual(div(-50, 5), -10)
    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
def test_log_invalid_argument(self): # 1 assertion
    try:
        logarithm(0, 5)
        result = "No Error"
    except ValueError:
        result = "ValueError"

def test_hypotenuse(self): # 3 assertions
    self.assertEqual(hypotenuse(3, 4), 5.0)
    self.assertEqual(hypotenuse(6, 8), 10.0)
    self.assertEqual(hypotenuse(5, 12), 13.0)

def test_sqrt(self): # 3 assertions
    self.assertEqual(square_root(49), 7)
    self.assertEqual(square_root(81), 9)
    self.assertEqual(square_root(4), 2)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()