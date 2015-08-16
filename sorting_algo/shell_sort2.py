

def shell_sort(alist):
	
	sublist_count = len(alist)//2
	while sublist_count > 0:
		for startposition in range(sublist_count):
			gapInsertionSort(alist,startposition,sublist_count)
		print 'sublist_count', sublist_count, 'list', alist
		sublist_count = sublist_count//2

def gapInsertionSort(alist,startposition,gap):
	
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

