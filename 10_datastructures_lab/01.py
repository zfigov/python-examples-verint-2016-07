"""
A file named hosts holds hostnames and IP addresses
in format: hostname=ip
Write a program that reads the file and takes
a list of hostnames in sys.argv
Program should print the IP addresses of the hosts requested
"""
import sys
from itertools import izip

(_,file1) = sys.argv

host_ip = {}
with open(file1) as fin:
    a = [(line.rstrip('\n')).split("=") for line in fin]

for c1 in range(len(a)):
    host_ip[a[c1][0]] = a[c1][1]

print ("Enter username:")
line = raw_input()

if not (host_ip.has_key(line)):
    print "Key not found"
else:
    print "Key found: %s" % host_ip[line]

