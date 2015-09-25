
def insert(alist):
	for index in range(1,len(alist)):
		pos =index
		curVal = alist[pos]
		while pos > 0 and alist[pos-1] > curVal:
			alist[pos] = alist[pos-1]
			pos = pos - 1
		alist[pos] = curVal


def select(alist):
	for slot in range(len(alist)-1,0,-1):
		posmax = 0
		for location in range(1,slot+1):
			if alist[location] > alist[posmax]:
				posmax = location

		tmp = alist[posmax]
		alist[posmax] = alist[location]
		alist[location] = tmp
		

def bubble(alist):
	for i in range(len(alist)-1,0,-1):
		for j in range(i):
			if alist[j] > alist[j+1]:
				tmp = alist[j]
				alist[j] = alist[j+1]
				alist[j+1] = tmp

	
alist = [26,54,20,17,77,31,44,55,93]
select(alist)
print alist

alist = [26,54,20,17,77,31,44,55,93]
insert(alist)
print alist

alist = [26,54,20,17,77,31,44,55,93]
bubble(alist)
print alist

