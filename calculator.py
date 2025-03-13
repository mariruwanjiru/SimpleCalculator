num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter an operation (+, -, *, /): ")

if operation == '+':
    print(f"Result: {num1 + num2}")
elif operation == '-':
    print(f"Result: {num1 - num2}")
elif operation == '*':
    print(f"Result: {num1 * num2}")
elif operation == '/':
    print("Error: Division by zero" if num2 == 0 else f"Result: {num1 / num2}")
else:
    print("Invalid operation")