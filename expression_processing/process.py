def get_expression_arguments(args):
    head, *tail = args
    return tail

def remove_calculatorpy(expression):
    return [val.replace('calculator.py', '*') for val in expression]

def are_parenthesis_balanced(expression):
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
        return False

    return True

def normalize_expression(expression):
    normalized = []
    for segment in expression:
        if segment.isdigit():
            normalized.append(segment)

        else:
            digits = ''
            for char in segment:
                if char == ' ':
                    if len(digits):
                        normalized.append(digits)
                        digits = ''
                        continue

                elif char.isdigit():
                    digits = digits + char
                
                else:
                    if len(digits): normalized.append(digits)
                    normalized.append(char)
                    digits = ''

            if len(digits): normalized.append(digits)

    return normalized

def is_sum_symbol_position_correct(next_val):
    return next_val.isdigit() or next_val == "("

def is_subtraction_symbol_position_correct(next_val):
    return next_val.isdigit() or next_val == "(" 

def is_multiplication_symbol_position_correct(next_val, index):
    return index != 0 and next_val != '' and (next_val.isdigit() or next_val in "(+-")

def is_division_symbol_position_correct(next_val, index):
    return index != 0 and next_val != '' and (next_val.isdigit() or next_val in "(+-")

def is_mod_symbol_position_correct(next_val, index):
    return index != 0  and next_val != '' and (next_val.isdigit() or next_val in "(+-")

def is_power_symbol_position_correct(next_val, index):
    return index != 0 and next_val != '' and (next_val.isdigit() or next_val in '(+-')

def is_open_parenthesis_position_correct(next_val, index):
    return next_val != '' and (next_val in '(+-' or next_val.isdigit())

def is_close_parenthesis_position_correct(next_val, index):
    return index != 0 and (next_val in '+-*/%^)' or next_val == '')