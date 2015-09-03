
def recur_sum(alist,n):
	if n == 0:
		return 0
	else:
		return alist[n-1] + recur_sum(alist,n-1)

alist = range(1,11)
print recur_sum(alist,5)
