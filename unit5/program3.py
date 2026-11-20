"""Simulate rolling a dice using the random module."""
import random
def roll_dice():  """Generate a random number between 1 and 6."""
 return random.randint(1, 6)
def main():
    print("===== DICE SIMULATOR =====")
while True:
  input("\nPress Enter to roll the dice...")
    result = roll_dice()
      print("Dice Result:", result)
      choice = input("Do you want to roll again? (yes/no): ")
     if choice.lower() != "yes":
      print("Thank you for playing!")
    break
if __name__ == "__main__":
    main()