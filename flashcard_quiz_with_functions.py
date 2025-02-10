import random


def ask_question(question, correct_answer):
    """
    Ask a question and return the user's answer along with the correct answer.
    """

    print("\nQuestion:", question)
    user_answer = input("\nPlease give your answer: ").strip().upper() # Asking for the user input and normalizing it (to uppercase)
        
    return user_answer, correct_answer # Return user's answer and the correct answer


def check_answer(user_answer, correct_answer):
    """
    Compare user_answer with the correct_answer and print the result.
    """
    if user_answer == correct_answer.upper():  # Compare lowercase answers to handle case insensitivity
        print("\nYou answered correctly!")
    else:
        print("\nYour answer was wrong!")


def main():
    """Main function to initialize quiz data"""
    quiz_data = [
        ('What is 2 + 2?', '4'),
        ('What is the color of the sky?', 'blue'),
        ('What is the capital of Finland?', 'Helsinki'),
        ('What is the square root of 16?', '4')
    ]     

    random.shuffle(quiz_data) # Shuffles questions

    # Loop through eachquestions and check answers
    for question, correct_answer in quiz_data:
        user_answer, correct_answer = ask_question(question, correct_answer)  # Get the answer from the user
        check_answer(user_answer, correct_answer)  # Check the answer
        
# Call main function
if __name__ == "__main__":
    main()
