# Datetime and Random Module

import random
from datetime import datetime

# Current date and time
now = datetime.now()

print("Current date:", now.date())
print("Current time:", now.strftime("%H:%M:%S"))

# Generate random numbers
print("\nRandom numbers:")

for i in range(5):
    number = random.randint(1, 100)
    print(number)