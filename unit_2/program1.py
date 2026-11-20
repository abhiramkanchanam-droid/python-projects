
"""Play a number guessing game with a limited number of attempts."""

import random

def main():
    print("\n======= NUMBER GUESSING GAME =======")

    secret_number = random.randint(1, 100)
    max_attempts = 5
    attempts = 0

    print("Guess a number between 1 and 100.")
    print("You have only 5 attempts!")

    while attempts < max_attempts:
        guess = int(input("\nEnter your guess: "))
        attempts += 1

        if guess == secret_number:
            print("\nCongratulations! You guessed correctly.")
            print("Number of attempts:", attempts)
            break

        elif guess < secret_number:
            print("Too low! Try a higher number.")

        else:
            print("Too high! Try a lower number.")

    else:
        print("\nGame Over! You used all attempts.")
        print("The correct number was:", secret_number)

if __name__ == "__main__":
    main()