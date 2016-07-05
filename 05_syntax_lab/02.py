"""
Write a Python program that randomizes 7 numbers
and prints their sum total.
If the sum is divisable by 7, also print the word "Boom"
"""
# Exercise 2
# By Zvi Figov
from random import randint

acc = 0
# accumulate numbers from user
for i in range(1,8):
    x = randint(1,100)
    print "Number %d is %d" % (i, x)
    acc = acc + x
print "Accumulated sum = %d" % acc
# test if they divide by 7
if acc % 7 ==0 : print "Boom!"

