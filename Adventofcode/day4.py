#!/usr/bin/env python
import adventapi
from hashlib import md5

x = adventapi.levelInput(4)

i=0
while not md5(x+str(i)).hexdigest().startswith('00000'): i+=1
print "part1:", i
while not md5(x+str(i)).hexdigest().startswith('000000'): i+=1
print  "part2:", i