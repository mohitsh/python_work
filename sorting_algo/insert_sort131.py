

def insert_sort(alist):
	
	for index in range(1,len(alist)):
		
		position = index 
		currentValue = alist[position]
	
		while position > 0 and currentValue < alist[position-1]:

			alist[position] = alist[position-1]
			position = position - 1
		alist[position] = currentValue
	
	return alist

alist = [54,26,93,17,77,31,44,55,20]

print alist
print insert_sort(alist)

