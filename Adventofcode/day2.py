#!/usr/bin/env python
import adventapi
y= adventapi.levelInput(2).split('\n')[:-1]
x = [[int(j) for j in i.split('x')] for i in y]

def prod(x):
    y = 1
    for i in x: y*=i
    return y
<<<<<<< HEAD
    
=======

>>>>>>> 02f7717a8e75915717f4575d35cfc5c982ee5566
def sides(x): return [prod(x)/i for i in x]

    
# the solve!
print "part1:", sum(min(sides(i))+2*sum(sides(i)) for i in x)
print "part2:", sum(2*(sum(i)-max(i))+prod(i) for i in x)