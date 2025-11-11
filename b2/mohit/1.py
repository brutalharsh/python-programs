import random

print(" Welcome to the Number Guessing Game!")

secret_number = random.randint(1, 10)

for attempt in range(1, 6):
    guess = int(input(f"\nAttempt {attempt}/5 - Enter your guess (1 to 10): "))

    if guess == secret_number:
        print(" Boom! You guessed it right!")
        break
    elif guess < secret_number:
        print("Too low! Try a bit higher.")
    else:
        print("Too high! Try a bit lower.")

else:
   
    print(f"\n  The correct number was {secret_number}.")

print(" Thanks for playing!")
