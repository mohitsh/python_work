

def count(alist,word,n):
	arr = []
	for i in range(100):
		count = 0
		for j in range(n):
			if i == alist[j]:
				count = count + 1
		arr.insert(i,count)

	#print arr
	#ans = []
	#count = 0
	#for m in range(len(arr)):
	#	count = count + arr[m]
	#	ans.append(count)
	#print ' '.join(str(x) for x in ans)
	ans = []
	for k in range(len(arr)):
		for m in range(arr[k]):
			ans.append(k)
	print ' '.join(str(j) for j in ans)	
	print 'soulution part -->'
	print word
	print ans
		

n = int(raw_input())
num = []
word = {}
for i in range(n):
	a = raw_input().split()
	num.append(int(a[0]))	
	word[int(a[0])] = a[1]

#print num
#print word
#alist = [int(x) for x in a]
count(num,word,n) 
