

def beast(n):
	if n < 3:
		return -1
	
	else:
		for noFive in range(n):
			noThree = (n-5*noFive)
			if noThree == 0:
				dude = makeNum(noThree,noFive*5)
				return dude
			elif noThree < 0:
				return -1
			else:
				if noThree%3 == 0:
					dude = makeNum(noThree,noFive*5)
					return dude
				


def makeNum(NoOfFive,NoOfThree):
	arr1 = [5]*NoOfFive + [3]*NoOfThree
	arr2 = [str(x) for x in arr1]
	ans1 = ''.join(arr2)
	ans = int(ans1)
	return ans



t = int(raw_input())
arr = []
for i in range(t):
	dude = int(raw_input())
	ans = beast(dude)
	arr.append(ans)
for i in arr:
	print i


					
					
