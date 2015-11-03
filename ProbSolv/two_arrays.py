

def two_array(a,b,n,k):
	flag = 0
	for i in range(n):
		temp = k-a[i]
		index = 0
		found = False
		while index < len(b) and not found:
			if b[index] == temp:
				found = True
				del b[index]
			else:
				index = index + 1
			#print b
		if found == False:
			flag = 1
	return flag
		

t = int(raw_input())
for i in range(t):
	n_k = raw_input().split()
	n_k = [int(x) for x in n_k]
	n = n_k[0]
	k = n_k[1]
	a = []
	b = []
	a = raw_input().split()
	b = raw_input().split()
	a = [int(x) for x in a]
	b = [int(x) for x in b]
	flag = two_array(a,b,n,k)
	if flag == 0:
		print "YES"
	else:
		print "NO"
