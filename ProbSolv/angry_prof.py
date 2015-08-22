

def angry_prof(n,k,arrivalT):
	count = 0
	for i in range(n):
		if arrivalT[i] <= 0:
			count = count + 1
	if count >= k:
		return "NO"
	else:
		return "YES"


t = int(raw_input())
for i in range(t):
	n,k = raw_input().split()
	arrivalT = raw_input().split()
	n,k = int(n),int(k)
	arrivalT = [int(x) for x in arrivalT]
	print angry_prof(n,k,arrivalT)
	
	#print 't-->',t
	#print 'n-->', n
	#print 'k-->', k
	#print 'arrivalT-->', arrivalT
	
