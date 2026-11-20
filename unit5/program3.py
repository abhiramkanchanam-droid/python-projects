import random

while True:

    print("\n--- DICE SIMULATOR ---")

    choice = input("Press Enter to roll the dice or type 'q' to quit: ")

    if choice.lower() == "q":
        print("Game ended!")
        break

    dice = random.randint(1, 6)

    print("Dice Result:", dice)

    if dice == 6:
        print("Congratulations! You got 6!")