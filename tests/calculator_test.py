from unittest import TestCase
from calculator import calculation

class calculationTest(TestCase):

    def test_sum(self):
        result = calculation.sum(2, 2)
        self.assertEqual(result, 4)

    def test_another_sum(self):
        result = calculation.sum(10, 23)
        self.assertEqual(result, 33)
    
    def test_sum_negative_numbers(self):
        result = calculation.sum(-3, -18)
        self.assertEqual(result, -21)

    def test_subtract(self):
        result = calculation.subtract(5,3)
        self.assertEqual(result, 2)

    def test_subtract_negative_numbers(self):
        result = calculation.subtract(-10, -2)
        self.assertEqual(result, -8)

    def test_multiply(self):
        result = calculation.multiply(5, 5)
        self.assertEqual(result, 25)

    def test_another_multiplication(self):
        result = calculation.multiply(-3, -6)
        self.assertEqual(result, 18)

    def test_divide(self):
        result = calculation.divide(6, 3)
        self.assertEqual(result, 2)
    
    def test_division_by_zero(self):
        with self.assertRaises(Exception): calculation.divide(10, 0)

    def test_exponentiation(self):
        result = calculation.power(3, 3)
        self.assertEqual(result, 27)

    def test_another_exponentiation(self):
        result = calculation.power(9, -2)
        self.assertEqual(result, 0)

    def test_modulo(self):
        result = calculation.modulo(10, 3)
        self.assertEqual(result, 1)

    def test_modulo_again(self):
        result = calculation.modulo(10, -3)
        self.assertEqual(result, -2)

    def test_calculate(self):
        result = calculation.calculate('12', '-', '3')
        self.assertEqual(result, 9)

    def test_calculate_division_by_zero(self):
        with self.assertRaises(Exception): calculation.calculate('12', '/', '0')

    def test_calculate_occurences_of_multiplication(self):
        result = calculation.calculate_all_occurences_of_operator(['2','*','3','+','1','-','0'], '*')
        self.assertEqual(result, ['6', '+', '1', '-', '0'])

    def test_calculate_occurences_of_multiple_multiplications(self):
        result = calculation.calculate_all_occurences_of_operator(['2','*','3','+','1','-','0', '-', '5', '*', '100', '-', '2'], '*')
        self.assertEqual(result, ['6','+','1','-','0', '-', '500', '-', '2'])