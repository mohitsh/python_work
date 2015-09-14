

def bubble(alist):
		
	for i in range(len(alist)-1,0,-1):             # making n-1 passes
		for j in range(i):		       # making i passes for each pass
			if alist[j] > alist[j+1]:
				temp = alist[j]
				alist[j] = alist[j+1]
				alist[j+1] = temp

	return alist

def selection(alist):
	for i in range(len(alist)-1,0,-1):             # make n-1 passes
		max_pos = 0
		for j in range(1,i+1):		       # find position for max_pos
			if alist[j] > alist[max_pos]:
				max_pos = j
		temp = alist[i]
		alist[i] = alist[max_pos]
		alist[max_pos] = temp
	return alist

alist = [6,5,4,3,2,1]
print alist
print 'bubble -> ', bubble(alist)
alist = [6,5,4,3,2,1]
print 'selection -> ', selection(alist)

def selection_sort(alist):
	# these slots are going to filled so n-1 passes
	for i in range(len(alist)-1,0,-1):
		pos_max = 0
		# make comparisons from 1 to last element to find the right spot
		for j in range(1,i+1):
			if alist[j] > alist[pos_max]:
				pos_max = j
		# pos_max is known so for every pass replace pos_max with i
		temp = alist[i]
		alist[i] = alist[pos_max]
		alist[pos_max] = temp
	return alist

a = [6,5,4,3,2,1]
print selection_sort(alist)

def bubble_sort(alist):
	# make n-1 passes to sort all elements
	for i in range(len(alist)-1,0,-1):
		# making i comparisons for each pass
		for j in range(i):
			if alist[j] > alist[j+1]:
				alist[j],alist[j+1] = alist[j+1],alist[j]
	return alist

alist = [6,5,4,3,2,1]
print bubble_sort(alist) 

def bubble(alist):
	for i in range(len(alist)-1,0,-1):
		for j in range(i):
			if alist[j] > alist[j+1]:
				temp = alist[j]
				alist[j] = alist[j+1]
				alist[j+1] = temp
	return alist

def select(alist):
	for i in range(len(alist)-1,0,-1):
		pos_max = 0
		for j in range(1,i+1):
			if alist[j] > alist[pos_max]:
				pos_max = j
		temp = alist[i]
		alist[i] = alist[pos_max]
		alist[pos_max] = temp
	return alist


def insert(alist):
	for i in range(1,len(alist)):
		position = i
		value = alist[i]
		while position > 0 and alist[position-1] > value:
			alist[position] = alist[position-1]
			position = position -1
		alist[position] = value

	return alist


def insert_sort(alist):
	for i in range(1,len(alist)):
		position = i
		value =	alist[i]
		while position > 0 and alist[position-1] > value:
			alist[position] = alist[position-1]
			position = position - 1
		alist[position] = value

	return alist

alist = [6,5,4,3,2,1]
print 'original list -> ', alist
bubble_sort(alist)
print 'bubble sort ->', alist
alist = [6,5,4,3,2,1]
print 'original list ->', alist
select(alist)
print 'select sort ->', alist
alist = [6,5,4,3,2,1]
print 'original list -> ', alist
insert(alist)
print 'insert sort ->', alist
alist = [6,5,4,3,2,1]
print 'original list ->', alist
insert_sort(alist)
print 'insert sort ->', alist






























a
