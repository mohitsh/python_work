

def bubble_sort(alist):
	
	for passnum in range(len(alist)-1,0,-1):
		
		for i in range(passnum):
			if alist[i] > alist[i+1]:
				temp = alist[i]
				alist[i] = alist[i+1]
				alist[i+1] = temp
	return alist


alist = [9,8,7,6,5,4,3,2,1,0]
print alist
print bubble_sort(alist)
