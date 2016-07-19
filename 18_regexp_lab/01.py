"""
Write a program that reads data
from property files.
Each line in the file can either be:
    An empty line
    A comment line (Start with #)
    A property line (of the form key = value)

Write a program that takes a property file name and key
as command line arguments and prints the requested value
"""

import sys
import re

(_,file1,key) = sys.argv


lines_file1 = []

with open(file1,"r") as fin1:
    for line in fin1:
        res = re.search(r'\b%s' % key,line)    
        if res is not None:
            (a,b) =  ((line[res.start()+len(key):]).split('='))
            print b.strip(' \n')       
