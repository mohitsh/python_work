


def minion(string):
	vowel = 'aeiou'
	vowelInd = []
	for i in vowel:
		if i in string:
			vowelInd.append(string.index(i))

	
	ans = []
	for j in vowelInd:
		for k in range(j+1, len(string)):
			ans.append(string[j:k])

	print ans

minion("banana")
