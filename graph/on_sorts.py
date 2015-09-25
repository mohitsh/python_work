
def bubble(a):
	for j in range(len(a)-1,0,-1):
		for i in range(j):
			if a[i] > a[i+1]:
				tmp = a[i]
				a[i] = a[i+1]
				a[i+1] = tmp
	

def select(alist):
	for slot in range(len(alist)-1,0,-1):
		posmax = 0
		for location in range(1,slot+1):
			if alist[location] > alist[posmax]:
				posmax = location
		tmp = alist[posmax]
		alist[posmax] = alist[slot]
		alist[slot] = tmp
	
	
def insert(alist):
	for index in range(1,len(alist)):
		pos = index 
		curVal = alist[pos]
		while pos > 0 and alist[pos-1] > curVal:
			alist[pos] = alist[pos-1]
			pos = pos - 1
		alist[pos] = curVal

alist = [23,45,2,412,6767,767,345,56,54243,12663,12123,54,75634]
bubble(alist)
print alist
