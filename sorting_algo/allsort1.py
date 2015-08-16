

def bubble_sort(alist):
	
	for passnum in range(len(alist)-1,0,-1):
		for i in range(passnum):
			if alist[i] > alist[i+1]:
				temp = alist[i]
				alist[i] = alist[i+1]
				alist[i+1] = temp
	return alist


def select_sort(alist):
	
	for fillslot in range(len(alist)-1,0,-1):
		posOfMax = 0
		for i in range(1,fillslot+1):
			if alist[i] > alist[posOfMax]:
				posOfMax = i
		temp = alist[fillslot]
		alist[fillslot] = alist[posOfMax]
		alist[posOfMax] = temp

	return alist

def insert_sort(alist):
		
	for i in range(1,len(alist)):
		position = i
		location = alist[i]
		
		while position > 0 and alist[position-1] > location:
			alist[position] = alist[position-1]
			position = position - 1
		alist[position] = location
	
	return alist

alist = [9,8,7,6,5,4,3,2,1,0]
print alist
print 'bubble', bubble_sort(alist)
print 'select', select_sort(alist)
print 'insert', insert_sort(alist)
			 
