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
        questi = input("Shall we role? enter = roll and q = quit")
        if questi.lower() != "q":
            num_roll = roll(sides)
            print ("you got a ", num_roll)
        else:
            rolling = False
    print ("Hope you had fun!")
    
guess()