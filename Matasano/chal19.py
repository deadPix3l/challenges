#!/usr/bin/env python
import binascii
import base64

import myalgs
import util
########### challenge 19 #############
def rotatestr(data):
    return data[-1] + data[:-1]
    
def easyprint(x, y):
    formatted =  " | ".join([x[i:i+y] for i in range(0, len(x), y)])
    return "".join([i if (31 < ord(i) <127) else ('[%s]' % binascii.hexlify(i)) for i in formatted])
    

print "------19--------"
with open("text/19.txt",'r') as file19:
    encstrs = [myalgs.myCTR(base64.b64decode(line)) for line in file19]

# choose strings
def makeM2():
    (x,y) = map(int, raw_input("please select x^y [0-39]: ").split('^'))[:2]
    print "select: %s ^ %s" % (x, y)
    return util.fixedXor(encstrs[x], encstrs[y])


def guesschars(M2):
    while True:
        guess = raw_input("> ")
        if ord(guess[0])==27: break
        for i in range(len(guess)):
            x = util.fixedXor(M2, guess)
            print "  %s [%s] (%s)" %(easyprint(x, len(guess)), guess, binascii.hexlify(x))
            guess = rotatestr(guess)
        print ""
        
# this loop allows continuous uninterrupted guessing
# and checking all strings for hints and trigrams
while True:
    M2 = makeM2()
    guesschars(M2)

    x = encstrs[int(raw_input("enter index: "))]
    key = raw_input("key: ")
    
    for i in range(len(encstrs)):
        crypted = util.fixedXor(x, encstrs[i])[:min(len(x), len(encstrs[i]))]
        xdecrypt = util.fixedXor(crypted, key)
        print "%d: [%d/%d]:: %s" %(i, len(xdecrypt), len(encstrs[i]), xdecrypt)
        
######################################