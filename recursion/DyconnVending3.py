

def vending(coinList, change, store):
	mincoin = change
	if change in coinList:
		store[change] = 1
		return 1
	elif store[change] > 0:
		return store[change]
	else:
		for i in [c for c in coinList if c<=change]:
			numCoin = 1 + vending(coinList, change -i, store)
			if numCoin < mincoin:
				mincoin = numCoin
				
				store[change] = mincoin
	return mincoin


print vending([1,5,10,25],63,[0]*64)



