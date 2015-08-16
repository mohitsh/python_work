

def insert_sort(alist):
	for i in range(1,len(alist)):
		#print alist[:i]
		position = i
		location = alist[position]
		
		while position > 0 and alist[position-1] > location:
			alist[position] = alist[position - 1]
			position = position - 1
		alist[position] = location 
		
	return alist
		



alist  =  [54,26,93,17,77,31,44,55,20]
print alist
print insert_sort(alist)
