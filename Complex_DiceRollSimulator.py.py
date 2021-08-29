# This is a simple dice roll simulator. 

import random

minVal = 1
maxVal = 6

while True:
        print('Enter 1 to roll the dice or Enter 2 to exit the program.')

        user = int(input('Enter your selection now: '))

        if user == 1:
        
                print(random.randint(minVal, maxVal))

        else:
            exit()

