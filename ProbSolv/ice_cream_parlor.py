

def binary_search(alist,item):
	first = 0
	last = len(alist)-1
	found = False
	
	while not found and first <= last:
		mid = (first+last)/2
		if alist[mid] == item:
			found = True
		else:
			if item > alist[mid]:
				first = mid + 1
			else:
				last = mid - 1
	if found == False:
		return -1
	else:
		return mid

def ice_cream_parlor(m,n,arr):
	#print m
	#print n
	#print arr
	for a in range(len(arr)):
		b = m-arr[a]
		place = binary_search(arr,b)
		if place != -1:
			dude = [a+1,place+1]
			dude.sort()
			return ' '.join([str(x) for x in dude])
			
				


t = int(raw_input())
for i in range(t):
	m = int(raw_input())
	n = int(raw_input())
	a = raw_input().split()
	arr = [int(x) for x in a]
	print ice_cream_parlor(m,n,arr)


#alist = [1,4,7,10,15,19,23,28,34,38,45,48,50,54,59]
#print binary_search(alist,7)
#print binary_search(alist,28)
#print binary_search(alist,48)
#print binary_search(alist,100)
