# Hangman
# https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/
import random

guessLimit = 7
wordList = ("bowdoin", "bear", "graduate")

secretWord = wordList[random.randint(0, len(wordList) - 1)]

guesses = []
matchedCount = 0;

# https://stackoverflow.com/questions/6142689/initialising-an-array-of-fixed-size-in-python
secretWordRevealed = ['*'] * len(secretWord)

print("The word I'm thinking of is " + str(len(secretWord)) + " characters long (lowercase).")

while True:
    
    guess = input()
    
    if guess == 'quit':
        break
    
    if guess in guesses:
        print("You already guessed that letter.")
    elif len(guesses) >= guessLimit:
        print("You lose. The secret word was: " + secretWord)
        break
    else:
        index = 0
        # https://stackoverflow.com/questions/3873361/finding-multiple-occurrences-of-a-string-within-a-string-in-python
        while index < len(secretWord):
            index = secretWord.find(guess, index)
            if index == -1:
                break
            else:
                secretWordRevealed[index] = guess
                matchedCount += 1              
            index += 1        
            
        if matchedCount == len(secretWord):
            print("You win! The secret word is " + secretWord + "!")
            break
        
        guesses.append(guess)
    
    print("Guesses: " + str(guesses))
    print("Progress: " + str(secretWordRevealed))
    
    
    