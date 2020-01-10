# Dice Rolling Simulator
# https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/
import random

done = 'y'

while True:
    print(random.randint(1,6))
    print('Would you like to roll again? (y/n): ')
    done = input()
    if done == 'n':
        break

