import random

number = random.randint(1, 10)
guess = 0 
attempts = 0

print(" Guess the number between 1 and 10!")

while guess != number:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == number:
        print(f" You got it right in {attempts} tries! ")
    elif guess < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

print("Game Over ")

