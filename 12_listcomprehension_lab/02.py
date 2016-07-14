"""
Find and print all possible sequences
of 3 lowercase characters: aaa, aab, aac, ..., zzz
"""

lower_keys = [chr(lc) for lc in range(255) if (chr(lc)).islower()]
combined = [x+y+z for x in lower_keys for y in lower_keys for z in lower_keys]
print ("combined: "),
for a in combined:
    print "3 letters : %s " % a