#!/usr/bin/env python
import codejam

def fractile(x):
    k, c, s = map(int, x.split(" "))
    if c==1:
        if s<k: return "IMPOSSIBLE"
        return " ".join(map(str, range(1,k+1)))
        
    if s < k-1: 
        return "IMPOSSIBLE"
        
    if k==1: return "1"
        
    return " ".join(map(str, range(2, k+1)))

if __name__ == "__main__":
    codejam.linebyline("D-large-practice.in", fractile)