
def findDigits(n):
	strn = str(n)
	strnl = list(strn)
	arr1 = [int(x) for x in strnl]	
	count = 0
	for k in arr1:
		if k!=0:
			if n%k == 0:
				count = count + 1
	return count

t = int(raw_input())
arr = []
for k in range(t):
	dude = int(raw_input())
	ans = findDigits(dude)
	arr.append(ans)

for i in arr:
	print i
	
