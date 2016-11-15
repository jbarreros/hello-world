'''
Created on Nov 14, 2016
@author: Jose
'''

import random

def roll(sides=6):
    num_rolled = random.randint(1, sides)
    return num_rolled

def guess():
    sides = 6
    rolling = True
    while rolling == True:
        questi = input("Roll the dice? Enter = Roll and Q = Quit")
        if questi.lower() != "q":
            num_roll = roll(sides)
            print ("You rolled a", num_roll)
        else:
            rolling = False
    print ("Thanks for playing! Hope you had fun!")
    
guess()
