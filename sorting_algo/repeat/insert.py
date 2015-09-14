
def insert(alist):
	for i in range(1,len(alist)):
		pos = i
		value = alist[pos]
		while pos > 0 and alist[pos-1] > value:
			alist[pos] = alist[pos-1]
			pos = pos-1
		alist[pos] = value	
	return alist

def select(alist):
	for i in range(len(alist)-1,0,-1):
		maxPos = 0
		for j in range(1,i+1):
			if alist[j] > alist[maxPos]:
				maxPos = j
		temp = alist[i]
		alist[i] = alist[maxPos]
		alist[maxPos] = temp

	return alist

def bubble(alist):
	for i in range(len(alist)-1,0,-1):
		for j in range(i):
			if alist[j] > alist[j+1]:
				alist[j], alist[j+1] = alist[j+1],alist[j]
	
	return alist

def shell_sort(alist):
	sublistcount = len(alist)//2
	while sublistcount > 0:
		for startposition in range(sublistcount):
			gapinsertsort(startposition,alist,sublistcount)
		
		sublistcount = sublistcount//2
	

def gapinsertsort(start,alist,gap):
	for i in range(start+gap,len(alist),gap):
		position = i
		value = alist[i]
		while position >= gap and alist[position-gap] > value:
			alist[position] = alist[position-gap]
			position = position - gap
		alist[position] = value
		
alist = [6,5,4,3,2,1]
print 'original list ->', alist
shell_sort(alist)
print 'shell sorted list ->', alist

alist = [6,5,4,3,2,1]
print 'original list ->', alist
bubble(alist)
print 'sorted list ->', alist 



alist = [6,5,4,3,2,1]
print 'original list ->', alist
select(alist)
print 'sorted list ->', alist


alist = [6,5,4,3,2,1]
print 'print original ->', alist
insert(alist)
print 'print sorted ->', alist
