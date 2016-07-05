"""
Write a program that reads 10 numbers from
the user and prints the largest one
"""
# Exercise 1
# By Zvi Figov
import sys

print "Enter 10 numbers" 
largest = -1
for i in range(1,11):
    txtstr =  "Enter number %d : " % i
    sys.stdout.write(txtstr)
    num = int(raw_input())
    largest = max(num,largest)

print "Largest number is %d" % largest

