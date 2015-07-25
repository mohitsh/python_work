
#this is sorted sequential search or linear search 
# it gives better results only when item is not 
# present in the list.
# Item not in the list
#best case is 1 worst in n and average in n/2
# Item in the list
# best case is 1 worst in n and average in n/2


def lin_sort_search(a,val):
	found = False
	stop = False
	i = 0
	
	while i<len(a) and not found and not stop:
		if a[i] == val:
			found = True
		else:
			if a[i] > val:
				stop = True
			else:
				i = i + 1

	return found

a = [1,2,4,5,6,6]
print lin_sort_search(a,3)
print lin_sort_search(a,10)
print lin_sort_search(a,6)

