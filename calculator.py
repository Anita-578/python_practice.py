first = float(input("Enter first number: "))
second = float(input("Enter second number: "))
operation = input("Choose (+, -, *, /, %)")
if operation == "+":
    print(first + second)
elif operation == "-":
    print(first - second)
elif operation == "*":
    print(first * second)
elif operation == "/":
    print(first / second)
elif operation == "%":
    print(first % second)
else:
    print("Invalid operator")
