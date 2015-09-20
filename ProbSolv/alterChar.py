

def altchar(string):
	count = 0
	ans = []
	for i in range(1,len(string)):
		if string[i-1] != string[i]:
			count = count + 1
			ans.append(string[i-1])
			ans.append(string[i])
	
	#print len(string)-1
	#print count
	print len(string)-1-count
	#print ''.join(ans)

n = int(raw_input())
for i in range(n):
	altchar(str(raw_input()))
