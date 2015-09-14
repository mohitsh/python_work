

def bubble(alist):
	for i in range(len(alist),0,-1):
		for j in range(1,i):
			if alist[j-1] > alist[j]:
				temp = alist[j-1]
				alist[j-1] = alist[j]
				alist[j] = temp

	return alist


alist = [6,5,4,3,2,1]
print alist
print bubble(alist)

