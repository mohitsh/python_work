

def resize(alist,cap,first):
	old = alist
	alist = [None]*cap
	walk = first
	for k in old:
		alist[k] = old[walk]
		walk = (walk+1)%len(old)
	first = 0
	return alist	

alist = [1,2,3,4,5]
print resize(alist,20,0)
