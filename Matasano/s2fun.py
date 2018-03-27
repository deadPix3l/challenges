#! /usr/bin/env python
import base64
import random
from Crypto.Cipher import AES

import util
import myalgs
###############################
## Checks ECB by looking for ##
## 2 identical ciphertexts   ##
###############################
# didnt i write this already?
# set 1? might just use that one.
def confirmECB(oracle, blocksize=16):
    blankdata = chr(0) *2 *blocksize;
    
    x = oracle(blankdata)
    if x[:blocksize] != x[blocksize:blocksize*2]:
        raise Exception("Not running ECB");
    return True
    
##############################
## Find blocksize of Oracle ## 
## based on return length   ##
##############################
def findBlocksize(oracle):
    base = oracle('')
    i = 1;
    while True:
        new = oracle('X'*i);
        if len(new) > len(base):
            return len(new) - len(base);
        i+=1


#######################################################################
### generates random key and encrypts as either ECB or CBC at random ##
#######################################################################
def encrypt_randomly(data):
    # randomize needed parts
    key = util.randombytes(16);
    iv = util.randombytes(16);
    randstream = util.randombytes(20);
    
    # how much to put before and after data
    n = random.randint(5,10);
    n2 = random.randint(5,10);
    
    #prepend a random count of random chars to each side of data 
    data = randstream[:n] + data + randstream[n:n+n2]
    
    #pad data properly for encryption
    data = util.pkcs7(data)
    
    # random : 1 - ECB, 0 - CBC
    if random.randint(0,1):
        cipher = AES.new(key);
        ciphertext = cipher.encrypt(data);
    else:
        ciphertext = myalgs.myCBC(data, key, iv);
    return ciphertext
    
##############################################################
### generates random key and encrypts ECB with secret data  ##
### to decrypt, pass '-1 blocks' and look at last char      ##
##############################################################
#set one global random key for encrypting
def encryption_oracle(data):
    #add secret and pad for encryption
    data = util.pkcs7(data)
    
    #encrypt and return
    cipher = AES.new(util.randkey, AES.MODE_ECB);
    ciphertext = cipher.encrypt(data);
    return ciphertext
    
randprefix = util.randombytes(random.randint(0,100));
secret = base64.b64decode('Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg\
aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq\
dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg\
YnkK');
#aliases for 12 and 14
def oracle_12(data):
    return encryption_oracle(data+secret)
    
def oracle_14(data):
    return encryption_oracle(randprefix+data+secret)   

##############################################
##### Challenge 12 and 14 Oracle Revealers ###
##############################################
def OracleDict(oracle, decstr, blocksize, off, fb):
    lettermap = {}
    for byte in range(256):
        testdata = 'X'*off
        testdata += decstr[-(blocksize-1):]
        testdata += chr(byte)
        encbyte = oracle(testdata)[fb:fb+blocksize]
        lettermap[encbyte] = chr(byte)
    return lettermap    
    
## add offset support for challenge 14 later
def RevealText(oracle, blocksize, off, fb):
    #We'll remove the A's later. makes things easier
    decstr = 'A' * (blocksize+off);
    fb *=16
    # for each block (which is len of secret text divided by blocksize of 16):
    for idx in range(len(oracle(''))):
        Astr = 'A' * ((blocksize+off-1) - (idx%blocksize))
        idx = (idx/blocksize)*blocksize;
    
        lettermap = OracleDict(oracle, decstr, blocksize, off, fb)
        mytempstr = Astr
        correct = oracle(mytempstr)[fb+idx:fb+idx+blocksize]
        if correct in lettermap: decstr += lettermap[correct]
        else: break;
    
    # fix the 'A' thing,remove padding, and return
    return util.unpkcs7(decstr[blocksize+off:]);

######################################
###     The Profile Functions!      ##
############ challenge 13 ############
######################################
# almost useless really.
def getprofile(email):
    return encryption_oracle(profile_for(email))

def parseprofile(inputstr):
    final = {};
    for each in inputstr.split('&'):
        (key,val) = each.split('=',1);
        final[key] = val    
    return final;

def profile_for(email):
    
    email = email.split('&')[0].replace('=','')
    email = 'email='+email+'&uid='+str(random.randint(1,100))+'&role=user'
    return email
    
def decryptprofile(profile):
    # bad ciphertext, wrong size
    if (len(profile)%16):
        raise Exception('bad Cipher Length: '+str(len(profile))+'('+str(len(profile)%16)+')')
    
    #decrypt, parse, and return
    cipher = AES.new(util.randkey, AES.MODE_ECB);
    parseme = util.unpkcs7(cipher.decrypt(profile))
    return parseprofile(parseme)