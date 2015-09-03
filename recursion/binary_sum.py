

def binary_sum(alist,first,last):
	if first > last:
		return 0
	elif first == last:
		return alist[first]
	else:
		mid = (first + last)/2
		return binary_sum(alist,first,mid) + binary_sum(alist,mid+1,last)

alist = [1,2,3,4,5,6,7]
print binary_sum(alist,0,6)
