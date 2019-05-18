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
        result = process.are_parenthesis_balanced(["(", "(", ")", "(", ")"])
        self.assertEqual(result, False)

    def test_are_parenthesis_balanced_again(self):
        result = process.are_parenthesis_balanced(["(", "(", ")", "(", "2", "3", ")", ")"])
        self.assertEqual(result, True)

    def test_normalize_expression(self):
        result = process.normalize_expression(["(2*3-13+(03)-2*((3/31)*3)"])
        self.assertEqual(result, ["(", "2", "*", "3", "-", "13", "+", "(", "03", ")", "-", "2", "*", "(", "(", "3", "/", "31", ")", "*", "3", ")"])

    def test_normalize_expression_with_spaces(self):
        result = process.normalize_expression(["(  ", "30+2", "152/3-    2"])
        self.assertEqual(result, ["(", "30", "+", "2", "152", "/", "3", "-", "2"])

    def test_close_parenthesis_position_as_first_item(self):
        result = process.is_close_parenthesis_position_correct('+', 0)
        self.assertEqual(result, False)

    def test_close_parenthesis_position_as_last_item(self):
        result = process.is_close_parenthesis_position_correct('', 3)
        self.assertEqual(result, True)

    def test_close_parenthesis_position_followed_by_open_parenthesis(self):
        result = process.is_close_parenthesis_position_correct('(', 6)
        self.assertEqual(result, False)