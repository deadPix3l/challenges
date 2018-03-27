#!/usr/bin/env python
import base64

import util
import s2fun
import myalgs

###### challenge 9: see util.pkcs7() #######

############## challenge 10 #################
with open('text/10.txt', 'r') as file10:
    ciphertxt = file10.read();
    ciphertxt = base64.b64decode(ciphertxt);
    
    key = 'YELLOW SUBMARINE';
    iv = '\x00' * 16
    decrypted = myalgs.myCBC(ciphertxt,key,iv,0)

print "------10--------"
print decrypted 
##############################################

############## challenge 11 ##############
### see: s1fun.checkECB()               ##
###      s2fun.encrypt_randomly()       ##
###                                     ##
### checkECB(encrypt_randomly(data))    ##
##########################################

############### challenge 12 ############# 
print "------12--------"
#confirm it's ECB and get the blocksize
blocksize = s2fun.findBlocksize(s2fun.oracle_12);
s2fun.confirmECB(s2fun.oracle_12, blocksize);

print s2fun.RevealText(s2fun.oracle_12, blocksize, 0, 0)
############################################

############# challenge 13 #################
print "------13--------"

lastblock = '1234567890'
lastblock += 'admin'
lastblock += chr(11) * 11
emailblocks = s2fun.getprofile('hacks@woo.com')
adminrole = s2fun.getprofile(lastblock)

escalated = emailblocks[:-16] + adminrole[16:32]
print s2fun.decryptprofile(escalated)
###########################################

############# challenge 14 ################
print "------14--------"

#confirm it's ECB and get the blocksize
blocksize = s2fun.findBlocksize(s2fun.oracle_12);
s2fun.confirmECB(s2fun.oracle_12, blocksize);

#loop to determine offset
#send 32 X's
i = 32;
while True:
    doublebreak = False;
    possible = s2fun.oracle_14('X'*i);
    for block in range(len(possible)/blocksize):
        block*=16;
        if possible[block:block+blocksize] == possible[block+blocksize:block+(2*blocksize)]:
            offset = i - 32
            fb = block/16;
            doublebreak = True;
            break;
    if doublebreak: break;
    i+=1;

print "(harder!!) offset: %d\nfirst breakable block: %d\n" %(offset,fb)
print s2fun.RevealText(s2fun.oracle_14, blocksize, offset, fb)

#############################################

############### challenge 15 ################
########### see s2fun.unpkcs7() #############

################ challenge 16 ###############
print "------15--------"
def CBCencryptme(data):
    thestr = "comment1=cooking%20MCs;userdata="
    # kinda hacky, kinda ugly, dont care, moving on.
    thestr +=  "".join(map(lambda x: "\\"+x if x in ["=",";"] else x, data))
    thestr += ";comment2=%20like%20a%20pound%20of%20bacon"
    paddedout = util.pkcs7(thestr)
    return myalgs.myCBC(paddedout, util.randkey, mode=1)

def decryptcheck(ciphertext):
    dectxt = myalgs.myCBC(ciphertext, util.randkey, mode=0)
    return (';admin=true;' in dectxt)

# a filer block to modify/corrupt. and the real data to be changed.
userinput = 'XXX block[2] XXX'
userinput += '9admin<true'
enc = CBCencryptme(userinput)

# enc is a string of ciphertxt
# block[3] is our admin string, block[2] set aside for corruption
# change block[2] (32-48), enc[32:49]
# these changes will ruin block 2, but cascade onto block 3
enc2 = enc[:32] + util.fixedXor(enc[32:39],'\x02\x00\x00\x00\x00\x00\x01') + enc[39:]
print decryptcheck(enc2)