#!/usr/bin/python

from random import randint

def dice_roll(amount, modifier):
    params = map(int, amount.split('d'))
    count = 0
    for i in range(1, params[0] + 1):
        roll = randint(1, params[1])
        count += roll
        print "Roll #{0}: {1}".format(i, roll)
        print "Sum:    ", count
    print "Dice + Modifier:", count + modifier

toss = raw_input('die roll> ')
mod = int(raw_input('modifier> '))

dice_roll(toss, mod)