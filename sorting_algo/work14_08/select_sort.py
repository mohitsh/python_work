
def select_sort(alist):
		
	for fillslot in range(len(alist)-1,0,-1):
		
		# this while loop finds out the largest value in the 
		# current array 
		position = fillslot
		value = alist[position]
		
		for i in range(fillslot):
			posMax = 0
			while position > 0 and  alist[position] > alist[posMax]:
				posMax = position
		position = position - 1
		
		# here we are placing the largest term at its position
		temp = alist[fillslot]
		alist[fillslot] = alist[posMax]
		alist[posMax] = temp

	return alist


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]

print alist
print select_sort(alist)
