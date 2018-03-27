import binascii
import base64
import random

### Xor's A and B, using B as a repeating key ##
def fixedXor(a,b):
    x = [chr(ord(a[i]) ^ ord(b[i % len(b)])) for i in range(len(a))];
    return "".join(x);
## calculates Hamming Distance between A and B ##
def editDistance(a,b):
    return sum([bin(ord(i)).count('1') for i in fixedXor(a,b)]);

#################################
## implements PKCS#7 padding  ###
#################################
class PaddingError(Exception):
    pass

def pkcs7(txt, blocksize=16):
    padchar = (blocksize - (len(txt) % blocksize));
    txt += chr(padchar)*padchar
    return txt
    
def unpkcs7(txt, blocksize = 16):
    if not len(txt): return
    padchar = txt[-1]
    if ord(padchar) <= blocksize:
        if txt[-(ord(padchar)):] == padchar*ord(padchar):
            return txt[:-(ord(padchar))]
    raise PaddingError('Bad Padding for PKCS7')
    
#################################
## generates n random bytes   ###
#################################
def randombytes(n = 16):
   randbytes = ''
   for i in range(n):
       randbytes += chr(random.randint(0,255))
   return randbytes


#########################################
## Check if contains repeating blocks ###
## Indicating possible ECB encryption ###
#########################################
def checkECB(ct):
    templist = [ct[i:i+16] for i in range(0,len(ct),16)]
    if len(templist) != len(set(templist)): return True;
    return False;
    
#important globals
randkey = randombytes(16);