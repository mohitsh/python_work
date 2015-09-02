

def binary_search(alist,item):
	mid = len(alist)/2
	if item <= alist[len(alist)-1]:
		if alist[mid] == item:
			return True
		elif alist[mid] > item:
			return binary_search(alist[:mid],item)
		elif alist[mid] < item:
			return binary_search(alist[mid+1:],item)
	else:
		return False


alist = [1,2,3,4,5,6,7,8,9,10]
print binary_search(alist,3)
print binary_search(alist,9)
print binary_search(alist,14)	
