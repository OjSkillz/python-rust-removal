# collect first number from user
# collect operand or operator from user
# collect second number from user
# return result of operation

def calculate(first_number, operator, second_number):
    if operator == "+":
        return add(first_number, second_number)
    elif operator == '-':
        return subtract(first_number, second_number)
    elif operator == '*' or operator == 'x'.lower():
        return multiply(first_number, second_number)
    elif operator == '/':
        return divide(first_number, second_number)

    return "Invalid Operation"

def add(first, second):
    return first + second

def subtract(first, second):
    return first - second

def multiply(first, second):
    return first * second

def divide(first, second):
    return first / second

first_input = input("Enter first number: ")
operand = input("Enter operator ('+', '-', '* or x', and '/'): " )
second_input = input("Enter second number: ")

print(calculate(first_input, operand, second_input))

