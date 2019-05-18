def sum(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if (num2 == 0):
        raise Exception("Cannot divide by zero")

    return num1 // num2

def power(num1, num2):
    return int( num1 ** num2 )

def modulo(num1, num2):
    return num1 % num2

def calculate(first_val, symbol, sencond_val):
    if symbol == '+':
        return sum(int(first_val), int(sencond_val))
    elif symbol == '-':
        return subtract(int(first_val), int(sencond_val))
    elif symbol == '*':
        return multiply(int(first_val), int(sencond_val))
    elif symbol == '/':
        if sencond_val == '0':
            raise Exception("Can't divide by zero: " + first_val, '/', sencond_val)
        return divide(int(first_val), int(sencond_val))
    elif symbol == '^':
        return power(int(first_val), int(sencond_val))
    elif symbol == '%':
        if sencond_val == '0':
            raise Exception("Can't divide by zero: " + first_val, '%', str(int(sencond_val)))
        return modulo(int(first_val), int(sencond_val))

def calculate_all_occurences_of_operator(segment, operator):
    while operator in segment:
        index = segment.index(operator)
        result = calculate(segment[index - 1], operator, segment[index + 1])
        del segment[index - 1 : index + 2]
        segment.insert(index - 1, str(result))

    return segment