from unittest import TestCase
from calculator import calculator

class CalculatorTest(TestCase):

    def test_sum(self):
        result = calculator.sum(2, 2)
        self.assertEqual(result, 4)

    def test_another_sum(self):
        result = calculator.sum(10, 23)
        self.assertEqual(result, 33)