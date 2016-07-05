""" Write a program that selects a random number
and asks the user to guess it.

After each guess print a hint "too large" or "too small" to the user.

Bonus: To make things interesting, the program should cheat once in a white
"""
# Exercise 7
# By Zvi Figov
from random import randint

num = randint(1,100)
found = False
while not found:
    print "Enter guess" 
    guess_num = int(raw_input())
    if num==guess_num:
        print "Well done"
        found = True
    elif guess_num > num:
        print "Too big"
    else:
        print "Too small"

