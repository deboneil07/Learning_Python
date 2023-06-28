#program to create a random dice generator

import random as ran

#first_end = ran.randint(0, 7)
#second_end = ran.randint(0,7)

#dice = (first_end, second_end)
#print(dice)

#OOP METHOD

class Dice:
    def roll(self):
        first = ran.randint(1,6)
        second = ran.randint(1,6)
        return first, second
    
dice = Dice()
print(dice.roll())
