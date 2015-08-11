
def getminstep(n):
	dp = [0]*(n+1)
	print dp
	dp[1] = 0
	print dp
	
	for i in range(2,n+1):
		dp[i] = 1+dp[i-1]
		print i,'-->',dp[i]
		if i%2 == 0:
			if dp[i] < 1+dp[i/2]:
				dp[i] = dp[i]
			else:
				dp[i] = 1+dp[i/2]
		if i%3 == 0:
			if dp[i] < 1+dp[i/3]:
				dp[i] = dp[i]
			else:
				dp[i] = dp[i/3] + 1
	print dp
	return dp[n]



#print getminstep(1)
print getminstep(4)
#print getminstep(7)
#print getminstep(10)
#print getminstep(20)
#print getminstep(30)
#print getminstep(337)
