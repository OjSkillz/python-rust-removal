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

