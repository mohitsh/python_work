

	
def shell_sort(alist):
	sublist_count = len(alist)//2
	while sublist_count > 0:
		for startposition in range(sublist_count):
			getInsertionSort(startposition, alist, sublist_count)

		print 'gap', sublist_count, 'list', alist
		sublist_count = sublist_count//2


def getInsertionSort(startposition, alist, gap):
	for index in range(startposition, len(alist), gap):
		position = index
		location = alist[index]
		
		while position >= gap and alist[position-gap] > location:
			alist[position] = alist[position-gap]
			position = position - gap
		
		alist[position] = location

alist =  [5, 16, 20, 12, 3, 8, 9, 17, 19, 7]
shell_sort(alist)
