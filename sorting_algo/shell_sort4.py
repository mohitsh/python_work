

def shell_sort(alist):
	
	sublist_count = len(alist)
	while sublist_count > 0:
		for startposition in range(sublist_count):
			gapInsertionSort(startposition, alist, sublist_count)
			print 'gap', sublist_count, 'sorted list', alist

		sublist_count = sublist_count-1

def gapInsertionSort(start,alist,gap):
		for index in range(start, len(alist), gap):
			position = index
			location = alist[index]
			
			while position >= gap and alist[position-gap] > location:
				alist[position] = alist[position-gap]	
				position = position - gap
			
			alist[position] = location 

		return alist

alist =  [5, 16, 20, 12, 3, 8, 9, 17, 19, 7]
shell_sort(alist)
	
