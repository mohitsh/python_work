

def shell_sort(alist):
	
	sublist_count = len(alist)-1
	while sublist_count > 0:
		for startposition in range(sublist_count):
			gapInsertionSort(startposition,alist,sublist_count)
			print 'gap', sublist_count, 'start', startposition, 'list', alist

		sublist_count = sublist_count - 1
	

def gapInsertionSort(startposition, alist, gap):
	
	for index in range(startposition, len(alist), gap):
		position = index
		location = alist[position]
		
		while position >= gap and alist[position-gap] > location:
			alist[position] = alist[position-gap]
			position = position - gap
		
		alist[position] = location
	
	return alist

alist = [54,26,93,17,77,31,44,55,20]
shell_sort(alist)
print alist
