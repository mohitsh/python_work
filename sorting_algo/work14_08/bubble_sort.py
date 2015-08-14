

def bubble_sort(alist):
	
	
	# we have to make total n-1 passes to sort n numbers hence 
	# numpass runs for n-1 times
		
	for passnum in range(len(alist)-1,0,-1):
		
		# every pass sorts one number so number of comparison 
		# decreases with passes hence range of i decreses
		# with increasing no of passes
		for i in range(passnum):
			if alist[i] > alist[i+1]:
				temp = alist[i]
				alist[i] = alist[i+1]
				alist[i+1] = temp
		
	return alist

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]

print alist
print bubble_sort(alist)
