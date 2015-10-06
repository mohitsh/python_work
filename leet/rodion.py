

def rodion(n,t):
	a = [1] + [0]*(n-1)
	b = [9]*n
	#print a
	#print b
	a = [str(x) for x in a]
	b = [str(x) for x in b]
	a1 = "".join(a)
	b1 = "".join(b)
	a1 = int(a1)
	b1 = int(b1)
	print a1
	print b1
	ans = -1
	#dude = []
	for i in range(a1,b1+1):
		if i%10 !=0 and i%t == 0:
			ans = i
			#dude.append(i)	
	return ans
		

print rodion(3,2)
