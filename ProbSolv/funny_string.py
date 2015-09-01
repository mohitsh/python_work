

def funny_str(dude):
	dudeList = [ch for ch in dude]
	revstr = []
	for i in range(len(dudeList)-1,-1,-1):
		revstr.append(dudeList[i])
	duderev = ''.join(revstr)
	
	flag = True
	index = 1
	while i < len(dude) and flag:
		if abs(ord(dude[i])-ord(dude[i-1])) != abs(ord(duderev[i])-ord(duderev[i-1])):
			flag = False
		i = i +1
	if flag == True:
		return 'Funny'
	else:
		return 'Not Funny'



n = int(raw_input())
arr = []
for i in range(0,n):
	a = raw_input()
	arr.append(str(a))

for j in arr:
	print funny_str(j)
