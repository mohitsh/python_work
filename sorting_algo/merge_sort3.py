

def merge_sort(alist):
	
	if len(alist)>1:
		
		mid = len(alist)//2
		left = alist[mid:]
		right = alist[:mid]
		
		merge_sort(left)
		merge_sort(right)
		
		i = 0
		j = 0
		k = 0
		
		while i<len(left) and j<len(right):
			if left[i] < right[j]:
				alist[k]=left[i]
				i = i + 1
			else:
				alist[k] = right[j]
				j = j + 1
			k = k + 1
		while i<len(left):
			alist[k] = left[i]
			i = i + 1
			k = k + 1
		while j<len(right):
			alist[k] = right[j]
			j = j + 1
			k = k + 1
	print 'mergin', alist


alist = [9,8,7,6,5,4,3,2,1,0]
merge_sort(alist)
print alist
