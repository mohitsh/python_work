

def select(alist):
	for i in range(len(alist)-1,0,-1):
		pos_max = 0
		for j in range(1,i+1):
			if alist[j] > alist[pos_max]:
				pos_max = j
		temp = alist[i]
		alist[i] = alist[pos_max]
		alist[pos_max] = temp
	return alist

alist = [6,5,4,3,2,1]
print 'originality ->', alist
print 'sorted ->', select(alist)

def bubble(alist):
	for i in range(len(alist)-1,0,-1):
		for j in range(i):
			if alist[j] > alist[j+1]:
				alist[j], alist[j+1] = alist[j+1], alist[j]
	return alist

def selection(alist):
	for i in range(len(alist)-1,0,-1):
		posmax = 0
		for j in range(1,i+1):
			if alist[j] > alist[posmax]:
				posmax = j
		temp = alist[posmax]
		alist[posmax] = alist[i]
		alist[i] = temp
	return alist

def insert(alist):
	for i in range(1,len(alist)):
		position = i 
		value = alist[position]
		while position > 0 and alist[position-1] > value:
			alist[position] = alist[position-1]
			position = position - 1
		alist[position] = value
	return alist

alist = [6,5,4,3,2,1]
print 'original list ->', alist
print 'insert sorted ->', insert(alist)

alist = [6,5,4,3,2,1]
print 'original array ->', alist
print 'bubble sorted ->', bubble(alist)

alist = [6,5,4,3,2,1]
print 'original array ->', alist
print 'select sorted ->', selection(alist)

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
	return alist


alist = [6,5,4,3,2,1]
print 'original list ->', alist
print 'merge sorted list ->', merge(alist)

def quick(alist):
	quicksorthelper(alist,0,len(alist)-1)

def quicksorthelper(alist,first,last):
	if first<last:
		split = partition(alist,first,last)
		quicksorthelper(alist,first,split-1)
		quicksorthelper(alist,split+1,last)

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
			alist[left],alist[right] = alist[right],alist[left]
		alist[right],alist[pivot] = alist[pivot],alist[right]

	return right

alist = [6,5,4,3,2,1]
print 'original list ->', alist
quick(alist)
print 'sorted list ->', alist	








