


def binary_search(alist,item):
	found = False
	first = 0
	last = len(alist)-1
	mid = (first+last)/2
	while not found and first <= last:
		mid = (first+last)/2
		if item == alist[mid]:
			found = True
		elif item > alist[mid]:
			first = mid + 1
		elif item < alist[mid]:
			last = mid - 1
	return found


alist = [1,2,3,4,5,6]
item1 = 1
item2 = 4
item3 = 6
item4 = 32

print binary_search(alist, item1)
print binary_search(alist, item2)
print binary_search(alist, item3)
print binary_search(alist, item4)
