#!/usr/bin/env python2
import math

def NotPrime(x):
	#return first divisor of x, or 0 if none
	if x%2==0: return 2
	for i in xrange(3,20,2):
		if x%i==0: return i
	return 0

def getDivs(binstr):
	return [NotPrime(int(binstr,base)) for base in range(2,11)]

with open("coinjam-small.in",'r') as f:
	print "Case #1:"
	T = int(f.readline())
	for i in range(T):
		n,j = [int(i) for i in f.readline().split()]
		# n is number of digits
		# j is number to produce

		perms=('1'+bin(i)[2:].zfill(n-2)+'1' for i in xrange(0,2**n,3))

		for k in perms:
			coin = getDivs(k)
			if 0 in coin: continue
			print k," ".join(str(i) for i in coin)
			j-=1
			if not j: break

    Contact GitHub API Training Shop Blog About 

    © 2016 GitHub, Inc. Terms Privacy Security Status Help 

