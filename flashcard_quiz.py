import random

quiz_data = [
    ('What is 2 + 2?', '4'),
    ('What is the color of the sky?', 'blue'),
    ('What is the capital of Finland?', 'Helsinki'),
    ('What is the square root of 16?', '4')
]

random.shuffle(quiz_data)

# Ask a question
for question in quiz_data:
    #random.shuffle(question[0])
    print("")
    print("Question:", question[0])
    answer = input("\nPlease give your answer: ").strip().upper() # Ask user for an input
    if answer == question[1].upper():
        print("\nYou answered correctly!")
    else:
        print("\nYour answer was wrong!")
        break
