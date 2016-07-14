"""
Write a program that finds anagrams in a words file
Program takes a path to a words file, 
reads the file and searches for words with the same letters.
All words with the same letters should be printed together
"""

import sys
from collections import Counter
(_,file1) = sys.argv

lines_file1 = []
words = []

# read all lines
with open(file1,"r") as fin1:
    lines_file1   = fin1.readlines()

# create words list (wthout the endline)
words = [ line.rstrip('\n') for line in lines_file1]

# count the number of letters in each word
words_count = []
for word in words:
    w = Counter(word)
    words_count.append(w)

# compare each word to the other using the counter
found = [False for i in range(len(words))]

for i in range(len(words)):
    for j in range(i+1,len(words)):
        if (words_count[i]==words_count[j]) :
            print "%s  %s" %  (words[i],words[j])
            found[i] = True
            found[j] = True
    if not found[i]:
        print "%s " % (words[i])
            




