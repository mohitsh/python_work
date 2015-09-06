

def bin_search(alist,item):
	first = 0
	last = len(alist)-1
	found = False
	while first <= last and not found:
		mid = (first + last)/2
		if item < alist[mid]:
			last = mid-1
		elif item > alist[mid]:
			first = mid+1
		elif item == alist[mid]:
			found = True
	
	if found == False:
		return found,-1
	else:
		return found,mid


alist = [1,3,5,8,12,15,17,19,22,24,26,28,31]
print bin_search(alist,8)
print bin_search(alist,22)
print bin_search(alist,31)
print bin_search(alist,100)
