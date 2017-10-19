#!/usr/bin/python

from random import randint          # Standard Library modules

def dice_roll(amount, modifier):
    # Turn the die roll input into a list of integers.  Element 0 is number of dice to roll, element 1 is the number of faces on the dice.
    params = map(int, amount.split('d'))
    count = 0
    
    # The for loop executes and 'rolls' a die, then adds that result to count, then prints a summary of what happened
    for i in range(1, params[0] + 1):
        roll = randint(1, params[1])
        count += roll
        print "Roll #{0}: {1}".format(i, roll)
        print "Sum:    ", count
    print "Dice + Modifier:", count + modifier

toss = raw_input('die roll> ').lower()
mod = int(raw_input('modifier> '))

dice_roll(toss, mod)