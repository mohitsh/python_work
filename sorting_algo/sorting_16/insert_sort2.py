

def insert_sort(alist):
	
	for index in range(1,len(alist)):
		
		position = index
		location = alist[position]
		
		while position > 0 and alist[position-1] > location :
			alist[position] = alist[position-1]
			position = position-1
		alist[position] = location 

	return alist

alist = [9,8,7,6,5,4,3,2,1]
print alist
print insert_sort(alist)
