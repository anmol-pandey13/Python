# Python Functions

def greet(name):
    return f"Hello, {name}!"


def calculate_average(numbers):
    return sum(numbers) / len(numbers)


print(greet("Anmol"))

marks = [80, 75, 90, 85]

average = calculate_average(marks)

print("Marks:", marks)
print("Average:", average)