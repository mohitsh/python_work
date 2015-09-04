

def insert_sort(alist):
	for i in range(1,len(alist)):
		pos = i 
		val = alist[i]
		while pos > 0 and val < alist[pos-1]:
			tmp = alist[pos] 
			alist[pos] = alist[pos-1]
			alist[pos-1] = tmp
			pos = pos -1
			#print alist
	return alist

alist  = [5,4,3,2,1]
print insert_sort(alist)
