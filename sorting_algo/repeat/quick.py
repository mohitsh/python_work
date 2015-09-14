
def quick(alist):
	quicksort(alist,0,len(alist)-1)

def quicksort(alist,first,last):
	print alist
	if first < last:
		split = partition(alist,first,last)
		quicksort(alist,first,split-1)
		quicksort(alist,split+1,last)


def partition(alist,first,last):
	pivot = first
	left = first + 1
	right = last
	
	done = False
	while not done:
		while left <= right and alist[left] <= alist[pivot]:
			print 'fuck you'
			left = left + 1
		while right >= left and alist[right] >= alist[pivot]:
			right = right - 1
		if left > right:
			done = True

		else:
			temp = alist[left]
			alist[left] = alist[right]
			alist[right] = temp
	temp = alist[right]
	alist[right] = alist[first]
	alist[first] = temp

	return right

alist = [6,5,4,3,2,1]
print 'original list ->', alist
print 'sorted ->', quick(alist)
		
