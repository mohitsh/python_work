
arr = []
def quicksort(alist):
	return quicksort_helper(alist,0,len(alist)-1)
def quicksort_helper(alist,first,last):
	
	if first < last:
		split = partition(alist,first,last)
		arr.append(split)
		quicksort_helper(alist,first,split-1)
		quicksort_helper(alist,split+1,last)
	return arr
	
def partition(alist,first,last):
	pivot = first
	leftmark = first+1
	rightmark = last
	done = False	

	while leftmark <= rightmark and alist[leftmark] <= alist[pivot]:
		leftmark = leftmark + 1
	while rightmark >= leftmark and alist[rightmark] >= alist[pivot]:
		rightmark = rightmark - 1
	
	if rightmark < leftmark:
		done = True

	else:
		tmp = alist[rightmark]
		alist[rightmark] = alist[leftmark]
		alist[leftmark] = tmp
	
	tmp = alist[rightmark]
	alist[rightmark] = alist[first]
	alist[first] = tmp
	return rightmark

n = int(raw_input())
a = raw_input().split()
arr = [int(x) for x in a]

print ' '.join(str(x) for x in quicksort(arr))

