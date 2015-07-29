def select_sort(a):
	for fillslot in range(len(a)-1,0,-1):
		posOfMax = 0
		for location in range(1,fillslot+1):
			if a[location] > a[posOfMax]:
				posOfMax = location
			
		tmp = a[posOfMax]
		a[posOfMax] = a[fillslot]
		a[fillslot] = tmp
	
	return a
a = [12,345,546,234,56,23,5667,234,56,2134,5467,6756]
print a
select_sort(a)
print a
