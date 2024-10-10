while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /) or 'exit' to quit: ")

    if operator == "exit":
        break
    elif operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        if num2 != 0:
            print(num1 / num2)
        else:
            print("Division by zero is not allowed")
    else:
        print("Invalid operator")
