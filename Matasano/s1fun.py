#!/usr/bin/env python
import util

######################################################
#### scores a string on likelyhood of being english ##
######################################################
def score(dec):
     return sum(freq[i.lower()] for i in dec if i.lower() in freq)
     
###### frequency of characters in english language
###### Used by score() to determine english score
freq = {        
'a' : 0.0651738, 'b' : 0.0124248, 'c' : 0.0217339,
'd' : 0.0349835, 'e' : 0.1041442, 'f' : 0.0197881,
'g' : 0.0158610, 'h' : 0.0492888, 'i' : 0.0558094,
'j' : 0.0009033, 'k' : 0.0050529, 'l' : 0.0331490,
'm' : 0.0202124, 'n' : 0.0564513, 'o' : 0.0596302,
'p' : 0.0137645, 'q' : 0.0008606, 'r' : 0.0497563,
's' : 0.0515760, 't' : 0.0729357, 'u' : 0.0225134,
'v' : 0.0082903, 'w' : 0.0171272, 'x' : 0.0013692,
'y' : 0.0145984, 'z' : 0.0007836, ' ' : 0.1918182
};

###################################################
## breaks a single char Xor against target[str] ###
## returns most likely key. (based on Score)    ###
###################################################
def breakSingleChar(target):
    highscore = 0;
    bestkey = '';
    for i in range(256):
        i = chr(i);
        potential = util.fixedXor(target, i);
        current = score(potential);

        if current > highscore:
            highscore = current;
            bestkey = i;

    return bestkey;

def breakRepeatingChar(keylens, breakme):
    bestscore = 0;
    bestkey = '';

    for k in keylens: #test each keylength. best score wins.

        blocks = [''] * k;
        poskey = '';
        for i in range(k):
            #number of times key repeats is (length of ciphertext)/keylen
            for y in range(len(breakme)/k): blocks[i] += breakme[(k*y)+i];

        #blocks contains blocks all single char encrypted
        for i in blocks:
            poskey += breakSingleChar(i);

        currentscore = score(util.fixedXor(breakme, poskey));
        if currentscore > bestscore:
            bestscore = currentscore;
            bestkey = poskey;
    return bestkey

def findkeylen(breakme):
    #large number to ensure "less than" works
    top3 = [(100000,0)] * 3;
    for keylen in range(2,41):
        #takes first 8 blocks of keylen size each
        samples =[breakme[keylen*i:keylen*(i+1)] for i in range(8)]

        #determine edit distances
        distance = sum([util.editDistance(samples[i],samples[i+1]) for i in range(7)])
        distance /= float(keylen);

        #keep the 3 best keylengths
        if distance < top3[2][0]:
            top3[2] = (distance, keylen);
            top3.sort();

    return [keylen for score,keylen in top3] #gets rid of score. dont need it any more