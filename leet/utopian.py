

def utopian(n):
	h = 1
	if n == 0:
		return 1
	elif n == 1:
		return 2
	elif n>1:
		count = 1
		while(count <= n):
			if count%2 != 0:
				h = 2*h
			elif count%2 == 0:
				h = h + 1
			count = count + 1		
	return h



t = int(raw_input())
arr = []
for i in range(t):
	dude = int(raw_input())
	ans = utopian(dude)
	arr.append(ans)
for k in arr:
	print k
