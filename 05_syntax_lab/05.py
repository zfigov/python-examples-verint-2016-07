"""
Write a program that randomizes integers in a loop
until it finds a number that is divisable by: 7, 13 and 15
"""
# Exercise 5
# By Zvi Figov
from random import randint


while True:
    num = randint(1,1000000)
    if num % 7 ==0 and num % 13 ==0 and num % 15 ==0:
        break
print "Chosen number = %d" % num

