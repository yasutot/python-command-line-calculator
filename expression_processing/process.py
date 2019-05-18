from datetime import datetime
import logging


def get_expression_arguments(args):
    head, *tail = args
    return tail

def remove_calculatorpy(expression):
    return [val.replace('calculator.py', '*') for val in expression]

# def are_parenthesis_balanced(expression):
def check_parenthesis_balance(expression):
    parenthesis_queue = []
    for item in expression:
        if item == '(':
            parenthesis_queue.append('(')
        elif item == ')' and len(parenthesis_queue):
            if parenthesis_queue[-1] == '(':
                parenthesis_queue.pop()
            else:
                parenthesis_queue.append(')')

    if len(parenthesis_queue):
        logging.error('Invalid parenthesis')
        raise Exception('Invalid parenthesis')

    return True

def normalize_expression(expression):
    normalized = []
    for segment in expression:
        if segment.isdigit():
            normalized.append(int(segment))

        else:
            digits = ''
            for char in segment:
                if char == ' ':
                    if len(digits):
                        normalized.append(int(digits))
                        digits = ''
                        continue

                elif char.isdigit():
                    digits = digits + char

                else:
                    if len(digits): normalized.append(int(digits))
                    normalized.append(char)
                    digits = ''

            if len(digits): normalized.append(int(digits))

    return normalized

def is_sum_symbol_position_correct(next_val):
    return type(next_val) is int or str(next_val) == "("

def is_subtraction_symbol_position_correct(next_val):
    return type(next_val) is int or str(next_val) == "(" 

def is_multiplication_symbol_position_correct(next_val, index):
    return index != 0 and next_val != '' and (type(next_val) is int or next_val in "(+-")

def is_division_symbol_position_correct(next_val, index):
    return index != 0 and next_val != '' and (type(next_val) is int or next_val in "(+-")

def is_mod_symbol_position_correct(next_val, index):
    return index != 0  and next_val != '' and (type(next_val) is int or next_val in "(+-")

def is_power_symbol_position_correct(next_val, index):
    return index != 0 and next_val != '' and (type(next_val) is int or next_val in '(+-')

def is_open_parenthesis_position_correct(next_val, index):
    return next_val != '' and (str(next_val) in '(+-' or type(next_val) is int)

def is_close_parenthesis_position_correct(next_val, index):
    return index != 0 and (str(next_val) in '+-*/%^)' or next_val == '')

def is_symbol_correct(symbol, next_val, index):
    return {
        '+': is_sum_symbol_position_correct(next_val),
        '-': is_subtraction_symbol_position_correct(next_val),
        '*': is_multiplication_symbol_position_correct(next_val, index),
        '/': is_division_symbol_position_correct(next_val, index),
        '%': is_mod_symbol_position_correct(next_val, index),
        '^': is_power_symbol_position_correct(next_val, index),
        '(': is_open_parenthesis_position_correct(next_val, index),
        ')': is_close_parenthesis_position_correct(next_val, index)
    }[symbol]

def validate_expression(expression):
    invalid_chars = []
    for index, value in enumerate(expression):
        next_value = expression[index + 1] if len(expression) - 1 > index else ''
        if type(value) is not int:
            if str(value) in '+-*/^%()':
                if not is_symbol_correct(value, next_value, index):
                    logging.error('Error near symbol ' + value)
                    raise Exception('Error near symbol ' + value)
            else:
                invalid_chars.append(value)

    if len(invalid_chars):
        logging.error('Invalid characters: ' + ' '.join(invalid_chars))
        raise Exception('Invalid characters: ' + ' '.join(invalid_chars))
    else:
        return True