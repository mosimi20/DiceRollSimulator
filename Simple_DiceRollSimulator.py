# This is a simple dice roll simulator. 

import random

minVal = 1
maxVal = 6

rollDice = input('Write start to roll the dice: ')

if rollDice == 'start' or 'Start':
    print(random.randint(minVal, maxVal))

exit()

