
def choco(n,c,m):
	bought = n/c
	if bought >= m:
		wrapper = (bought/m)*m		
	else: 
		return bought
	left = bought - wrapper

	while left >0:
		exchanged = wrapper/m
		left = left + exchanged
		bought = bought  + exchanged
		if bought >= m:
			wrapper = (bought/m)*m
		left=bought-wrapper
	return bought
		




t = int(raw_input())
for i in range(t):
	dude = raw_input().split()
	dude = [int(x) for x in dude]
	ans = choco(dude[0],dude[1],dude[2])
	print ans
