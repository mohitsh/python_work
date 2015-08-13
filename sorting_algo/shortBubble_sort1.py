

def shortBubbleSort(alist):
	
	numpass = len(alist)-1
	exchanges = True
	while numpass > 0 and exchanges:
		exchanges = False
		for i in range(numpass):
			if alist[i] > alist[i+1]:
				exchanges = True
				temp = alist[i] 
				alist[i] = alist[i+1]
				alist[i+1] = temp
		numpass = numpass - 1
	return alist
