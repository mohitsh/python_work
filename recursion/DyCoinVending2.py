
def dynamicVendor(coinValue, change, known):
	mincoins = change
	if change in coinValue:
		known[change] = 1
		return 1
	elif known[change] > 0:
		return known[change]
		
	else:
		for i in [c for c in coinValue if c <= change]:
			numCoins = 1 + dynamicVendor(coinValue, change-i, known)
			if numCoins < mincoins:
				mincoins = numCoins
				known[change] = mincoins
	return mincoins

print dynamicVendor([1,5,10,25],63,[0]*64)
