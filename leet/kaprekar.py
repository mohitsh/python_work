
def kaprekar(n):
	square = n*n
	dude = str(square)
	l = len(dude)
	for i in range(l):
		a = dude[:i]
		if i == 0:
			pass
		else:
			a1 = int(a)
		b = dude[i:]
		b1 = int(b)
		#print "a",a
		#print "b",b1
		if i == 0:
			if b1 >0 and b1 == n:
				return n
		else:
			if a1>0 and b1>0 and a1+b1 == n:
				return n
		

def karp(a,b):
	arr = []
	for i in range(a,b+1):
		arr.append(kaprekar(i))

	return [x for x in arr if x is not None]

a = int(raw_input())
b = int(raw_input())

ans = karp(a,b)
if len(ans) == 0:
	print "INVALID RANGE"
else:
	dude = [str(x) for x in ans]
	print " ".join(dude)

'''
kaprekar(4879)
'''
		
