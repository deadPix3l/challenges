with open("small-data.in") as f:
	n = int(f.readline())

	for i in range(1,n+1):
		digits = [str(y) for y in range(10)]
		awake=True
		line = int(f.readline())
		if line==0:
			print "Case #{}: INSOMNIA".format(i)
			continue;
		for j in range(1,1000):
			for k in str(line*j):
				try: digits.remove(k)
				except ValueError: pass
	
				if len(digits)==0:
					print "Case #{}: {}".format(i,str(line*j))
					awake=False
					break;
			if(not awake): break
if(awake): print "Case #{}: INSOMNIA".format(i)