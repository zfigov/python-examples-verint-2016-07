"""
Write a program that randomizes integers in a loop
until it finds a number that is divisable by: 7, 13 and 15
"""
# Exercise 5
# By Zvi Figov
from random import randint

flag_done = False

while not flag_done:
    num = randint(1,1000000)
    if num % 7 ==0 and num % 13 ==0 and num % 15 ==0:
        flag_done = True
print "Chosen number = %d" % num

