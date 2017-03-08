#!/usr/bin/env python
import codejam
import collections

def missingcol(f):
    N = int(f.readline())
    allnums = []
    for col in range((2*N)-1):
        allnums += map(int, f.readline().split())
    
    Count = [k for k,v in collections.Counter(allnums).iteritems() if v % 2]
    Count.sort()
    return " ".join(map(str, Count))

if __name__ == "__main__":
    with open("B-large-practice.in", 'r') as f:
        T = int(f.readline())
        for case in range(T):
            print "Case #{}: {}".format(case+1, missingcol(f))