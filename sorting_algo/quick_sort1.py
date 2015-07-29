def quick_sort(a):
	quickSortHelper(a,0,len(a)-1)

def quickSortHelper(a,first,last):
	if first<last:
		splitPoint = partition(a,first,last)
		
		quickSortHelper(a,first,splitPoint -1)
		quickSortHelper(a,splitPoint+1,last)
		

def partition(a,first,last):
	pivotValue = a[first]
	
	leftmark = first + 1
	rightmark = last

	done = False
	while not done:
		while leftmark <= rightmark and \
			a[leftmark] <= pivotValue:
			leftmark = leftmark + 1

		while rightmark >= leftmark and \
			a[rightmark] >= pivotValue:
			rightmark = rightmark - 1
		
		if rightmark < leftmark:
			done = True
		else:
			tmp = a[leftmark]
			a[leftmark] = a[rightmark]
			a[rightmark] = tmp
	tmp = a[first]
	a[first] = a[rightmark]
	a[rightmark] = a[first]
	
	return rightmark

a = [54,26,93,17,77,31,44,55,20]
print a
quick_sort(a)
print a
