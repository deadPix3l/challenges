#!/usr/bin/env python
import codejam

def lastword(x):
    x = x.strip()
    word = x[0]
    for i in x[1:]:
        if i < word[0]: 
            word = word+i
        else:
            word = i+word
    return word

if __name__ == "__main__":
    codejam.linebyline("A-large-practice.in", lastword)