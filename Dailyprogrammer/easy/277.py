#!/usr/bin/env python

def gcd(a,b):
    i = min(a,b)
    while (a%i or b%i): i-=1
    return i
    
def simplify(a,b):
    x = gcd(a,b)
    return "{}/{}".format(a/x, b/x)
    
    
print simplify(4,8)
print simplify(1536, 78360)
print simplify(51478, 5536)
print simplify(46410, 119340)
print simplify(7673, 4729)
print simplify(4096, 1024)
