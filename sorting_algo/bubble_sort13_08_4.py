

def bubble_sort(alist):
	
	for numpass in range(len(alist)-1,0,-1):
		for i in range(numpass):
			if alist[i] > alist[i+1]:
				temp = alist[i]
				alist[i] = alist[i+1]
				alist[i+1] = temp
	return alist

alist = [3434,2432,46546,24,3245,234,132,234,132,3455,464,567]
print 'list', alist
print 'sorted list', bubble_sort(alist)
