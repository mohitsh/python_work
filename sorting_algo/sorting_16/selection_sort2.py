

def select_sort(alist):
	
	for passnum in range(len(alist)-1,0,-1):
		
		posOfMax = 0
		
		for i in range(1,passnum+1):
			if alist[i] > alist[posOfMax]:
				posOfMax = i
		
		temp = alist[passnum]
		alist[passnum] = alist[posOfMax]
		alist[posOfMax] = temp
	
	return alist

alist = [8,7,6,5,4,3,2,1,0]
print alist
print select_sort(alist) 
