import sys
import logging
from calculation import calculation
from expression_processing import process

def start(expression):
    logging.basicConfig(filename='calculator.log', level=logging.DEBUG, 
                        format='%(levelname)s %(asctime)s %(message)s', 
                        datefmt='%d/%m/%Y %H:%M:%S')
    logging.info('Calculating: ' + ''.join(expression))

    expression = process.remove_calculatorpy(expression)
    expression = process.normalize_expression(expression)
    original_expression = expression.copy()
    process.check_parenthesis_balance(expression)
    process.validate_expression(expression)
    result = calculation.calculate_expression(expression)

    print(str(result))

    logging.info('Calculated: ' + ''.join([str(item) for item in original_expression]) + ' = ' + str(result))

if __name__  == '__main__':
    expression_parameters = process.get_expression_arguments(sys.argv)
    start(expression_parameters)