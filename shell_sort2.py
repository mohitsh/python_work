def shell_sort(a):
	sublist_count = len(a)
	while sublist_count > 0:
		for i in range(sublist_count):
			gapInsertSort(a,i,sublist_count)

		sublist_count = sublist_count/2
	
def gapInsertSort(a,start,gap):
	for i in range(len(a)):
		index = i
		current_value = a[i]
		while index >= gap and a[index-gap]> current_value:
			a[index] = a[index -gap]
			index = index - gap
		a[index] = current_value
	

a = [54,26,93,17,77,31,44,55,20]
print 'original array ==>'
print a
shell_sort(a)
print 'sorted list ==> '
print a
	
