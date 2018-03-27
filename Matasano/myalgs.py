#! /usr/bin/env python
import struct
from Crypto.Cipher import AES

import util
##########################################################
## PURPOSE: To implement algorithms and Cryptographic  ###
##          functions in one central location.         ###
##                                                     ###
## this file contains implementations of:              ###
##     - CBC Mode                                      ###
##     - CTR Mode                                      ###
##     - MT19937 RNG                                   ###        
##     - Diffie-Hellman                                ###
##     - RSA                                           ###
##########################################################

###########################################
##          CBC Mode - AES              ###
###########################################

def myCBC(txt, key, iv='\x00'*16, mode=1):

    blocks = [txt[i:i+16] for i in range(0,len(txt),16)]
    if len(blocks[-1]) != 16:
        print 'last block isn\'t padded properly'
        return False
        
    cipher = AES.new(key);
    
    result = []
    lastcipher = iv;
    for idx, val in enumerate(blocks):
        
        if mode: #encrypt
            lastcipher = cipher.encrypt(util.fixedXor(val, lastcipher))
            result += lastcipher

        else: #decrypt
            result += util.fixedXor(cipher.decrypt(val), lastcipher)
            lastcipher = val;
    return ''.join(result)
###########################################   

###########################################
##          CTR Mode - AES              ###
###########################################
def myCTR(data):
    cipher = AES.new("YELLOW SUBMARINE");
    s = struct.Struct("< 8s Q") # Q = unsigned long long (8 bytes)
    nonce = '\0'*8
    keystream = ''
    #get blockcount
    blockcount = (len(data)/16)
    
    #generate keystream
    for i in range(blockcount+1): 
        keystream+=cipher.encrypt(s.pack(nonce, i))
    return util.fixedXor(data, keystream)
##########################################