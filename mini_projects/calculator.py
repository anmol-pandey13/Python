# Calculator using match-case
# Python 3.10+

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

match operator:
    case "+":
        result = num1 + num2

    case "-":
        result = num1 - num2

    case "*":
        result = num1 * num2

    case "/":
        if num2 == 0:
            result = "Cannot divide by zero"
        else:
            result = num1 / num2

    case _:
        result = "Invalid operator"

print("Result:", result)