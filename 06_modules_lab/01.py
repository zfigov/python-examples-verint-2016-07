""" Write a program that takes a count
from sys.argv import and prints "Hello Python"
count times
"""
import sys

if len(sys.argv)==2:
    times = sys.argv[1]
    for i in range(0,int(times)):
        print "Hello Python"
