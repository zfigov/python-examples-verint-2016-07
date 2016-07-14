"""
Write a function that takes two arguments: 
    A string
    And a number
If wrong types were passed in, raise an exception
"""
from types import *

def func(my_num,my_str):
    if type(my_num) is not IntType  or type(my_str) is not StringType:
        raise Exception("Error type")
    else:
        print "Input ok"

# Test : 
func(12,'ere')

# Test : 
func('23432','ere')

