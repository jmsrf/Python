'''Prints factorial of number given as input by user'''
def factorial(user_input):
   factorial = 1
  
   for i in range(1, user_input):
      factorial *= i
   return factorial
   
# Check that user input is correct as only positive integers are allowed.   
while True:
    try:
        user_input = int(input("\nPlease give a non-negative integer: ")) 
        if user_input < 0:
            print("\nNegative integers are prohibited! Please try again.")
        else:
            break  # Valid input, exit the loop
    except ValueError:
        print("\nNot a number! Please enter a valid integer.")

print(f"\nFactorial of {user_input} is {factorial(user_input)}")
