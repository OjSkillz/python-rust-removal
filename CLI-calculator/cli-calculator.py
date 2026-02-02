# collect first number from user
# collect operand or operator from user
# collect second number from user
# return result of operation

def calculate(first_number, operator, second_number):
    if operator == "+":
        return add(first_number, second_number)
    elif operator == '-':
        return subtract(first_number, second_number)
    elif operator in ('*', 'x', 'X'):
        return multiply(first_number, second_number)
    elif operator == '/':
        return divide(first_number, second_number)

    return "Invalid Operator"

def add(first, second):
    return first + second

def subtract(first, second):
    return first - second

def multiply(first, second):
    return first * second

def divide(first, second):
    if second == 0:
        return "Error division by zero"
    return first / second


try:
    first_input = float(input("Enter first number: "))
    operand = input("Enter operator ('+', '-', '* or x', and '/'): " )
    second_input = float(input("Enter second number: "))

    result = calculate(first_input, operand, second_input)
    print(f"{first_input} {operand} {second_input} = {result}")

except ValueError:
    print("Please enter a valid number!\n")
