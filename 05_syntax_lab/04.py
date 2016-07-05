"""
Write a program that reads lines from the user
until an empty line is inserted.
After the user typed in an empty line,
print all previously inserted lines in reverse
order (from last to first)
"""
# Exercise 4
# By Zvi Figov



total_lines = ""
print "Enter text, empty line to stop"

line = raw_input()
while len(line)>0:
    print "Input line %s" % line
    total_lines = line + "\n" + total_lines
    line = raw_input()

print "Lines reversed: \n%s" % total_lines

