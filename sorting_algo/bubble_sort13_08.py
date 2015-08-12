

def bubble_sort(alist):
	
	
	for j in range(len(alist)-1,0,-1):

		for i in range(j):
			if alist[i] > alist[i+1]:
				temp = alist[i+1]
				alist[i+1] = alist[i]
				alist[i] = temp
				print 'after sorting', i, 'list -->', alist
	
	return alist



alist = [54,26,93,17,77,31,44,55,20]
print alist
print bubble_sort(alist)
