"""
Write a program that takes a file name
and prints line count for the file

Alert the user politely if there was any problem opening the file
"""

import sys
import msvcrt

(_,file1) = sys.argv

try :
    num_lines = sum(1 for line in open(file1))
except Exception as e:
    print 'Sorry %s file not found',file1
    c = msvcrt.getch()
    if c:
        sys.exit()
print 'Num lines : ',num_lines