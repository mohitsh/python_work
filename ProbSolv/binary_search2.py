

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
				first = alist[mid+1]
			elif item < alist[mid]:
				last = alist[mid-1]

	return found, mid

alist = [1,2,3,4,5,6,7,9]
print binary_search(alist,2)
print binary_search(alist,7)
print binary_search(alist,10)
