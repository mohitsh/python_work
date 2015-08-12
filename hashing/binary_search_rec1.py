
def binarysearch(alist, item):
	if len(alist) == 0:
		return False
	
	else:
		mid = len(alist)/2
		if item == alist[mid]:
			return True
		elif item < alist[mid]:
			return binarysearch(alist[:mid],item)
		elif item > alist[mid]:
			return binarysearch(alist[mid+1:], item)

	
alist = [1,2,3,4,5,6]
item1 = 1
item2 = 2
item3 = 3
item4 = 31

print binarysearch(alist, item1)
print binarysearch(alist, item2)
print binarysearch(alist, item3)
print binarysearch(alist, item4)
