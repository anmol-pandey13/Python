# Number Guessing Game

import random

secret_number = random.randint(1, 10)

print("Guess the number between 1 and 10.")

while True:
    guess = int(input("Your guess: "))

    if guess == secret_number:
        print("Correct! You guessed it.")
        break

    elif guess < secret_number:
        print("Too low!")

    else:
        print("Too high!")