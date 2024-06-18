import random

# Generate a random number between 1 and 100
number_to_guess = random.randint(1, 100)

# Initialize the number of attempts
attempts = 0

while True:
    # Ask the user for their guess
    user_guess = int(input("Guess a number between 1 and 100: "))

    # Increment the number of attempts
    attempts += 1

    # Check if the user's guess is correct
    if user_guess == number_to_guess:
        print(f"Congratulations! You found the number in {attempts} attempts.")
        break
    elif user_guess < number_to_guess:
        print("Your guess is too low. Try again!")
    else:
        print("Your guess is too high. Try again!")