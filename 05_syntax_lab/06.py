"""
Write a program that randomizes 2 numbers
and calculates their least common multiplier,
that is the smallest number that is divisable
by both.
For example if the numbers were 4 and 6,
program should print 12
"""
# Exercise 6
# By Zvi Figov
from random import randint

num1 = randint(1,10)
num2 = randint(1,10)

m1 = min(num1,num2)
for i in range(m1,num1*num2+1,m1):
    if i % num1 ==0 and i % num2 ==0:
        print "Least common multiplier of %d and %d = %d" % (num1,num2,i)
        break
