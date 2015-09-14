

def bubble(alist):
	for i in range(len(alist),0,-1):
		for j in range(1,i):
			if alist[j-1] > alist[j]:
				temp = alist[j-1]
				alist[j-1] = alist[j]
				alist[j] = temp
		print alist
	return alist

def short_bubble(alist):
	exchanges = True
	passnum = len(alist)
	while passnum > 0 and exchanges == True:
		exchanges = False
		for j in range(1,passnum):
			if alist[j-1] > alist[j]:
				exchanges = True
				temp = alist[j-1]
				alist[j-1] = alist[j]
				alist[j] = temp
		passnum = passnum - 1
	return alist	

def shortBubble(alist):
	exchange = True
	passnum = len(alist)
	while passnum > 0 and exchange == True:
		exchange = False
		for i in range(1,passnum):
			if alist[i-1] > alist[i]:
				exchange = True
				temp = alist[i-1]
				alist[i-1] = alist[i]
				alist[i] = temp
		passnum = passnum - 1

	return alist

def selection_sort(alist):
	for i in range(len(alist)-1,0,-1):
		
		index = 0
		for location in range(1,i+1):
			if alist[index] > alist[i]:
				index = i
		
		temp = alist[index]
		alist[index] = alist[i]
		alist[i] = temp
	print alist
		
	return alist
			

alist = [6,5,4,3,2,1]
print selection_sort(alist)
					
alist = [6,5,4,3,2,1]
#print alist

#bubble(alist)
alist = [6,5,4,3,2,1]
print short_bubble(alist)
alist = [6,5,4,3,2,1]
print shortBubble(alist)

