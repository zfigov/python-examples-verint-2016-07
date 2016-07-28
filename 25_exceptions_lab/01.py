"""
Write a python program that takes numbers in a loop
and for each number prints its square root
If value is negative or not a number show 
a warning and keep reading values
"""
import math

while 1:
    print ('Enter number')
    inp = raw_input()
    try :
        val = math.sqrt(int(inp))
    except ValueError as e:
            e.message
            print "Invalid input : %s " % e.message
            continue
        
    print 'square root = %d' % val