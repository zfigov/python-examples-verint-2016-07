""" Write a program that reads 2 numbers from sys.argv
and prints their sum.
"""
import sys

if len(sys.argv)==3:
    num1 = sys.argv[1]
    num2 = sys.argv[2]
    print "Sum of %s + %s = %d" % (num1,num2,int(num1)+int(num2))


