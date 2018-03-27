#!/usr/bin/env python
import base64
import binascii
from Crypto.Cipher import AES

import s1fun
from util import (fixedXor,editDistance,checkECB)

############# challenge 1 ####################
c1expect = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t";
thestr = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d";
if base64.b64encode(binascii.unhexlify(thestr)) == c1expect:
    print "1: pass!";
else:
    print "1: fail!";
    raise Exception(base64.b64encode(binascii.unhexlify(thestr)) + " is incorrect");
###############################################    
    
############# challenge 2 ###################
thestr = "1c0111001f010100061a024b53535009181c";
thekey = "686974207468652062756c6c277320657965";
c2expect = "746865206b696420646f6e277420706c6179";

thestr = binascii.unhexlify(thestr);
thekey = binascii.unhexlify(thekey);
if fixedXor(thestr, thekey) == binascii.unhexlify(c2expect):
    print "2: pass!";
else:
    print "2: fail!";
    raise Exception(binascii.hexlify(fixedXor(thestr, thekey)) + " is wrong!");
############################################### 

############## challenge 3 ################
thestr = binascii.unhexlify("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736");
key = s1fun.breakSingleChar(thestr);
print "3: " + fixedXor(thestr, key);
########################################### 

############# challenge 4 #################
highscore = 0;
bestkey = '';
besthex = "";
with open("text/4.txt", 'r') as detect:
    for line in detect:
        line = line.rstrip();
        line = binascii.unhexlify(line);
        key = s1fun.breakSingleChar(line);
        linescore = s1fun.score(fixedXor(line, key));
        
        if linescore > highscore:
            highscore = linescore;
            bestkey = key;
            besthex = binascii.hexlify(line);
print "4: " + fixedXor(binascii.unhexlify(besthex), bestkey);
############################################

############# challenge 5 ##################
thestr = '''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal''';
thekey = 'ICE';

c5expect = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a\
26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
if binascii.hexlify(fixedXor(thestr, thekey)) == c5expect:
    print "5: pass!";
else:
    print "5: fail!";
    raise Exception(binascii.hexlify(fixedXor(thestr, thekey)) + " is not right!");
###############################################

############# challenge 6 ##################
with open("text/6.txt", 'r') as b64crypted:  
    breakme = b64crypted.read();         
    breakme = base64.b64decode(breakme); 

top3 = s1fun.findkeylen(breakme)
print "6: key:", s1fun.breakRepeatingChar(top3, breakme);
#commented out because the output is long
#print fixedXor(breakme, bestkey);
##################################################

################ challenge 7 #####################
with open('text/7.txt', 'r') as file7:
    ciphertext = file7.read();
    ciphertext = base64.b64decode(ciphertext);
    key = b'YELLOW SUBMARINE';
    cipher = AES.new(key, AES.MODE_ECB);
    
    dectxt = cipher.decrypt(ciphertext);
    #output is long. uncomment to see.
    #print dectxt;
    
    #condensed output. if first 16 bytes are right
    #then theoretically, its all right
    if dectxt[:16] == "I'm back and I'm":
        print "7: pass!";
    else:
        print "7: fail!";
###################################################

################ challenge 8 ######################
print '8:',
linenum = 0;
with open('text/8.txt', 'r') as file8:
    for line in file8:
        linenum +=1;
        ct = binascii.unhexlify(line.rstrip('\r\n'))
        
        if checkECB(ct):
            print linenum,'contains repeated blocks'
###################################################

# EOF - Set 1 Complete