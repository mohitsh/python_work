def insert_sort(a):
	for i in range(1,len(a)):
		position = i
		current_value = a[i]
		
		while position > 0 and a[position-1] > current_value:
			a[position] = a[position -1]
			position = position - 1
		
		a[position] = current_value

	return a

a = [12,34,123,46,1234,436,1234,123,45,456,2345,456,234,1234,546,4567,547]
print 'original ==> '
print a
insert_sort(a)
print 'sorted ==> '
print a
