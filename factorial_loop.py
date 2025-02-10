def factorial(user_input):
    """Calculates the factorial of a given non-negative integer."""
    factorial = 1  # Fix indentation here

    for i in range(1, user_input + 1):  # Include user_input itself in range
        factorial *= i
    return factorial

   
# Check that user input is correct as only non-negative integers are allowed. 
while True:
    try:
        user_input = int(input("\nPlease give a non-negative integer: ")) 
        if user_input < 0:
            print("\nNegative integers are prohibited! Please try again.")
        else:
            break  # Valid input, exit the loop
    except ValueError:
        print("\nNot a number! Please enter a valid integer.")

# Print the result
print(f"\nFactorial of {user_input} is {factorial(user_input)}")
