#!/usr/bin/env python

#import requests
#x = requests.get("http://adventofcode.com/day/1/input")
#print x.text
from hashlib import md5

x = 'ckczppom'

i=0
while not md5(x+str(i)).hexdigest().startswith('00000'): i+=1
print "part1:", i
while not md5(x+str(i)).hexdigest().startswith('000000'): i+=1
print  "part2:", i