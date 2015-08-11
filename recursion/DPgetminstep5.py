

def getminstep(n):
	ans = [0]*(n+1)
	
	for i in range(2,n+1):
		ans[i] = 1 + ans[i-1]
		if i%2 == 0:
			if ans[i] < 1+ans[i/2]:
				ans[i] = ans[i]
			else:
				ans[i] = 1 + ans[i/2] 
		if i%3 == 0:
			if ans[i] < 1+ans[i/3]:
				ans[i] = ans[i]
			else:
				ans[i] = 1 + ans[i/3]
		if i%5 == 0:
			if ans[i] < 1+ans[i/5]:
				ans[i] = ans[i]
			else:
				ans[i] = 1+ans[i/5]

	return ans[n]

print getminstep(1)
print getminstep(5)
print getminstep(7)
print getminstep(10)
print getminstep(20)
