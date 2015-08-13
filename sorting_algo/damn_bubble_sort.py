

def bubble_sort(alist):
	
	for numpass in range(len(alist)-1,0,-1):
		for j in range(numpass):
			
			if alist[j] > alist[j+1]:
				temp = alist[j]
				alist[j] = alist[j+1]
				alist[j+1] = temp
	return alist

alist = [234,56,214,546,1243,54,567,346,2341,32456,24,54647]
print bubble_sort(alist)



def short_bubble_sort(alist):
		
	numpass = len(alist)-1
	exchange = True
	while numpass > 0 and exchange:
		exchange = False
		for i in range(numpass):
			if alist[i] > alist[i+1]:
				exchange = True
				temp = alist[i]
				alist[i] = alist[i+1]
				alist[i+1] = temp
		numpass = numpass - 1

	return alist

alist=[20,30,40,90,50,60,70,80,100,110]
print short_bubble_sort(alist)





