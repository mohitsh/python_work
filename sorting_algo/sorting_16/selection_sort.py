

def select_sort(alist):
		
	# total no of passes are n-1 so loop runs n-1 times
	# and passnum starts from end of the list 
	# at the end of this loop largest no is placed at 
	# its desired position
	
	for passnum in range(len(alist)-1,0,-1):
	
		# and for each pass 0the position is considered as
		# a max position
		posMax = 0
		# for for each passnum check for the maximum value in the
		# unsorted array
		
		for j in range(1, passnum+1):
			
			if alist[j] > alist[posMax]:
				posMax = j
		
		# at this point largest no is placed at its position
		# exchange passnum with posMax		
		temp = alist[passnum]
		alist[passnum] = alist[posMax]
		alist[posMax] = temp
	
	return alist

alist = [8,7,6,5,4,3,2,1,0]
print alist
print select_sort(alist)		
