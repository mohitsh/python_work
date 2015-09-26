

def merge(alist):
	if len(alist)>1:
		mid = len(alist)//2
		left = alist[:mid]
		right = alist[mid:]
		
		merge(left)
		merge(right)
	
		i = 0
		j = 0 
		k = 0
		
		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				alist[k] = left[i]
				i = i + 1
			else:
				alist[k] = right[j]
				j = j + 1
			k = k + 1

		while i < len(left):
			alist[k] = left[i]
			i = i + 1
			k = k + 1
		while j < len(right):
			alist[k] = right[j]
			j = j + 1
			k = k + 1
	
alist = [26,54,20,17,77,31,44,55,93]
merge(alist)
print alist

def quick(alist):
	quicksort(alist,0,len(alist)-1)

def quicksort(alist,first,last):
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

	tmp = alist[right]
	alist[right] = alist[pivot]
	alist[pivot] = tmp

	return right

alist = [26,54,20,17,77,31,44,55,93]
quick(alist)
print alist
	



		








