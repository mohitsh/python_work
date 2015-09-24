

def bubble(alist):
	for i in range(len(alist)-1,0,-1):
		for j in range(i):
			if alist[j] > alist[j+1]:
				alist[j], alist[j+1] = alist[j+1],alist[j]

alist = [567,34,234,456,567,35424,3456,567,78,234,2345,57,6767]
bubble(alist)
print "bubbled ->", alist

def select(alist):
	for slot in range(len(alist)-1,0,-1):
		posmax = 0
		for location in range(1,slot+1):
			if alist[location] > alist[posmax]:
				posmax = location
		alist[posmax],alist[slot] = alist[slot],alist[posmax]

alist = [567,34,234,456,567,35424,3456,567,78,234,2345,57,6767]
select(alist)
print "selected ->", alist

def insert(alist):
	for index in range(1,len(alist)):
		pos =index 
		val = alist[pos]
		while pos > 0 and alist[pos-1] > val:
			alist[pos] = alist[pos-1]
			pos = pos - 1
		alist[pos] = val

alist = [567,34,234,456,567,35424,3456,567,78,234,2345,57,6767]
insert(alist)
print "inserted ->", alist
		 	
