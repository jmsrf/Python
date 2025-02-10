from random import randint


def generate_random_number():
    """Generate a random number between 1 - 10."""
    current_number = randint(1, 10)
    print(f"DEBUG: Current number is {current_number}")  # Debugging info
    return current_number # Return generated number


def ask_for_number(current_number): 
    """
    Ask user to give a number between 1 and 10.
    Compares input with current_number and gives feedback until guessed correctly.
    """
    guess_number = 0
    while True:
        guess_number += 1 
        print(f"DEBUG: Amount of guesses {guess_number}")
        try:
            answer = int(input("Please give a number between 1 - 10: "))

            # If the number is in range 1 - 10, compare with current_number
            if 1 <= answer <= 10:
                if answer < current_number:
                    print("Your guess is smaller than the current number. Try again!")      
                elif answer > current_number:
                    print("Your guess is bigger than the current number. Try again!")
                else:
                    print("You guessed the number right! Great job.")
                    break # Exit loop when guessed correctly    
            else:
                # If input is a number but outside the valid range, print error message
                print("Number is outside of range 1 - 10. Please try again!")

        except ValueError:
                # If input is not a number, print error message.
                print("Your input was not a number. Please give a number between 1 - 10:")

        if guess_number >= 3:
            print("Maximum of 3 tries exceeded!")
            break


# Generate a random number and pass it to the function
random_number = generate_random_number() # Store the return value 
ask_for_number(random_number)  # Pass it as an argument

       
