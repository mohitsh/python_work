

def move(p,U):
	q = []
	for i in range(len(p)):
		q.append(p[(i-U)%len(p)]*0.1 + p[(i-U-1)%len(p)]*0.8
			+ p[(i-U-2)%len(p)]*0.1)
	return q

p = [1,2,3,4,5]
print len(p)
print move(p,1)

