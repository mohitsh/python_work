

def count(alist,n):
	arr = []
	for i in range(100):
		count = 0
		for j in range(n):
			if i == alist[j]:
				count = count + 1
		arr.insert(i,count)
	#arr.sort()
	#ans = []
	#for k in arr:
	#	ans.append(alist[k])
	#arr.sort()
	#print ' '.join(str(z) for z in arr)
	print arr
	ans = []
	for k in range(len(arr)):
		for m in range(arr[k]):
			ans.append(k)
	print ' '.join(str(j) for j in ans)	
		

n = int(raw_input())
a = raw_input().split()
alist = [int(x) for x in a]
count(alist,n) 
