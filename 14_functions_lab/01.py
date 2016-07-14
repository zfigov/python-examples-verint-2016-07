"""
Write 2 functions:
    mysum - returns the sum of its input arguments
    mymul - returns the multiplication of its input arguments
    Ignore non-numeric arguments
"""
import operator 

def mysum(*paramsin):
    res = 0
    res = sum([int(val) for val in paramsin if type(val) is int])
    
    return res

def mymul(*paramsin):   
    if len(paramsin)>0:
        res = reduce(operator.mul,[int(val) for val in paramsin if type(val) is int])
    else:
        res = 1

    return res

# returns 60
print "Test - mysum(10,20,30) = %d" % mysum(10,20,30)

# returns 30
print "Test - mysum(10,'foo',20) = %d" % mysum(10,'foo',20)

# returns 1
print "Test - mymul() = %d" % mymul() 

# returns 200
print "Test - mymul('foo','bar',10,20) = %d" % mymul('foo','bar',10,20) 