

def insert(alist):
	count1 = 0
	#count2 = 0
	for index in range(1,len(alist)):
		position = index
		currentVal = alist[position]
		
		while position > 0 and alist[position-1] > currentVal:
			count1 = count1 + 1
			alist[position] = alist[position-1]
			position = position - 1
		#count2 = count2 + 1
		alist[position] = currentVal
		#print  ' '.join(str(x) for x in alist)
	#print 'count1',count1
	return count1
	
n = int(raw_input())
a = raw_input().split()
alist = [int(x) for x in a]
print insert(alist)

