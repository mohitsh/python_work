def shell_sort(a):
	sublist_count = len(a)//2
	while sublist_count > 0:

		for startposition in range(sublist_count):
			gapInsertionsort(a,startposition,sublist_count)

		print 'increment_size > ',sublist_count,' the list > ', a
		sublist_count = sublist_count // 2

def gapInsertionsort(a,start,gap):
	for i in range(start+gap, len(a), gap):
		
		position = i	
		current_value = a[i]
	
		while position >= gap and a[position-gap] > current_value:
			a[position] = a[position - gap]
			position = position - gap
	
		a[position] = current_value

a = [54,26,93,17,77,31,44,55,20]
shell_sort(a)
print 'sorted list ==> '
print a
		  
