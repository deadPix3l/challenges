
#!/usr/bin/env python2
with open("fractiles.in",'r') as f:
	T = int(f.readline()) #testcases
	for i in range(1,T+1):
		k,c,s = map(int,f.readline().split())
		print "Case #{}:".format(i),
		if s==k: # for the small file
			print " ".join(str(k) for k in range(1,s+1))
else: print "shit!"