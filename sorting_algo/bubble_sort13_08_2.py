

def bubble_sort(a):
	
	for i in range(len(a)-1,0,-1):
		
		for j in range(i):
			if a[j] > a[j+1]:
				temp =  a[j]
				a[j] = a[j+1]
				a[j+1] = temp
	
	return a

alist = [54,26,93,17,77,31,44,55,20]
print alist
print bubble_sort(alist)

