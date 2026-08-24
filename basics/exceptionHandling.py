# Exception Handling

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 / num2

    print("Result:", result)

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError:
    print("You cannot divide by zero.")

finally:
    print("Program finished.")