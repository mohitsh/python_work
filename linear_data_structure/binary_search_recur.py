
def binarysearch(alist, item):
	found = False
	first = 0
	last = len(alist) - 1
	
	while not found and first <= last:
		mid = (first+last)/2
		if item == alist[mid]:
			found = True
		else:
			if item < alist[mid]:
				return binarysearch(alist[:mid],item)
			else:
				return binarysearch(alist[mid+1:],item)
	return found

alist = [1,2,3,4,5,6]
item1 = 1
item2 = 4
item3 = 6
item4 = 32

print binarysearch(alist, item1)
print binarysearch(alist, item2)
print binarysearch(alist, item3)
print binarysearch(alist, item4)

                                  
