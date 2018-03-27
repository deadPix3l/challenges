#!/usr/bin/env python
import base64
import binascii
import random

import util
import myalgs

########### challenge 17 #############
def CBCoracle():
    with open('text/17.txt','r') as file17:
        lines = [i.rstrip() for i in file17.readlines()]
        
    encryptme = base64.b64decode(lines[random.randrange(10)])
    encryptme = util.pkcs7(encryptme)
    iv = util.randombytes(16)
    cipher = myalgs.myCBC(encryptme, util.randkey, iv, mode=1)
    return (cipher, iv)
    
def CBCcheckpadding(cipher):
    dectxt = myalgs.myCBC(cipher, util.randkey, mode=0)
    try: 
        if(util.unpkcs7(dectxt)): return True
    except util.PaddingError: 
        return False
        

(ciphertext, iv) = CBCoracle()
# chunks ciphertext into blocks
decryptme = [ciphertext[16*i:16*(i+1)] for i in range(len(ciphertext)/16)]
#somewhere to hold the intermediate state
intermediate = ''

for block in decryptme:
    i2 = ''
    for char in range(1,16+1):
        for i in range(256):
            #decrypting block
            forged = '\0'*(16-char)+chr(i)+util.fixedXor(i2, chr(char))
            #print len(forged), char, i
            if(CBCcheckpadding(forged+block)): 
                i2 = util.fixedXor(chr(i), chr(char))+i2 #prepend
                break
    intermediate+=i2

print "------17--------"
print util.unpkcs7(util.fixedXor(intermediate,iv+ciphertext))
######################################

########### challenge 18 #############
print "------18--------"
decryptme =  base64.b64decode("L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ==")
print myalgs.myCTR(decryptme)
######################################
