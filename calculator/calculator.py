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
