def calculator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b
    elif operator == '//':
        return a // b
    elif operator == '%':
        return a % b
    elif operator == '**':
        return a ** b
    elif operator == '==':
        return a == b
    elif operator == '>':
        return a > b
    elif operator == '<':
        return a < b
    elif operator == 'and':
        return a and b
    elif operator == 'or':
        return a or b
    elif operator == 'not':
        return not a
    else:
        return "Invalid operator"

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator (+, -, *, /, //, %, **, ==, >, <, and, or, not): ")

result = calculator(a, b, op)
print("Result:", result)
