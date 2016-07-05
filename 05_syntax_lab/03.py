"""
Write a program that randomizes a number
and prints the sum total of its digits.
For example if the number was: 2345
The result should be: 14
"""
# Exercise 3
# By Zvi Figov
from random import randint

num = randint(1,10000)
numstr = str(num)
acc = 0
for n in numstr:
    acc = acc + int(n)
print "The sum of the digits of the number %d is %d" % (num,acc)


