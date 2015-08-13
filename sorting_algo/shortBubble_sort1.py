

def shortBubbleSort(alist):
	
	numpass = len(alist)-1
	
	# make exchanges True initially to run the while loop and do the sorting 
	exchanges = True
	while numpass > 0 and exchanges:
		# when sorting starts make exchanges False
		exchanges = False
		for i in range(numpass):
			if alist[i] > alist[i+1]:
				# if this this loop runs and some exchange happens
				# then exchange becomes True and this True 
				# overrides the False that was assigned initially
				# so while loop will run again

				# on the other hand if no exchange happens then 
				# exchange remains False 
				# So the next while loop won't run becuase exchanges 
				# is False this time.

				# whoops! some space is saved and time too.	
				exchanges = True
				temp = alist[i] 
				alist[i] = alist[i+1]
				alist[i+1] = temp
			print 'after sorting', i, alist
		numpass = numpass - 1
	return alist

alist=[20,30,40,90,50,60,70,80,100,110]
shortBubbleSort(alist)

