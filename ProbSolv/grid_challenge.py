

def grid_sort(arr,m):
	for i in range(m):
		arr[i] = ''.join(sorted(arr[i]))
	flag = 1
	for i in range(m):
		for j in range(1,m):
			if (arr[j][i] < arr[j-1][i]):
				flag = 0
				break
	return flag

n = int(raw_input())
for i in range(n):
	m = int(raw_input())
	arr = []
	for j in range(m):
		ch = str(raw_input())
		arr.append(ch)
		
	ans = grid_sort(arr,m)
	if ans == 0:
		print "NO"
	else:
		print "YES"

