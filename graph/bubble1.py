

def bubble(alist):
	for i in range(len(alist)-1,0,-1):
		for j in range(i):
			if alist[j] > alist[j+1]:
				tmp = alist[j]
				alist[j] = alist[j+1]
				alist[j+1] = tmp


alist = [5,4,3,2,1]
print alist
bubble(alist)
print alist
