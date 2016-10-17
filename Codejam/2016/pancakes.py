def countchanges(x):
	count=0
	lc = ''
	for i in x:
		if i!=lc: count+=1
		lc=i
	return count

with open("pancakes.in",'r') as f:
	T = int(f.readline()) #tetcases
	for i in range(1,T+1):
		stack = list(f.readline().rstrip())
		count = (stack[-1]=='-')
		count+=countchanges(stack)-1
		#print count, stack
		print "Case #{}: {}".format(i,count)
