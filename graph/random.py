



n = int(raw_input())
m = n*2

names = []
marks = []
for i in range(m):
	data = raw_input()
	if i%2 == 0:
		names.append(str(data))
	else:
		marks.append(float(data))
	
def func1(marks,names):
	ans = []
	#marks.sort()
	mset = list(set(marks))
	#print 'mset', mset
	mset.sort()
	lastval = mset[1]
	#print 'lastval', lastval
	for i in range(len(marks)):
		if lastval == marks[i]:
			ans.append(names[i])
	return ans

kabba = func1(marks,names)
dabba = sorted(kabba)
for key in dabba:
	print key
