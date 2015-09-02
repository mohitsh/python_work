

def seq_search(alist,item):
	pos = 0
	flag = False
	while pos < len(alist) and not flag:
		if item == alist[pos]:
			flag = True
		else:
			pos = pos + 1
	if flag == True:
		return pos
	else:
		return False

alist = ['mohit','shukla','dalla','kutta']
print seq_search(alist,'dalla')
print seq_search(alist,'aditya')
