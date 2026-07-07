"""
Guessing Game - A fun number guessing game!
The player tries to guess a random number between 1 and 100.
"""

import random


def get_secret_number():
    """Generate a random secret number between 1 and 100."""
    return random.randint(1, 100)


def get_valid_guess():
    """Get a valid number guess from the user."""
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("❌ Please enter a number between 1 and 100.")
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")


def play_game():
    """Play a single round of the guessing game."""
    secret_number = get_secret_number()
    attempts = 0
    max_attempts = 10
    
    print("\n🎮 Welcome to the Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.\n")
    
    while attempts < max_attempts:
        guess = get_valid_guess()
        attempts += 1
        
        if guess == secret_number:
            print(f"\n🎉 Congratulations! You guessed it in {attempts} attempt(s)!")
            print(f"The secret number was: {secret_number}")
            return True
        elif guess < secret_number:
            remaining = max_attempts - attempts
            print(f"📈 Too low! Try a higher number. ({remaining} attempts left)")
        else:
            remaining = max_attempts - attempts
            print(f"📉 Too high! Try a lower number. ({remaining} attempts left)")
    
    print(f"\n😢 Game Over! You didn't guess the number.")
    print(f"The secret number was: {secret_number}")
    return False


def main():
    """Main function to run the game."""
    while True:
        play_game()
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower().strip()
        if play_again not in ['yes', 'y']:
            print("\n👋 Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()
