 
# this tiny took me 3 hours
# so I am going to explain everything here


def choco(n,c,m):
	# chocolate you bought with all your money
	bought = n/c
	# keep the count of chocolates bought
	count = bought
	# as long you have chocolates to exchange
	while bought >= m:
		# this is the number you can exchange
		exchange = (bought/m)*m 
		# chocolates you get in exchange
		choco = (bought/m)
		# increase your chocolate count
		count = count + choco
		# this is the amount of chocolates left after exchanging 
		bought = bought-exchange+choco
	return count




t = int(raw_input())
for i in range(t):
	dude = raw_input().split()
	dude = [int(x) for x in dude]
	ans = choco(dude[0],dude[1],dude[2])
	print ans
