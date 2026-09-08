import random

def generate_mad_lib(adjective, noun, verb):
    """Return a nonempty story containing all three supplied words."""
    return f"The {adjective} {noun} decided to {verb} through the forest."

def guessing_game():
    """Run an interactive number-guessing game."""
    secret_number = random.randint(1, 100)
    while True:
        guess = int(input("Enter your guess: "))
        if guess == secret_number:
            print("Congratulations! You've guessed the correct number.")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
