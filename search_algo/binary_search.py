
def binary_search(a,val):
	found = False
	last = len(a) - 1
	first = 0
	
	while first <= last and not found:
		midpoint = (first+last)/2
		if a[midpoint] == val:
			found = True
	
		else:
			if val < a[midpoint]:
				last = midpoint - 1
			else:
				first = midpoint + 1
	return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print binary_search(testlist,3)
print binary_search(testlist,13)
print binary_search(testlist,43)
