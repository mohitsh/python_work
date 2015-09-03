

def unique(alist):
	for i in range(len(alist)):
		for j in range(i+1,len(alist)):
			if alist[j] == alist[i]:
				return False,i,j
	return True

print 'unique part -->'
alist = [1,2,3,4,5,6]
print unique(alist)
alist = [1,2,3,3,100]
print unique(alist)

def unique2(alist):
	b = sorted(alist)
	for i in range(1,len(alist)):
		if b[i-1] == b[i]:
			return False,i-1,i
	return True

print 'unique2 part -->'
alist = [12,14,15,16,16,40,40]
print unique(alist)
alist = [12,13,14,15,18]
print unique(alist)

	
	
