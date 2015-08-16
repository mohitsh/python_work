

def insert_sort(alist):
	
	# number of times this loop is going to run
	for index in range(1,len(alist)):	 # n-1 times
		
		
		position  = index # token that will traverse the array
		location = alist[index] # element to be inserted
		
		# search for appropriate position to insert location
		while position > 0 and alist[position-1] > location:
			alist[position] = alist[position-1]
			position  = position - 1
			
		#insert the location at its position 
		temp = location
		location = alist[position]
		alist[position] = temp
	return alist




def insert_sort2(alist):
	
	for index in range(1,len(alist)):
		position = index
		location = alist[index]
		
		while position > 0 and alist[position-1] > location:
			alist[position] = alist[position-1]
			position = position - 1
		
		temp = location
		location = alist[position]
		alist[position] = temp
	
	return alist



def select_sort(alist):
	
	for fillslot in range(len(alist)-1,0,-1):
		posOfMax = 0
		for i in range(1,fillslot+1):
			if alist[i] > alist[posOfMax]:
				posOfMax = i
			
		tmp = alist[fillslot]
		alist[fillslot] = alist[posOfMax]
		alist[posOfMax] = tmp
	
	return alist

def bubble_sort(alist):
	for i in range(len(alist)-1, 0, -1):
		for j in range(i):
			if alist[j] > alist[j+1]:
				temp = alist[j]
				alist[j] = alist[j+1]
				alist[j+1] = temp

	return alist

		
alist = [54,26,93,17,77,31,44,55,20]
print 'original', alist
print 'insert_sort', insert_sort(alist)
print 'insert_sort2', insert_sort2(alist)
print 'select_sort', select_sort(alist)
print 'bubble_sort', bubble_sort(alist)
