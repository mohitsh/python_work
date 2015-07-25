
def binary_search(a,value):
	found = False
	first = 0 
	last = len(a)-1

	while first<=last and not found:
		midpoint = (first+last)/2
		print 'comparison ==> ', a[midpoint]
		if a[midpoint] == value:
			found = True
		else:
			if a[midpoint] > value:
				last = midpoint - 1
			else:
				first = midpoint + 1
	return found

'''a = [0, 1, 2, 8, 13, 17, 19, 32, 42, 100]
print binary_search(a,8)
print binary_search(a,100)
print binary_search(a,32)
print binary_search(a,'mohit')
'''
alist = [3, 5, 6, 8, 11, 12, 14, 15, 17, 18]
print binary_search(alist,8)
print binary_search(alist,16)

