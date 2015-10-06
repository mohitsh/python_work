
def kaprekar(n):
	if n == 1:
		return 1
	elif n == 9:
		return 9
	elif n==2 or n==3 or n==4 or n== 5 or n== 6 or n==7 or n== 8:
		return None
	square = n*n
	dude = str(square)
	d = len(str(n))
	#print d
	a = dude[:d]
	a1 = int(a)
	b = dude[d:]
	b1 = int(b)
	#print "a",a1
	#print "b",b1
	d1 = len(dude)-d
	m = dude[:d1]
	m1 = int(m)
	p = dude[d1:]
	p1 = int(p)
	#print "m1",m1
	#print "n1",n1
	#print m1+n1	
	if a1>0 and b1 >0:
		if a1+b1 == n or m1+p1 == n:
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
print kaprekar(297)
'''
		
