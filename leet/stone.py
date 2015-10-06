
def stones(n,a,b):
	arr = [0]
	for i in range(n-1):
		#print "Array: ", arr
		arr = next_step(arr,a,b)
		#print "Post Array: ", arr

	arr.sort()
	return arr

def next_step(arr,a,b):
	ans = []
	for i in arr:
		if (i+a) not in ans:
			ans.append(i+a)
		if (i+b) not in ans:
			ans.append(i+b)
	return ans


t = int(raw_input())
for i in range(t):
	n = int(raw_input())
	a = int(raw_input())
	b = int(raw_input())
	ans = stones(n,a,b)
	dude = ""
	for k in ans:
		dude = dude + str(k) + " "
	print dude
