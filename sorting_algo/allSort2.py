

def bubble_sort(alist):
	
	for j in range(len(alist)-1,0,-1):
		for i in range(j):
			if alist[i] > alist[i+1]:
				temp = alist[i]
				alist[i] = alist[i+1]
				alist[i+1] = temp
	return alist


def select_sort(alist):
	for fillslot in range(len(alist)-1,0,-1):
		maxpos = 0
		for j in range(1, fillslot+1):
			if alist[j] > alist[maxpos]:
				maxpos = j
		temp = alist[maxpos]
		alist[maxpos] = alist[fillslot]
		alist[fillslot] = temp
	return alist

def insert_sort(alist):
	for index in range(1,len(alist)):
		position = index
		location = alist[position]
		
		while position > 0 and alist[position-1] > location:
			alist[position] = alist[position-1]
			position = position - 1
		temp = alist[index]
		alist[index] = location
		location = temp

	return alist



alist = [54,26,93,17,77,31,44,55,20]
print alist
print 'bubble_sort', bubble_sort(alist)
print 'select_sort', select_sort(alist)		
print 'insert_sort', insert_sort(alist)
