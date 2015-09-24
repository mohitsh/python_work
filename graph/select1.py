
def select(alist):
	for fill in range(len(alist)-1,0,-1):
		posmax = 0
		for location in range(1,fill+1):
			if alist[location] > alist[posmax]:
				posmax =location
		tmp = alist[fill]
		alist[fill] = alist[posmax]
		alist[posmax] = tmp

	
alist = [5,4,3,2,1]
print alist
select(alist)
print "selected ->", alist

def bubble(alist):
	for i in range(len(alist)-1,0,-1):
		for j in range(i):
			if alist[j] > alist[j+1]:
				tmp = alist[j]
				alist[j] = alist[j+1]
				alist[j+1] = tmp
	
alist = [6,5,4,3,2,1]
bubble(alist)
print "bubbled ->", alist

def insert(alist):
	for index in range(1,len(alist)):
		position = index
		currentValue = alist[index]
		while position > 0 and alist[position-1] > currentValue:
			alist[position] = alist[position-1]
			position = position -1
		alist[position] = currentValue
alist = [6,5,4,3,2,1]
print alist
insert(alist)
print "inserted ->",alist
