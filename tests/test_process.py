from unittest import TestCase
from expression_processing import process

class CalculatorTest(TestCase):

    def test_get_expression_arguments(self):
        result = process.get_expression_arguments(['a', 'b', 'c'])
        self.assertEqual(result, ['b', 'c'])

    def test_remove_calculatorpy(self):
        result = process.remove_calculatorpy(['123', 'a', 'l', 'calculator.py', 'ldf'])
        self.assertEqual(result, ['123', 'a', 'l', '*', 'ldf'])

    def test_check_parenthesis_balance(self):
        with self.assertRaises(Exception): process.check_parenthesis_balance(['(', '(', ')', '(', ')'])

    def test_check_parenthesis_balance_again(self):
        result = process.check_parenthesis_balance(['(', '(', ')', '(', '2', '3', ')', ')'])
        self.assertEqual(result, True)

    def test_normalize_expression(self):
        result = process.normalize_expression(['(2*3-13+(03)-2*((3/31)*3)'])
        self.assertEqual(result, ['(', 2, '*', 3, '-', 13, '+', '(', 3, ')', '-', 2, '*', '(', '(', 3, '/', 31, ')', '*', 3, ')'])

    def test_normalize_expression_with_spaces(self):
        result = process.normalize_expression(['(  ', '30+2', '152/3-    2'])
        self.assertEqual(result, ['(', 30, '+', 2, 152, '/', 3, '-', 2])

    def test_close_parenthesis_position_as_first_item(self):
        result = process.is_close_parenthesis_position_correct('+', 0)
        self.assertEqual(result, False)

    def test_close_parenthesis_position_as_last_item(self):
        result = process.is_close_parenthesis_position_correct('', 3)
        self.assertEqual(result, True)

    def test_close_parenthesis_position_followed_by_open_parenthesis(self):
        result = process.is_close_parenthesis_position_correct('(', 6)
        self.assertEqual(result, False)

    def test_close_parenthesis_position_followed_by_number(self):
        result = process.is_close_parenthesis_position_correct('123', 6)
        self.assertEqual(result, False)

    def test_open_parenthesis_position_as_first_item(self):
        result = process.is_open_parenthesis_position_correct('+', 0)
        self.assertEqual(result, True)

    def test_open_parenthesis_position_as_last_item(self):
        result = process.is_open_parenthesis_position_correct('', 3)
        self.assertEqual(result, False)

    def test_open_parenthesis_position_followed_by_closing_parenthesis(self):
        result = process.is_open_parenthesis_position_correct(')', 6)
        self.assertEqual(result, False)


    def test_multiplication_symbol_position_as_first_item(self):
        result = process.is_multiplication_symbol_position_correct('2', 0)
        self.assertEqual(result, False)

    def test_multiplication_symbol_position_as_last_item(self):
        result = process.is_multiplication_symbol_position_correct('', 3)
        self.assertEqual(result, False)

    def test_multiplication_symbol_position_followed_by_sum_operator_symbol(self):
        result = process.is_multiplication_symbol_position_correct('+', 6)
        self.assertEqual(result, True)
    
    def test_multiplication_symbol_position_followed_by_multiplication_operator_symbol(self):
        result = process.is_multiplication_symbol_position_correct('*', 6)
        self.assertEqual(result, False)

    def test_multiplication_symbol_position_followed_by_close_parenthesis(self):
        result = process.is_multiplication_symbol_position_correct(')', 6)
        self.assertEqual(result, False)

    def test_multiplication_symbol_position_followed_by_open_parenthesis(self):
        result = process.is_multiplication_symbol_position_correct('(', 6)
        self.assertEqual(result, True)


    def test_division_symbol_position_as_first_item(self):
        result = process.is_division_symbol_position_correct('2', 0)
        self.assertEqual(result, False)

    def test_division_symbol_position_as_last_item(self):
        result = process.is_division_symbol_position_correct('', 3)
        self.assertEqual(result, False)

    def test_division_symbol_position_followed_by_sum_operator_symbol(self):
        result = process.is_division_symbol_position_correct('+', 6)
        self.assertEqual(result, True)
    
    def test_division_symbol_position_followed_by_multiplication_operator_symbol(self):
        result = process.is_division_symbol_position_correct('*', 6)
        self.assertEqual(result, False)

    def test_division_symbol_position_followed_by_close_parenthesis(self):
        result = process.is_division_symbol_position_correct(')', 6)
        self.assertEqual(result, False)

    def test_division_symbol_position_followed_by_open_parenthesis(self):
        result = process.is_division_symbol_position_correct('(', 6)
        self.assertEqual(result, True)


    def test_mod_symbol_position_as_first_item(self):
        result = process.is_mod_symbol_position_correct('2', 0)
        self.assertEqual(result, False)

    def test_mod_symbol_position_as_last_item(self):
        result = process.is_mod_symbol_position_correct('', 3)
        self.assertEqual(result, False)

    def test_mod_symbol_position_followed_by_sum_operator_symbol(self):
        result = process.is_mod_symbol_position_correct('+', 6)
        self.assertEqual(result, True)
    
    def test_mod_symbol_position_followed_by_multiplication_operator_symbol(self):
        result = process.is_mod_symbol_position_correct('*', 6)
        self.assertEqual(result, False)

    def test_mod_symbol_position_followed_by_close_parenthesis(self):
        result = process.is_mod_symbol_position_correct(')', 6)
        self.assertEqual(result, False)

    def test_mod_symbol_position_followed_by_open_parenthesis(self):
        result = process.is_mod_symbol_position_correct('(', 6)
        self.assertEqual(result, True)


    def test_power_symbol_position_as_first_item(self):
        result = process.is_power_symbol_position_correct(2, 0)
        self.assertEqual(result, False)

    def test_power_symbol_position_as_last_item(self):
        result = process.is_power_symbol_position_correct('', 3)
        self.assertEqual(result, False)

    def test_power_symbol_position_followed_by_sum_operator_symbol(self):
        result = process.is_power_symbol_position_correct('+', 6)
        self.assertEqual(result, True)
    
    def test_power_symbol_position_followed_by_multiplication_operator_symbol(self):
        result = process.is_power_symbol_position_correct('*', 6)
        self.assertEqual(result, False)

    def test_power_symbol_position_followed_by_close_parenthesis(self):
        result = process.is_power_symbol_position_correct(')', 6)
        self.assertEqual(result, False)

    def test_power_symbol_position_followed_by_open_parenthesis(self):
        result = process.is_power_symbol_position_correct('(', 6)
        self.assertEqual(result, True)


    def test_sum_symbol_position_followed_by_sum_operator_symbol(self):
        result = process.is_sum_symbol_position_correct('+')
        self.assertEqual(result, False)
    
    def test_sum_symbol_position_followed_by_multiplication_operator_symbol(self):
        result = process.is_sum_symbol_position_correct('*')
        self.assertEqual(result, False)

    def test_sum_symbol_position_followed_by_close_parenthesis(self):
        result = process.is_sum_symbol_position_correct(')')
        self.assertEqual(result, False)

    def test_sum_symbol_position_followed_by_open_parenthesis(self):
        result = process.is_sum_symbol_position_correct('(')
        self.assertEqual(result, True)


    def test_subtraction_symbol_position_followed_by_sum_operator_symbol(self):
        result = process.is_subtraction_symbol_position_correct('+')
        self.assertEqual(result, False)
    
    def test_subtraction_symbol_position_followed_by_multiplication_operator_symbol(self):
        result = process.is_subtraction_symbol_position_correct('*')
        self.assertEqual(result, False)

    def test_subtraction_symbol_position_followed_by_close_parenthesis(self):
        result = process.is_subtraction_symbol_position_correct(')')
        self.assertEqual(result, False)

    def test_subtraction_symbol_position_followed_by_open_parenthesis(self):
        result = process.is_subtraction_symbol_position_correct('(')
        self.assertEqual(result, True)


    def test_expression_validation(self):
        result = process.validate_expression(['(', 2, '+', 3, ')', '/', 2])
        self.assertEqual(result, True)

    def test_expression_validation_finishing_multiplication(self):
        with self.assertRaises(Exception): process.validate_expression(['(', 2, '+', 3, ')', '/', 2, '*'])

    def test_expression_validation_with_parenthesis_only(self):
        with self.assertRaises(Exception): process.validate_expression(['(', ')'])