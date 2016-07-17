"""
Write a function that calculates the sum
of the 10th digit from all arguments passed to it
"""


def sum_tens_digit(*numbers):

    val = sum([int(str(n)[-2]) for n in numbers if len(str(n))>1])
    return val

print "Test: sum_tens_digit(1120,220,140) = %d" % sum_tens_digit(1120,220,140)
print "Test: sum_tens_digit(20,1,10) = %d" % sum_tens_digit(20,1,10)
