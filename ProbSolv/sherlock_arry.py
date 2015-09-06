

def func(n,alist):
	
	for i in range(n):
		if sum(alist[:i]) == sum(alist[i+1:]):
			return "YES"
	else:
		return "NO"

def func2(n,alist):
	mid = n//2
	sum_left = sum(alist[:mid])
	sum_right = sum(alist[mid+1:])
	if sum_left > sum_right:
		return func2(,alist[
	


t = int(raw_input())
for i in range(t):
	n = int(raw_input())
	a = raw_input().split()
	alist = [int(x) for x in a]
	print func2(n,alist)
	
