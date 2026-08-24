# Conditions and Loops

temperature = 32

if temperature >= 35:
    print("Very Hot")
elif temperature >= 25:
    print("Warm")
else:
    print("Cool")


print("\nNumbers from 1 to 10:")

for number in range(1, 11):
    print(number)


print("\nCountdown:")

count = 5

while count > 0:
    print(count)
    count -= 1

print("Done!")