import random

def guess_number_game():
    secret_number = random.randint(1, 100)
    
    # Number of attempts allowed
    max_attempts = 2
    attempts = 0
    
    print("Welcome to the Guess the Number Game!Raozan, Chattogram.")
    print(f"Guess the number between 1 and 100. You have {max_attempts} attempts.👍")

    while attempts <= max_attempts:
        # Get user input for a guess
        guess = int(input("Enter your guess: "))
        
        # Increment the number of attempts
        attempts += 1
        
        if guess == secret_number:
            print(f"Congratulations! You guessed the correct number ({secret_number}) in {attempts} attempts.🤍")
            break
        elif guess < secret_number:
            print("Too low! Try again.😕")
        else:
            print("Too high! Try again.")

    if guess != secret_number:
        print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")

guess_number_game()
