
def partition(a,first,last):
	pivot = first
	leftmark = first + 1
	rightmark = last
	
	done = False
	
	while not done:
		while leftmark <= rightmark and a[leftmark] <= a[pivot]:
			leftmark = leftmark + 1
		while rightmark >= leftmark and a[rightmark] >= a[pivot]:
			rightmark = rightmark - 1

		if rightmark > leftmark:
			done = True
		else:
			tmp = a[leftmark]
			a[leftmark] = a[rightmark]
			a[rightmark] = tmp

		tmp = a[first] 
		a[first] = a[rightmark]
		a[rightmark] = tmp
	
	return rightmark 

a = [54,26,93,17,77,31,44,55,20]
index = partition(a,0,8) 
print index, a[index]
