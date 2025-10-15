"""
Program 3: Number Guessing Game
Practice: import random and from module import * (with careful use)
This program demonstrates the random module for game development.
"""

import random
from statistics import mean, median, mode  # Selective import instead of *

class NumberGuessingGame:
    def __init__(self, min_num=1, max_num=100):
        """Initialize the game with a random number"""
        self.min_num = min_num
        self.max_num = max_num
        self.secret_number = random.randint(min_num, max_num)
        self.attempts = []
        self.max_attempts = 10

    def play(self):
        """Main game loop"""
        print(f"I'm thinking of a number between {self.min_num} and {self.max_num}")
        print(f"You have {self.max_attempts} attempts to guess it!\n")

        for attempt in range(1, self.max_attempts + 1):
            try:
                guess = int(input(f"Attempt {attempt}: Enter your guess: "))

                if guess < self.min_num or guess > self.max_num:
                    print(f"Please enter a number between {self.min_num} and {self.max_num}")
                    continue

                self.attempts.append(guess)

                if guess == self.secret_number:
                    print(f"\nCongratulations! You guessed the number {self.secret_number} in {attempt} attempts!")
                    return True
                elif guess < self.secret_number:
                    print("Too low! Try higher.")
                else:
                    print("Too high! Try lower.")

            except ValueError:
                print("Please enter a valid number!")

        print(f"\nSorry! The number was {self.secret_number}")
        return False

    def show_statistics(self):
        """Display game statistics"""
        if self.attempts:
            print("\nGame Statistics:")
            print(f"  Attempts made: {len(self.attempts)}")
            print(f"  Guesses: {self.attempts}")
            print(f"  Average guess: {mean(self.attempts):.1f}")
            print(f"  Median guess: {median(self.attempts):.1f}")
            if len(self.attempts) >= 2:
                try:
                    print(f"  Most common guess: {mode(self.attempts)}")
                except:
                    print("  No repeated guesses")

def dice_roller():
    """Simulate rolling dice"""
    print("\n=== Dice Roller ===")
    num_dice = 2
    dice_results = [random.randint(1, 6) for _ in range(num_dice)]
    print(f"Rolling {num_dice} dice: {dice_results}")
    print(f"Total: {sum(dice_results)}")

def lottery_numbers():
    """Generate lottery numbers"""
    print("\n=== Lottery Number Generator ===")
    # Generate 6 unique numbers between 1 and 49
    numbers = random.sample(range(1, 50), 6)
    numbers.sort()
    print(f"Your lottery numbers: {numbers}")
    # Bonus ball
    bonus = random.randint(1, 10)
    print(f"Bonus ball: {bonus}")

def password_generator(length=12):
    """Generate a random password"""
    print("\n=== Password Generator ===")
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    password = ''.join(random.choice(characters) for _ in range(length))
    print(f"Generated password ({length} chars): {password}")

def coin_flip_simulation(flips=100):
    """Simulate coin flips"""
    print(f"\n=== Coin Flip Simulation ({flips} flips) ===")
    results = [random.choice(['Heads', 'Tails']) for _ in range(flips)]
    heads_count = results.count('Heads')
    tails_count = results.count('Tails')
    print(f"Heads: {heads_count} ({heads_count/flips*100:.1f}%)")
    print(f"Tails: {tails_count} ({tails_count/flips*100:.1f}%)")

def main():
    print("=== Random Module Practice ===\n")

    # Set seed for reproducible results (optional)
    # random.seed(42)

    while True:
        print("\nChoose an option:")
        print("1. Play Number Guessing Game")
        print("2. Roll Dice")
        print("3. Generate Lottery Numbers")
        print("4. Generate Password")
        print("5. Simulate Coin Flips")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")

        if choice == '1':
            game = NumberGuessingGame()
            game.play()
            game.show_statistics()
        elif choice == '2':
            dice_roller()
        elif choice == '3':
            lottery_numbers()
        elif choice == '4':
            password_generator()
        elif choice == '5':
            coin_flip_simulation()
        elif choice == '6':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()