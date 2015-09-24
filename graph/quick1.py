

def quick(alist):
	quicksort(alist,0,len(alist)-1)

def quicksort(alist,first,last):
	#print alist
	if first < last:
		split = partition(alist,first,last)
		quicksort(alist,first,split-1)
		quicksort(alist,split+1,last)

	
def partition(alist,first,last):
	pivot = first 
	left = first +1 
	right = last 
	done = False

	while not done:
		while left <= right and alist[left] <= alist[pivot]:
			left = left + 1
		while right >= left and alist[right] >= alist[pivot]:
			right = right - 1
		if left > right:
			done = True
		else:
			tmp = alist[left]
			alist[left] = alist[right]
			alist[right] = tmp
			#done = True

	tmp = alist[right]
	alist[right] = alist[first]
	alist[first] = tmp
	return right

alist = [5,4,3,2,1]
#print alist
#quick(alist)
#print alist

alist = [54,26,93,17,77,31,44,55,20]
print alist
quick(alist)
print alist

alist = range(500,0,-1)
quick(alist)
print alist
