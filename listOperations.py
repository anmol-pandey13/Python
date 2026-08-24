# List Operations

numbers = [10, 20, 30, 40, 50]

print("Original list:", numbers)

numbers.append(60)
print("After append:", numbers)

numbers.insert(0, 5)
print("After insert:", numbers)

numbers.remove(30)
print("After remove:", numbers)

print("Length:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))