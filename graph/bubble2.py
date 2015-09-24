

def bubble(alist):
	for i in range(len(alist)-1,0,-1):
		for j in range(i):
			if alist[j] > alist[j+1]:
				tmp = alist[j]
				alist[j] = alist[j+1]
				alist[j+1] = tmp
	
alist = [6,5,4,3,2,1]
print alist
bubble(alist)
print "sorted ->", alist


def merge(alist):
	if len(alist) > 1:
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

alist = [6,5,4,3,2,1]
print alist
merge(alist)
print "sorted ->",alist 	

def quick(alist):
	quicksort(alist,0,len(alist)-1)

def quicksort(alist,first,last):
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
			left = left + 1
		while right >= left and alist[right] >= alist[pivot]:
			right = right - 1
		
		if left > right:
			done = True
		else:
			tmp = alist[left]
			alist[left] = alist[right]
			alist[right] = tmp
	tmp = alist[first]
	alist[first] = alist[right]
	alist[right] = tmp
	
	return right

alist = [8,7,6,5,4,3,2,1]
print alist 
quick(alist)
print "sorted", alist















