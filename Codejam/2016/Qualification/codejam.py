#!/usr/bin/env python

def linebyline(inputfile, func):
    with open(inputfile, 'r') as f:
        numcases = int(f.readline())
        for i in range(numcases):
            print "Case #{}: {}".format(i+1, func(f.readline()))