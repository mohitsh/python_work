
# using for loop
def seqsearch(alist, token):
	found = False
	for item in alist:
		if token == item:
			found = True
		
	return found

alist = [1,2,3,4,5]
token1 = 3
token2 = 100
print seqsearch(alist,token1)
print seqsearch(alist,token2)


# using while loop
def seqSearch(alist, item):
	found = False
	pos = 0
	while not found and pos < len(alist):
		if alist[pos] == item:
			found = True
		else:
			pos = pos + 1
	return found

alist = [1,2,3,4,5]
token1 = 3
token2 = 100
print seqSearch(alist,token1)
print seqSearch(alist,token2)

