


def shell_sort(alist):
	sublist_count = len(alist)//2
	while sublist_count > 0:
		for startposition in range(sublist_count):
			gapInsertionSort(startposition,alist,sublist_count)
		
		print 'gap',sublist_count,'list',alist
		sublist_count = sublist_count//2

def gapInsertionSort(startposition,alist,gap):
	for index in range(startposition, len(alist), gap):
		position = index 
		location = alist[position]
		
		while position >= gap and alist[position - gap] >= location:
			alist[position] = alist[position-gap]
			position = position - gap
		alist[position] = location

	return alist

def merge_sort(alist):
	if len(alist) > 1:
		mid = len(alist)//2
		left = alist[mid:]
		right = alist[:mid]
		
		merge_sort(left)
		merge_sort(right)
		
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
	print 'merging', alist


def quick_sort(alist):
	quicksorthelper(alist,0,len(alist)-1)
	
def quicksorthelper(a,first,last):
	
	if first<last:
		split = partition(a,first,last)
		quicksorthelper(a,first,split-1)
		quicksorthelper(a,split+1,last)

def partition(a,first,last):
	pivot = first
	left = first + 1
	right = last

	done = False

	while not done:
		while left <= right and a[left] <= a[pivot]:
			left = left + 1
		while right >= left and a[right] >= a[pivot]:
			right = right - 1
		if left > right:
			done = True
		else:
			tmp = a[left]
			a[left] = a[right]
			a[right] = tmp
	tmp = a[right]
	a[right] = a[first]
	a[first] = tmp
	return right







def insert_sort(alist):
	for index in range(1,len(alist)):
		position = index
		location = alist[position]
		while position > 0 and alist[position-1] > location:
			alist[position] = alist[position-1]
			position = position -1
		alist[position] = location
	return alist


def select_sort(alist):
	for fillslot in range(len(alist)-1,0,-1):
		posOfMax = 0
		for i in range(1,fillslot+1):
			if alist[i] > alist[posOfMax]:
				posOfMax = i
		temp = alist[posOfMax]
		alist[posOfMax] = alist[fillslot]
		alist[fillslot] = temp
				
	return alist

def bubble_sort(alist):
	for j in range(len(alist)-1,0,-1):
		for i in range(j):
			if alist[i] > alist[i+1]:
				tmp = alist[i]
				alist[i] = alist[i+1]
				alist[i+1] = tmp	
	return alist	


alist = [9,8,7,6,5,4,3,2,1,0]
shell_sort(alist)
alist = [9,8,7,6,5,4,3,2,1,0]
merge_sort(alist)
alist = [9,8,7,6,5,4,3,2,1,0]
quick_sort(alist)
print 'quick_sort', alist
alist = [9,8,7,6,5,4,3,2,1,0]
print 'insert_sort', insert_sort(alist)
alist = [9,8,7,6,5,4,3,2,1,0]
print 'select_sort', select_sort(alist)
alist = [9,8,7,6,5,4,3,2,1,0]
print 'bubble_sort',bubble_sort(alist)
