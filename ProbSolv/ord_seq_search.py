

def ord_seq_search(alist,item):
	pos = 0
	flag = False
	stop = False
	while pos < len(alist) and not flag and not stop:
		if alist[pos] == item:
			flag = True
		else:
			if alist[pos] > item:
				stop = True
			else: 
				pos = pos + 1
		
	if flag == True:
		return pos
	else:
		return False	
		
alist = [1,3,7,9,13]
print ord_seq_search(alist,1)
print ord_seq_search(alist,3)
print ord_seq_search(alist,7)
print ord_seq_search(alist,13)
print ord_seq_search(alist,4)
