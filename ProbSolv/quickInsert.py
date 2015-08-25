
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
	print count1
        return count1


def quicksort(a):
	quicksorthelper(a,0,len(a)-1)
	fcount = []
def quicksorthelper(a,first,last):
	#print 'sorted', a
	
	if first < last:
		split = partition(a,first,last)[0]
		quicksorthelper(a,first,split-1)
		quicksorthelper(a,split+1,last)
		fcount.append(partition(a,first,last)[1])
		print (fcount)

def partition(a,first,last):
	pivot = first
	leftmark = first + 1
	rightmark = last
	done = False
	count = 0
	while not done:
		while leftmark <= rightmark and a[leftmark] <= a[pivot]:
			leftmark = leftmark + 1
		while rightmark >= leftmark and a[rightmark] >= a[pivot]:
			rightmark = rightmark - 1
	
		if rightmark < leftmark:
			done = True

		else:
			
			tmp = a[leftmark]
			a[leftmark] = a[rightmark]
			a[rightmark] = tmp
		
	count = count+1
	tmp = a[first]
	a[first] = a[rightmark]
	a[rightmark] = tmp
	return rightmark,count



n = int(raw_input())
arr = []
a = raw_input().split()
a = [int(x) for x in a]
insert(a)
quicksort(a)	
print a
