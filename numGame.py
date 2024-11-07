import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    # Define the range for the secret number
    lower_bound = 1
    upper_bound = 100
    
    # Generate a random secret number
    secret_number = random.randint(lower_bound, upper_bound)
    attempts = 0  # Initialize attempt counter

    while True:
        try:
            # Prompt the user for a guess
            guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))
            attempts += 1  # Increment the attempt counter
            
            # Check if the guess is within the valid range
            if guess < lower_bound or guess > upper_bound:
                print(f"Please guess a number within the range {lower_bound} to {upper_bound}.")
                continue
            
            # Compare the guess with the secret number
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                # Correct guess
                print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
                break  # Exit the loop
        except ValueError:
            # Handle non-integer inputs
            print("Please enter a valid integer.")

if __name__ == "__main__":
    number_guessing_game()