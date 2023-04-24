#!python3

'''
Create a number guessing game
There is a limit of 10 guesses
The program will ask the user to enter an integer from 1 to 100
The program will then tell the user if the number is too high, too low or correct.
If the number is correct, the program will end
If the 10 guesses are used up, the program will say that the user has lost
'''

import math
import random
from typing import Any

def game():
    x = random.randint(1,100)
    for i in range(0, 10):
        g = int(input('Enter your guess:\n'))
        if x==g:
            print("Congratulations, your guess was correct!")
            play()
        elif i==9:
            print("No tries remaining, game over")
            play()
        elif i==8:
            if g>x:
                print("Your guess was too high, 1 attempt remaining")
            elif g<x:
                print("Your guess was too low, 1 attempt remaining")
        else:
            if g>x:
                print(f"Your guess was too high, {(10-(i+1))} attempts remaining")
            elif g<x:
                print(f"Your guess was too low, {(10-(i+1))} attempts remaining")



def play():
    y = 0
    y = input("Play again?\n")
    if y!=None:
        game()

print("\nYou have ten tries to guess an integer between and including 1 and 100\n")
game()