import sys
from calculation import calculation
from expression_processing import process

def start(expression):
    expression = process.remove_calculatorpy(expression)
    expression = process.normalize_expression(expression)
    if not process.are_parenthesis_balanced(expression):
        raise Exception('Parenthesis in wrong position')
    process.validate_expression(expression)
    result = calculation.calculate_expression(expression)
    print(result)

if __name__  == '__main__':
    expression_parameters = process.get_expression_arguments(sys.argv)
    start(expression_parameters)