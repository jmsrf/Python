from random import randint

def print_randon_number()

	current_number = 0

	# Print random number between 1 and 10
	current_number = randint(1, 10)
	print("DEBUG: Current number is", current_number)

while True:
    try:
        answer = int(input("Please give a number between 1 - 10: "))
        
        # If answer is in range 1 - 10 check how it compares to current number with the inner if/elif/else block.
        if answer in range (1, 10): 
        	if answer <  current_number:
        		print("Your guess is smaller than the current number. Try again!")   	
        	elif answer >  current_number:
        		print("Your guess is bigger than the current number. Try again!")
        	else:
        		print("You guessed the number right! Great job.")
        		break	
        else:
        	# If input is valid number but outside of 1 - 10, this gets executed
            print("Number is outside of range 1 - 10. Please try again!")
    except ValueError:
    		# If input is not a number this gets executed.
            print("Your input was not a number. Please give a number between 1 - 10:")






	   