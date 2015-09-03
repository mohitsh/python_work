

def reverse(alist,first,last):
	if first <= last:
		tmp = alist[first]
		alist[first] = alist[last]
		alist[last] = tmp
		return reverse(alist, first+1, last-1)
	

alist = [1,2,3,4,5]
reverse(alist,0,4)
print alist
alist = ['dalla','jain','namit','mittal','varun','bohra']
reverse(alist,0,4)
print alist
