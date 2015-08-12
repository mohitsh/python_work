
# normal while loop 
def binary_search(alist, item):
	first = 0
	last = len(alist)-1
	#mid = (first+last)/2
	found = False
	
	while not found and first <= last:
		mid = (first + last)/2
		if item == alist[mid]:
			found = True
		else:
			if item < alist[mid]:
				last = mid-1
			else:
				first = mid + 1
	return found 
print 'normal while loop result --> '
alist = [1,2,3,4,5,6]
item1 = 1
item2 = 4
item3 = 6
item4 = 32

print binary_search(alist, item1)
print binary_search(alist, item2)
print binary_search(alist, item3)
print binary_search(alist, item4)


# recursion binary_tree

def binary_search_rec(alist, item):
	if len(alist) == 0:
		return False
	
	else:
		mid = len(alist)//2
		if item < alist[mid]:
			return binary_search(alist[:mid],item)
		elif item > alist[mid]:
			return binary_search(alist[mid+1:],item)
		elif item == alist[mid]:
			return True

print 'normal recursion loop result --> '
alist = [1,2,3,4,5,6]
item1 = 1
item2 = 4
item3 = 6
item4 = 32

print binary_search_rec(alist, item1)
print binary_search_rec(alist, item2)
print binary_search_rec(alist, item3)
print binary_search_rec(alist, item4)
















