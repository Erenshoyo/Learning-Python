# Python calculator

num1 = float(input("Enter the first number: "))

num2 = float(input("Enter the second number: "))

operator = input("Enter an operation ( + , - , * , / ):")

if operator == "+":
    result = num1 + num2
    print(result)

elif operator == "-":
    result = num1 - num2
    print(result)

elif operator == "*":
    result = num1 * num2
    print(result)

elif operator == "/":
    result = num1 / num2
    print(result)
else:
    print(f"{operator} is not a valid operation")