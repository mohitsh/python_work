

def func(n,alist):
	
	for i in range(n):
		if sum(alist[:i]) == sum(alist[i+1:]):
			return "YES"
	else:
		return "NO"
	


t = int(raw_input())
for i in range(t):
	n = int(raw_input())
	a = raw_input().split()
	alist = [int(x) for x in a]
	print func(n,alist)
	
