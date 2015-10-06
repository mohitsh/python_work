
def choco(n,c,m):
	bought = n/c
	count = bought
	while bought >= m:
		exchange = (bought/m)*m 
		choco = (bought/m)
		count = count + choco
		bought = bought-exchange+choco
	return count




t = int(raw_input())
for i in range(t):
	dude = raw_input().split()
	dude = [int(x) for x in dude]
	ans = choco(dude[0],dude[1],dude[2])
	print ans
