from unittest import TestCase
from calculator import calculator

class CalculatorTest(TestCase):

    def test_sum(self):
        result = calculator.sum(2, 2)
        self.assertEqual(result, 4)

    def test_another_sum(self):
        result = calculator.sum(10, 23)
        self.assertEqual(result, 33)
    
    def test_sum_negative_numbers(self):
        result = calculator.sum(-3, -18)
        self.assertEqual(result, -21)

    def test_subtract(self):
        result = calculator.subtract(5,3)
        self.assertEqual(result, 2)

    def test_subtract_negative_numbers(self):
        result = calculator.subtract(-10, -2)
        self.assertEqual(result, -8)

    def test_multiply(self):
        result = calculator.multiply(5, 5)
        self.assertEqual(result, 25)

    def test_another_multiplication(self):
        result = calculator.multiply(-3, -6)
        self.assertEqual(result, 18)