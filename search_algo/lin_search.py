
# sequential/linear search
# when Item is present 
# best case 1 worst case in n and average case is n/2
# when Item is not present 
# best case n worse case n and average case n


def lin_search(a, val):
	length = len(a)
	found = False
	i = 0
	while not found and i < len(a):
		if a[i] == val:
			found = True
		else:
			i = i+1
	return found
a = ['mohit','jain','namit','doga']
print lin_search(a,5)
print lin_search(a,'mohit')
print lin_search(a,'doga')
 
