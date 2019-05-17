from unittest import TestCase
from expression_processing import process

class CalculatorTest(TestCase):

    def test_get_expression_arguments(self):
        result = process.get_expression_arguments(["a", "b", "c"])
        self.assertEqual(result, ["b", "c"])

    def test_remove_calculatorpy(self):
        result = process.remove_calculatorpy(['123', 'a', 'l', 'calculator.py', 'ldf'])
        self.assertEqual(result, ['123', 'a', 'l', '*', 'ldf'])

    def test_are_parenthesis_balanced(self):
        result = process.test_are_parenthesis_balanced(["(", "(", ")", "(", ")"])
        self.assertEqual(result, False)
    
    def test_are_parenthesis_balanced_again(self):
        result = process.test_are_parenthesis_balanced(["(", "(", ")", "(", "2", "3" ")", ")"])
        self.assertEqual(result, True)