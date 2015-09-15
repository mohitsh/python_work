
def bubble(alist):
	for i in range(len(alist)-1,0,-1):
		for j in range(i):
			if alist[j] > alist[j+1]:
				alist[j],alist[j+1] = alist[j+1],alist[j]
	return alist

alist = [6,5,4,3,2,1]
print "original array ->", alist
print "sorted array ->", bubble(alist)

def bubble_sort(alist):
	count = 0
	for i in range(len(alist)-1,0,-1):
		done = True
		index = 0
		
		while done and index < i:
			done = False
			
			if alist[index] > alist[index+1]:
				done = True
				alist[index],alist[index+1] = alist[index+1],alist[index]
				#print "fuck this happened"
				count = count + 1
			index = index + 1
	#print "count ->", count
	return alist,count


alist = [6,5,4,3,2,1]
print "original list ->", alist
print "sorted list ->", bubble_sort(alist)
