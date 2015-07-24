def insert_sort(a):
	for i in range(len(a)):
		position = i
		current_value = a[i]
		while position > 0 and a[position-1] > current_value:
			a[position] = a[position -1]
			position = position - 1
		a[position] = current_value

	return a

a = [9,8,7,6,5,4,3,2,1]
print 'given array =>' , a
insert_sort(a)
print 'sorted array =>', a
