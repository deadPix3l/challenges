#!/usr/bin/env python
import adventapi
import re
def naughtyornice2(x): return (re.search('(..).*\\1',x)!=None and re.search('(.).\\1',x)!=None)
def naughtyornice1(x):
    for i in ['ab', 'cd', 'pq','xy']:
        if i in x: return 0
        
    if sum(x.count(i) for i in 'aeiou')<3: return 0
    for i in range(1,len(x)):
        if x[i]==x[i-1]: return 1
    return 0

x = adventapi.levelInput(5).split('\n')
print "part1:", sum(naughtyornice1(i) for i in x)
print "part2:", sum(naughtyornice2(i) for i in x)