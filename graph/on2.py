
def insert(alist):
	for index in range(1,len(alist)):
		pos = index
		currentVal = alist[index]
		while pos > 0 and alist[pos-1] > currentVal:
			alist[pos] = alist[pos-1]
			pos = pos -1
		alist[pos] = currentVal

alist = [6,5,4,3,2,1]
print alist
insert(alist)
print "inserted ->", alist




def insert2(alist):
	for index in range(1,len(alist)):
		pos = index
		currentVal = alist[pos]
		
		while pos > 0 and alist[pos-1] > currentVal:
			alist[pos] = alist[pos-1]
			pos = pos-1
		alist[pos] = currentVal

	
alist = [12,45,2,34,55,12,134,1,2,56,6]
print alist
insert2(alist)
print "insert sorted ->",alist

def select(alist):
	for slot in range(len(alist)-1,0,-1):
		posofmax = 0
		for location in range(1,slot+1):
			if alist[location] > alist[posofmax]:
				posofmax = location
		tmp = alist[posofmax]
		alist[posofmax] = alist[slot]
		alist[slot] = tmp
alist = [56,234,1,3435,56,234,435,67,2,341,1234,345,76,899]
print alist
select(alist)
print "select sorted ", alist


def bubble(alist):
	for i in range(len(alist)-1,0,-1):
		for j in range(i):
			if alist[j] > alist[j+1]:
				alist[j],alist[j+1] = alist[j+1],alist[j]
		
alist = [567,345,234,67,4356,657,354,1234,456,67,234,567,132]
print alist
bubble(alist)
print "bubble ->", alist




































































