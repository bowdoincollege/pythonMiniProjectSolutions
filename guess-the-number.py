# Guess the Number
# https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/
import random

min = 0
max = 5

theNumber = random.randint(min, max)
guess = -1
correct = False

print("I'm thinking of a whole number between " + str(min) + " and " + str(max) + ". What number am I thinking of? ")

while not correct:
    guessStr = input()
    
    try:
        guess = int(guessStr)
    
        correct = guess == theNumber
        
        if correct:
            print("You are correct!")
        elif guess > theNumber:
            print("Your guess is too high.")
        else:
            print("Your guess is too low.")
        
    except:
        print("That is not a number! Guess again!")    

    
