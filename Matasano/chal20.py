#!/usr/bin/env python
import base64

import util
import myalgs
import s1fun


########### challenge 20 #############
print "------20--------"
with open("text/20.txt",'r') as file20:
    encstrs = [myalgs.myCTR(base64.b64decode(line)) for line in file20]

# take the first n bytes (n being the shortest string length)
# create repeating key xor by concatination
# break them.
n = min([len(x) for x in encstrs])
nmax = max([len(x) for x in encstrs])
breakme = "".join([x[:n] for x in encstrs])
key = s1fun.breakRepeatingChar([n], breakme)

# this loop is intended to break the rest, 10chars at a time.
# as the count gets higher, available samples decreases.
# thus, some bytes may be incorrect, especially nearer the end.
# the next block will fix these errors.
while n < nmax:
    m = n+10
    next10char = "".join([i[n:m] for i in encstrs if len(i)>=m])
    key += s1fun.breakRepeatingChar([10], next10char)
    n=m #move start of next iteration to end of this one

#corrections time. a few bytes were scored incorrectly. i guess.
key = 'v'+key[1:94]+"!:\xf7"+key[97:99]+ '\x28\xcf\x43\xfa'+key[103:]

#the printing part
for i in encstrs:
    print "[%d/%d]" %(len(key),len(i)),
    print util.fixedXor(i, key)[:len(key)]
    
#its still not perfect.
#a few sentences are incomplete
#but the rest could be done through substitution
#im satisfied, so im moving on.     
######################################