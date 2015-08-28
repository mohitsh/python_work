

def quicksort(alist):
	quicksort_helper(alist,0,len(alist)-1)

def quicksort_helper(alist,first,last):
	#print 'sorted', alist
	if first < last:
		split = partition(alist,first,last)
		print ' '.join(str(x) for x in alist)
		quicksort_helper(alist,first,split-1)
		quicksort_helper(alist,split+1,last)
	
def partition(alist,first,last):
	#print 'after partition', alist
	pivot = last
	leftmark = first 
	rightmark = last-1
	done = False
	
	while not done:
		while leftmark <= rightmark and alist[leftmark] <= alist[pivot]:
			leftmark = leftmark + 1
		while leftmark <= rightmark and alist[rightmark] >= alist[pivot]:
			rightmark = rightmark - 1
		if rightmark < leftmark:
			done = True
		
		else:
			tmp = alist[rightmark]
			alist[rightmark] = alist[leftmark]
			alist[leftmark] = tmp
	
	tmp = alist[leftmark]
	alist[leftmark] = alist[last]
	alist[last] = tmp
	
	return leftmark

#alist = [1, 3, 9, 8, 2, 7, 5]
#quicksort(alist)


n = int(raw_input())
arr = []
a = raw_input().split()
a = [int(x) for x in a]
quicksort(a)	
