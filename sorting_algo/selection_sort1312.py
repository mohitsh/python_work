

def selection_sort(alist):
	
	for fillspot in range(len(alist)-1,0,-1):
		posMax = 0
		for location in range(1,fillspot+1):
			if alist[location] > alist[posMax]:
				posMax = location
		
		temp = alist[fillspot]
		alist[fillspot] = alist[posMax]
		alist[posMax] = temp

	return alist

alist = [6,5,4,3,2,1,0]
print 'original list ==>', alist
print 'sorted list ==>', selection_sort(alist)
