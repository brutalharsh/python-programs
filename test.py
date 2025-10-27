import random

print("Welcome to the Number Guessing Game!")
print('\n select a range')
print('1️⃣ 1-10')
print('2️⃣ 1-50')
print('3️⃣ 1-100')
print('4️⃣ custom range')

choice = int(input('Enter your choice (1-4): '))

if choice == '1':
    cnum_guess = 10
    print("I'm thinking of a number between 1 to 10")
elif choice == '2':
    cnum_guess = 50
    print("I'm thinking of a number between 1 to 50")
elif choice == '3':
    cnum_guess = 100
    print("I'm thinking of a number between 1 to 100")
elif choice == '4':
    upper_bound = int(input("Enter the range number: "))
    cnum_guess = upper_bound
    print(f"I'm thinking of a number between 1 to {upper_bound}")

num_guess = random.randint(1,cnum_guess)
attempts = 3

while True:
    guess = int(input("Enter your number: "))
    attempts -= 1
    if attempts == 0:
        print("You have no more attempts left. Game over!")
        break

    if guess < num_guess:
        print(f"Too low! Try again.you have {attempts} left")
    elif guess > num_guess:
        print(f"Too high! Try again.you have {attempts} left")
    else:
        print("Congratulations! You've guessed the number!")
        break