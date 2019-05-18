from datetime import datetime
import logging


def sum(num1, num2):
    return int(num1 + num2)

def subtract(num1, num2):
    return int(num1 - num2)

def multiply(num1, num2):
    return int(num1 * num2)

def divide(num1, num2):
    return num1 // num2

def power(num1, num2):
    return int(num1 ** num2)

def modulo(num1, num2):
    return int(num1 % num2)

def calculate(first_val, symbol, sencond_val):
    if symbol == '+':
        return sum(first_val, sencond_val)
    elif symbol == '-':
        return subtract(first_val, sencond_val)
    elif symbol == '*':
        return multiply(first_val, sencond_val)
    elif symbol == '/':
        if sencond_val == 0:
            logging.error("Can't divide by zero: " + str(first_val) + '/' + str(sencond_val) )
            raise Exception("Can't divide by zero: " + str(first_val) + '/' + str(sencond_val))
        return divide(first_val, sencond_val)
    elif symbol == '^':
        return power(first_val, sencond_val)
    elif symbol == '%':
        if sencond_val == 0:
            logging.error("Can't divide by zero: " + str(first_val) + '%' +str(sencond_val) )
            raise Exception("Can't divide by zero: " + str(first_val) + '%' + str(sencond_val))
        return modulo(first_val, sencond_val)

def calculate_all_occurences_of_operator(segment, operator):
    while operator in segment:
        index = segment.index(operator)
        result = calculate(segment[index - 1], operator, segment[index + 1])
        del segment[index - 1 : index + 2]
        segment.insert(index - 1, result)

    return segment

def calculate_expression_segment(segment):
    segment = calculate_all_occurences_of_operator(segment, '/')
    segment = calculate_all_occurences_of_operator(segment, '^')
    segment = calculate_all_occurences_of_operator(segment, '*')
    segment = calculate_all_occurences_of_operator(segment, '%')
    segment = calculate_all_occurences_of_operator(segment, '+')
    segment = calculate_all_occurences_of_operator(segment, '-')

    return segment[0]

def calculate_expression(expression):
    while '(' in expression:
        open_index = next(i for i in reversed(range(len(expression))) if expression[i] == '(')
        close_index = expression[open_index:].index(')') + open_index
        segment = expression[slice(open_index + 1, close_index)]
        result = calculate_expression_segment(segment)
        del expression[open_index : close_index+1]
        expression.insert(open_index, result)

    if len(expression): 
        expression = calculate_expression_segment(expression) 

    return expression