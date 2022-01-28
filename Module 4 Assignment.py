# Carlos Barona
# Module 4 Assignment

from sys import exit
from random import randint

# Start Here

myData = {} # Setting the variable to an empty dictionary
guesses = 0 # Setting the variable to 0
wins = 0 # Setting the variable to 0

with open('question.txt', 'r') as infile: # Using a context manager to open .txt file as 'infile'
    questions = infile.readlines() # Setting the 'question' variable to 'infile.readlines()'
    for question in questions: # This is a for loop that will iterate through 'questions'
        if 'first' in question: # Conditional will trigger if 'first' is in an iteration from .txt file
            myData['first_name'] = input(question) # Setting the variable to the input interation from .txt file
        elif 'last' in question: # Another conditional that will trigger if 'last' is in an iteration from .txt file
            myData['last_name'] = input(question) # Setting the variable to the input iteration from .txt file
        else: # Conditional that will trigger if none of the others are met.
            print('bad question input file') # A funtion that will display a string message
            exit() # An exit funtion

for play in range(10): # A for loop that will iterate 'play' through a range of 10
    number = randint(0, 100) # Setting the variable 'number' to the randint() function that picks a random number from 0 to 100
    solve = False # Setting the variable to the False Boolean
    while not solve: # A While loop set to continue to run while not the 'solve' variable
        guess = int(input(f'Guess a number from 0 to 100 : ')) # Setting the variable to the input that is turned into an intiger
        guesses += 1 # Updating the variable to increase by 1
        if guess == number: # If the user guessed the correct number this conditional will trigger
            print(f"Great Job {myData['first_name']}, your guess of {guess} is correct!!!") # Print function will diplay a string that is formated with 'myData' and 'guess' variables
            wins += 1 # Updating the variable to increase by 1
            solved = True # Setting the variable to the True Boolean
            break # Breaks out of the iteration
        if guess != number: # If the user guesses wrong this conditonal will be triggered
            print(f'Your guess of {guess} is incorrect!') # Print funtion will display a string formated with 'guess' variable
        if guess > number: # If user guesses to high this conditonal will be triggered
            print(f'Sorry, you guessed too high!!') # Print function will display a string message
        elif guess < number: # If user guesses too lower this conditional will be triggered
            print(f'Sorry, you guessed too low!!') # Print function will display a string message
        else: # Conditional that will trigger if non of the others are met
            pass # Placeholder statement

    if solved: # Will be triggered after user guesses correctly
        print(f'Lets play again, you have completed {wins} out of 10 plays.') # Print a string message formated with 'wins' variable
        continue # Will continue to next iteration in for loop

print(f"{myData['first_name']} {myData['last_name']} guessed the correct number {wins} out of 10 plays.") # Print function will display formated string message
print(f"It took {myData['first_name']} {myData['last_name']} {guesses} guesses to do this!") # Print function will display formated string message
exit() # Function that will exit script