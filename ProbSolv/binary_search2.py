

def binary_search(alist,item):
	first = 0
	last = len(alist)-1
	found = False
	
	while first <= last and not found:
		mid = (first+last)/2
		if item == alist[mid]:
			found = True
		else:
			if item > alist[mid]:
				first = mid+1
			elif item < alist[mid]:
				last = mid-1

	return found, mid

alist = [1,4,7,10,15,19,23,28,34,38,45,48,50,54,59]
print binary_search(alist,7)
print binary_search(alist,28)
print binary_search(alist,48)
print binary_search(alist,59)
print binary_search(alist,100)
print binary_search(alist,-10)
