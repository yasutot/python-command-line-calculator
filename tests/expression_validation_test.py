from unittest import TestCase
from validation import expression_validation

class CalculatorTest(TestCase):

    def test_get_expression_arguments(self):
        result = expression_validation.get_expression_arguments(["a", "b", "c"])
        self.assertEqual(result, ["b", "c"])

    def test_remove_calculatorpy(self):
        result = expression_validation.remove_calculatorpy(['123', 'a', 'l', 'calculator.py', 'ldf'])
        self.assertEqual(result, ['123', 'a', 'l', '*', 'ldf'])