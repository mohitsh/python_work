

def select(alist):
	for i in range(len(alist)-1,0,-1):
		pos_max = 0
		for j in range(1,i+1):
			if alist[j] > alist[pos_max]:
				pos_max = j
		temp = alist[i]
		alist[i] = alist[pos_max]
		alist[pos_max] = temp
	return alist

alist = [6,5,4,3,2,1]
print 'originality ->', alist
print 'sorted ->', select(alist)
