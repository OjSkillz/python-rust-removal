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

def add(first_number, second_number):
    return int(first_number) + int(second_number)

def subtract(first_number, second_number):
    return int(first_number) - int(second_number)

def multiply(first_number, second_number):
    return int(first_number) * int(second_number)

def divide(first_number, second_number):
    return int(first_number) / int(second_number)