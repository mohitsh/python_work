







def partition(a,first,last):
	pivot = first
	leftvalue = first + 1
	rightvalue = last
	
	done = False
	while not done:
		while leftvalue <= rightvalue and a[leftvalue] <= pivot:
			leftvalue = leftvalue + 1
		
		while rightvalue >= leftvalue and a[rightvalue] >= pivot:
			rightvalue = rightvalue - 1
		
		if rightvalue < leftvalue:
			done = True
		else:
			tmp = a[leftvalue]
			a[leftvalue] = a[rightvalue]
			a[rightvalue] = tmp
	tmp = a[first]
	a[first] = a[rightvalue]
	a[rightvalue] = tmp

	return rightvalue

alist = [54,26,93,17,77,31,44,55,20]
print partition(alist,1,8)
print partition(alist,2,8)
print partition(alist,3,8)
print partition(alist,4,8)
