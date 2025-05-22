def calculator(a, b, operator):
    match operator:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            return a / b
        case '//':
            return a // b
        case '%':
            return a % b
        case '**':
            return a ** b
        case '==':
            return a == b
        case '>':
            return a > b
        case '<':
            return a < b
        case 'and':
            return a and b
        case 'or':
            return a or b
        case 'not':
            return not a
        case _:
            return "Invalid operator"

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator (+, -, *, /, //, %, **, ==, >, <, and, or, not): ")

result = calculator(a, b, op)
print("Result:", result)
