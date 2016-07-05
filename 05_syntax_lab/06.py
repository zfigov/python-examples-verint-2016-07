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
# brute force 
max_m = num1*num2
# get multipliers of num1
mul1 = ""
for i in range(num1,max_m+1,num1):
    mul1 = mul1 + str(i) + "\n"
# get multipliers of num2
mul2 = ""
for i in range(num2,max_m+1,num2):
    mul2 = mul2 + str(i) + "\n"
# get common multipliers
common_mult = ""
for i in mul1.split():
    for j in mul2.split():
        if i==j:
            common_mult = common_mult + i + "\n"
# get minimum common mult
min_c = 999999
for i in common_mult.split():
    if int(i)<min_c :
        min_c = int(i)
print "Least common multiplier of %d and %d = %d" % (num1,num2,min_c)




