def get_expression_arguments(args):
    head, *tail = args
    return tail

def remove_calculatorpy(expression):
    return [val.replace('calculator.py', '*') for val in expression]