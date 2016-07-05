"""
Write a program that reads 10 numbers from
the user and prints the largest one
"""
# Exercise 1
# By Zvi Figov
print "Enter 10 positive numbers" # Assuming positive numbers 
largest = -1
for i in range(1,11):
    print "Enter number %d" % i
    num = int(raw_input())
    largest = max(num,largest)

print "Largest number is %d" % largest

