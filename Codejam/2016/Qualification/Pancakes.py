#!/usr/bin/env python
import codejam

def pancake(x):
    x = str(x).strip()
    return x.count('+-')+x.count('-+')+bool(x.endswith('-'))
    

if __name__ == "__main__":
    codejam.linebyline("B-large-practice.in", pancake)