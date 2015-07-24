def insert_sort(a):
	for i in range(1,len(a)):
		position = i
		current_value = a[i]
		
		while position > 0 and a[position-1] > current_value:
			a[position] = a[position-1]
			position = position - 1
		
		a[position] = current_value

a = [12,34,123,34,123,34,123,354,34]
print a
insert_sort(a)
print a 
