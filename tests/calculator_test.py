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

    def test_divide(self):
        result = calculator.divide(6, 3)
        self.assertEqual(result, 2)
    
    def test_division_by_zero(self):
        with self.assertRaises(Exception): calculator.divide(10, 0)

    def test_exponentiation(self):
        result = calculator.power(3, 3)
        self.assertEqual(result, 27)

    def test_another_exponentiation(self):
        result = calculator.power(9, -2)
        self.assertEqual(result, 0)

    def test_modulo(self):
        result = calculator.modulo(10, 3)
        self.assertEqual(result, 1)

    def test_modulo_again(self):
        result = calculator.modulo(10, -3)
        self.assertEqual(result, -2)