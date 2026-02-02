# collect first number from user
# collect operand or operator from user
# collect second number from user
# return result of operation

def calculate(first_number, operator, second_number):
    if operator == '+':
        add(first_number, second_number)
    elif operator == '-':
        subtract(first_number, second_number)
    elif operator == '*' or operator == 'x'.lower():
        multiply(first_number, second_number)
    elif operator == '/':
        divide(first_number, second_number)
    return "Invalid Operation"

def add(first, second):
    return int(first) + int(second)

def subtract(first, second):
    return int(first) - int(second)

def multiply(first, second):
    return int(first) * int(second)

def divide(first, second):
    return int(first) / int(second)

first_input = input("Enter first number: ")
operand = input("Enter operator ('+', '-', '* or x', and '/': " )
second_input = input("Enter second number: ")

calculate(first_input, operand, second_input)

