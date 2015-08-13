
def shortBubbleSort(a):
	exchange = True
	numpass = len(a) - 1

	while numpass > 0 and exchange:
		exchange = False
		for i in range(numpass):
			if a[i] > a[i+1]:
				exchange = False
				tmp = a[i]
				a[i] = a[i+1]
				a[i+1] = tmp
		numpass = numpass - 1
	return a

alist=[20,30,40,90,50,60,70,80,100,110]
shortBubbleSort(alist)
print(alist)
