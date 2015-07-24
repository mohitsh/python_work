def insert_sort(a):
	for passnum in range(1,len(a)):
		index = passnum
		current_value = a[passnum]
		while index > 0 and a[index-1] > current_value:
			a[index] = a[index-1]
			index = index - 1
		a[index] = current_value
	return a

a = [9,8,7,6,5,4,3,2,1]
print 'original array ==>'
print a
insert_sort(a)
print 'sorted a ==>'
print a
