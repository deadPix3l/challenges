#!/usr/bin/env python

def reverseFactorial(n):
    i = 1;
    while (int(n)/i) > 1: 
        n = (int(n)/i);
        i+=1;
    if n%i: return None
    return i
    
print reverseFactorial(3628800)
print reverseFactorial(479001600)
print reverseFactorial(6)
print reverseFactorial(18)
