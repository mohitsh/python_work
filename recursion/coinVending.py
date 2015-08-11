
def vendor(coinValue, amt):
	minCoins = amt
	if amt in coinValue:
		print 'returning 1'
		return 1
	else:
		for i in [c for c in coinValue if c <= amt]:
			print 'amt is ', amt
			print 'value of i ', i
			numCoins = 1 + vendor(coinValue, amt-i)
			print 'number of coins ', numCoins
			if numCoins < minCoins:
				minCoins = numCoins
	
	return minCoins
vendor([2,4],8)
