
import random

# Available choices in the game
choices = ["snake", "water", "gun"]

# Display the welcome message
print("=" * 40)
print("   WELCOME TO SNAKE, WATER, GUN GAME")
print("=" * 40)

# Keep playing until the user chooses to quit
while True:

    # Get the player's choice
    user = input(
        "\nChoose snake, water, or gun (or type quit): "
    ).lower().strip()

    # Exit the game
    if user == "quit":
        print("Thanks for playing! Goodbye!")
        break

    # Check whether the choice is valid
    if user not in choices:
        print("Invalid choice! Please choose snake, water, or gun.")
        continue

    # Let the computer select a random choice
    computer = random.choice(choices)

    # Display both choices
    print("\nYour choice:", user)
    print("Computer choice:", computer)

    # Decide the winner
    if user == computer:
        print("Result: It's a draw!")

    elif (
        (user == "snake" and computer == "water")
        or (user == "water" and computer == "gun")
        or (user == "gun" and computer == "snake")
    ):
        print("Result: Congratulations! You win!")

    else:
        print("Result: Computer wins!")

    print("-" * 40)
