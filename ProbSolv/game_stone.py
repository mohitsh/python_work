

def gamestone(arr,n):
	ans = []
	for i in range(n):
		ans.append(''.join(set(arr[i])))
	#print ans
	#for ch in ans
	anschar = ''.join(ans)
	ansdict = {}
	for ch in anschar:
		ansdict[ch] = anschar.count(ch)
	dude = []
	for key in ansdict:
		if ansdict[key] == n:
			dude.append(key)
	print len(dude)
	#print dude
	#print ''.join(dude)	

n = int(raw_input())
arr = []
for i in range(n):
	a = raw_input()
	arr.append(str(a))
	
gamestone(arr,n)
#gamestone(['abcdde', 'baccd', 'eeabg'],3)

