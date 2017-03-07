#!/usr/bin/env python
import codejam

def sheep(N):
    N = int(N)
    if N==0: return "INSOMNIA"
    
    i = 0
    y = set()
    while len(y)<10:
        i += 1;
        for char in str(N*i):
            y.add(char)
            
    return N*i

if __name__ == "__main__":
    codejam.linebyline("A-large-practice.in", sheep)