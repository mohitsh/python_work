
def getminstep(n):

	memo = [-1]*(n+1)
	if n==1:
		return 0
	if memo[n] != -1:
		return memo[n]
	r = 1 + getminstep(n-1)
	if (n%2 == 0):
		if r < (1+getminstep(n/2)):
			return r
		else:
			return (1+getminstep(n/2))

	if (n%3 == 0):
		if r < (1+getminstep(n/3)):
			return r
		else:
			return (1+getminstep(n/3))

	memo[n] = r
	return r
print getminstep(10)
print getminstep(20)
print getminstep(30)
