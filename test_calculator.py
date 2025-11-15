# https://github.com/egladron/lab10-EL-JL
# Partner 1: Edwin Ladron de Guevara
# Partner 2: Joshua Lovett

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(26, 2), 28)
        self.assertEqual(add(-3, 3), 0)
        self.assertEqual(add(0, 0), 0)
    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(12, 14), -2)
        self.assertEqual(subtract(0, 3), -3)
        self.assertEqual(subtract(6, 2), 4)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3, 3), 9)
        self.assertEqual(mul(-2, -10), 20)
        self.assertAlmostEqual(mul(0.5, 10), 5)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(10, 5), 2)
        self.assertEqual(div(100, -5), -20)
        self.assertAlmostEqual(div(5, 2), 2.5)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)
    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(2, 16), 4)
        self.assertAlmostEqual(logarithm(4, 16), 2)
        self.assertAlmostEqual(logarithm(5, 125), 3)
    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(1, 10)

    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0,5)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(8, 15), 17)

    def test_sqrt(self):  # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertAlmostEqual(square_root(16), 4)
        self.assertAlmostEqual(square_root(4), 2)

    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
