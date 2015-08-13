

def selection_sort(alist):
	
	for fillslot in range(len(alist)-1,0,-1):
		posMax = 0
		for i in range(1,fillslot+1):
			if alist[i] > alist[posMax]:
				posMax = i
		
		temp = alist[posMax]
		alist[posMax] = alist[fillslot]
		alist[fillslot] = temp
	
	return alist

alist = [9,8,7,6,5,4,3,2,1,0]
print 'original list ==>', alist
print 'after selection_sort ==>', selection_sort(alist)


def bubble_sort(alist):
	
	for numpass in range(len(alist)-1,0,-1):
		for i in range(numpass):
			
			if alist[i] > alist[i+1]:
				temp = alist[i]
				alist[i] = alist[i+1]
				alist[i+1] = temp
		
	return alist


print 'after bubble sort ==>', bubble_sort(alist)


