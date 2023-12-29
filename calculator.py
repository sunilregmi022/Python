a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))
operator = input("Enter the operator (+, -, *, /): ")
2
def calculator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b != 0:  
            return a / b
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operator"
result = calculator(a,b,operator)
print(f"Result: {result}")
