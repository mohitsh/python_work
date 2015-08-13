

def selection_sort(alist):
	
	for fillslot in range(len(alist)-1,0,-1):
		
		posMax = 0
		for location in range(1,fillslot+1):
			if alist[location] > alist[posMax]:
				posMax = location
			
		temp = alist[fillslot]
		alist[fillslot] = alist[posMax]
		alist[posMax] = temp
	
	return alist
alist = [234,56,214,546,1243,54,567,346,2341,32456,24,54647]
print selection_sort(alist) 
