""" Write a program that searches current working directory
for files larger than 1MB. Every time you find such a file print
its name to the user.

- When the program finds a large file. It should ask the user
  a message asking if she wants to delete it, and delete the
  file if requested

- Take threshold and path as command line arguments
"""
import os
import readchar
import sys

correct_input = False
if len(sys.argv)==3:
    current_working_directory = sys.argv[1]
    MinimumSizeInMB = float(sys.argv[2])
    correct_input = True
else: 
    # default folder
    correct_input = False
    program_name = sys.argv[0]
    print " Usage : %s [directory name] [minimum size]" % program_name


if correct_input:
    # size in bytes = 1 MB = 1k * 1k
    sizeInB = MinimumSizeInMB * 1024 * 1024;
    for root,dirs,files in os.walk(current_working_directory):
        for name_f in files:
           fp = os.path.join(root , name_f)            
           stat_info = os.stat(fp)
           if stat_info.st_size> sizeInB:
               print ("Larger than %f MB %s ") % (MinimumSizeInMB,name_f)
               print ("Do you want to erase?  Y/N : %s ") % name_f
               key = readchar.readkey()
               if key=='Y' or key=='y':
                   # erase file
                   os.remove(fp)
                   print ("File %s erased") % name_f
                                                  
