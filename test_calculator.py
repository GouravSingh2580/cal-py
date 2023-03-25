# test_calculator.py

import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculator.calculate("2 + 2"), 4)

    def test_subtraction(self):
        self.assertEqual(calculator.calculate("5 - 3"), 2)

    def test_multiplication(self):
        self.assertEqual(calculator.calculate("4 * 6"), 24)

    def test_division(self):
        self.assertEqual(calculator.calculate("10 / 2"), 5)

    def test_invalid_expression(self):
        with self.assertRaises(Exception):
            calculator.calculate("2 + abc")

if __name__ == '__main__':
    unittest.main()
