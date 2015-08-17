

def quicksort(a):
	quicksorthelper(a,0,len(a)-1)
	

def quicksorthelper(a,first,last):
	print 'sorted', a
	if first < last:
		split = partition(a,first,last)
		quicksorthelper(a,first,split-1)
		quicksorthelper(a,split+1,last)

def partition(a,first,last):
	pivot = first
	leftmark = first + 1
	rightmark = last
	done = False
	
	while not done:
		while leftmark <= rightmark and a[leftmark] <= a[pivot]:
			leftmark = leftmark + 1
		while rightmark >= leftmark and a[rightmark] >= a[pivot]:
			rightmark = rightmark - 1
	
		if rightmark < leftmark:
			done = True

		else:
			tmp = a[leftmark]
			a[leftmark] = a[rightmark]
			a[rightmark] = tmp

	tmp = a[first]
	a[first] = a[rightmark]
	a[rightmark] = tmp

	return rightmark


alist = [9,7,6,5,4,3,2,1,0]
print alist
quicksort(alist)
print alist
