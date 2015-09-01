

def reverse(dude):
	dudeList = [ch for ch in dude]
	ans  = []
	for i in range(len(dudeList)-1,-1,-1):
		ans.append(dudeList[i])
	print ''.join(ans)
reverse('mohit')
