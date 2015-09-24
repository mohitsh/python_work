
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
		
alist = [6,4,3,2,1]
print alist
merge(alist)
print "merge sorted ->", alist


def quick(alist):
	quickhelp(alist,0,len(alist)-1)

def quickhelp(alist,first,last):
	if first < last:
		split = partition(alist,first,last)
		quickhelp(alist,first,split-1)
		quickhelp(alist,split+1,last)

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
		alist[pivot],alist[right] = alist[right],alist[pivot]
		return right

alist = [45,234,56,67,345,67,78,324,567,2345,567,24,456]
print alist
quick(alist)
print "quick sorted ->", alist

































