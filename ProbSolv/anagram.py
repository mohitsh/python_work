



def anagram(string):
	mid = len(string)/2
	if len(string)%2 != 0:
		return -1
	else:
		str1 = string[:mid]
		str2 = string[mid:]
		count = 0
		for i in range(len(str1)):
			if str1[i] not in str2:
				count = count + 1
		return count
	

n = int(raw_input())
for i in range(n):
	a = raw_input()
	print anagram(str(a))
