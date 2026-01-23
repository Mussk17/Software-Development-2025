import random


def generate_secret_number(min_num=1, max_num=100):
    """Generate a random secret number within the specified range."""
    return random.randint(min_num, max_num)


def get_user_guess(attempt, max_attempts):
    """Prompt the user for a guess and validate the input."""
    while True:
        try:
            guess = int(input(f"Attempt {attempt}/{max_attempts} - Enter your guess: "))
            return guess
        except ValueError:
            print("Invalid input! Please enter a number.")


def check_guess(guess, secret_number):
    """Compare the user's guess with the secret number and return feedback."""
    if guess < secret_number:
        return "too_low"
    elif guess > secret_number:
        return "too_high"
    else:
        return "correct"


def provide_feedback(result, guess, secret_number):
    """Provide feedback to the user based on their guess."""
    if result == "too_low":
        print(f"Too low! The secret number is higher than {guess}.")
    elif result == "too_high":
        print(f"Too high! The secret number is lower than {guess}.")
    else:
        print(f"🎉 Congratulations! You guessed it! The number was {secret_number}.")


def play_game(min_num=1, max_num=100, max_attempts=7):
    """Main game function that runs the guess the number game loop."""
    secret_number = generate_secret_number(min_num, max_num)
    attempts = 0
    
    print(f"\n🎮 Welcome to Guess the Number!")
    print(f"I'm thinking of a number between {min_num} and {max_num}.")
    print(f"You have {max_attempts} attempts to guess it. Good luck!\n")
    
    # Main game loop - repeats until correct guess or max attempts reached
    while attempts < max_attempts:
        attempts += 1
        guess = get_user_guess(attempts, max_attempts)
        result = check_guess(guess, secret_number)
        provide_feedback(result, guess, secret_number)
        
        # Exit loop if guess is correct
        if result == "correct":
            print(f"You won in {attempts} attempt(s)!")
            return True
    
    # If loop ends without correct guess, player loses
    print(f"\n😔 Game Over! You've used all {max_attempts} attempts.")
    print(f"The secret number was {secret_number}.")
    return False


def display_repetition_examples():
    """Display examples of everyday repetition scenarios that use loops."""
    examples = [
        "1. Brushing teeth - Repeat brushing motion until teeth are clean",
        "2. Checking email - Keep checking inbox until all messages are read",
        "3. Washing dishes - Repeat washing each dish until all are clean",
        "4. Studying flashcards - Go through cards repeatedly until memorized",
        "5. Searching for keys - Keep looking in different places until found",
        "6. Reading a book - Turn pages repeatedly until book is finished",
        "7. Exercising - Repeat sets of exercises until workout is complete",
        "8. Cooking - Stir food repeatedly until it's ready",
    ]
    
    print("\n📋 Examples of Everyday Repetition (Loop Scenarios):")
    print("=" * 60)
    for example in examples:
        print(example)
    print("=" * 60)
    print("\nThese scenarios all involve repeating an action until a condition is met,")
    print("which is exactly what loops do in programming!\n")

