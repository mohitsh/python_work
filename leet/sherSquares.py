
import math
def sherSquares(a,b):
	count = 0
	for k in range(a,b+1):
		original = math.sqrt(k)
		deformed = math.floor(original)
		if original == deformed:
			count=count + 1
	return count

t = int(raw_input())
arr = []
for i in range(t):
	dude = raw_input().split()
	dude = [int(x) for x in dude]
	ans = sherSquares(dude[0],dude[1])
	print ans


