def merge_sort(a):
	print 'splitting >',a
	if len(a)>1:
		mid = len(a)//2
		lefthalf = a[:mid]
		righthalf = a[mid:]
		
		merge_sort(lefthalf)
		merge_sort(righthalf)
	
		i = 0
		j = 0
		k = 0
		while i<len(lefthalf) and j<len(righthalf):
			if lefthalf[i] < righthalf[j]:
				a[k] = lefthalf[i]
				i = i+1
			else:
				a[k] = righthalf[j]
				j = j + 1
			k = k+1
		
		while i<len(lefthalf):
			a[k] = lefthalf[i]
			i = i + 1
			k = k + 1
		while j<len(righthalf):
			a[k] = righthalf[j]
			j = j + 1
			k = k + 1

	print 'merging >',a

a = [54,26,93,17,77,31,44,55,20]
merge_sort(a)

 
