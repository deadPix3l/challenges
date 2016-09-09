#!/usr/bin/env python
import adventapi

x=adventapi.levelInput(1)
a=0
p2=False
for k,v in enumerate(x):
    if v=='(': a+=1
    elif v==')': a-=1
    if a==-1 and not p2: 
        print "part 2:",k+1
        p2=True
    
print "part 1:", a
    