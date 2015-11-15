
p = 	 [[0.05,0.05,0.05,0.05,0.05],
          [0.05,0.05,0.05,0.05,0.05],
          [0.05,0.05,0.05,0.05,0.05],
          [0.05,0.05,0.05,0.05,0.05]]

colors = [['R','G','G','R','R'],
          ['R','R','G','R','R'],
          ['R','R','G','G','R'],
          ['R','R','R','R','R']]

measurements = ['G','G','G','G','G']
#motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]
motions = [[0,0],[0,1],[1,0]]

pHit = 0.7
pMiss = 0.3

pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def sense(p,measurements):
	q = []
	for subp in range(len(p)):
		for j in range(len(p[subp])): 
			hit = (measurements == colors[subp][j])
			p[subp][j] = (p[subp][j]*(hit*pHit + (1-hit)*pMiss))
		dude_sum = sum(p[subp])
		#print dude_sum
		q.append(p[subp])
	s = 0
	for i in q:
		s = s + sum(i)
	for i in range(len(q)):
		for j in range(len(q[i])):
			q[i][j] = q[i][j]/s
	return q


def move(p,U):
	if U == [0,0]:
		flag = 1
		U = 0
	elif U == [0,1]:
		flag = 1
		U = 1
	elif U == [0,-1]:
		flag = 1
		U = -1
	elif U == [1,0]:
		flag = 0
		U = 1
	elif U == [-1,0]:
		flag = 0
		U = -1
	
	if flag == 1:
		print "flag is 1"
		q = []
		for i in range(len(p)):
			q1 = [0]*len(p[i])
			for j in range(len(p[i])):
				q1[(j+U)%len(p[i])] = q1[(j+U)%len(p[i])]+p[i][j]*pExact
				q1[(j+U-1)%len(p[i])] = q1[(j+U-1)%len(p[i])]+p[i][j]*pUndershoot
				q1[(j+U+1)%len(p[i])] = q1[(j+U+1)%len(p[i])]+p[i][j]*pOvershoot
			q.append(q1)
		#return q

	if flag == 0:
		print "flag is 0"
		print "U is: ", U
		rows = len(p)
		cols = len(p[0])
		#print rows
		#print cols
		q = [[0]*cols]*rows
		#for k in q:
		#	print k
		for j in range(cols):
			for i in range(rows):
				print "i",i,"j",j
				print q
                                q[(i+U)%rows][j]  = q[(i+U)%rows][j] + p[i][j]*pExact
                                q[(i+U-1)%rows][j] = q[(i+U-1)%rows][j]  + p[i][j]*pUndershoot
                                q[(i+U+1)%rows][j]  = q[(i+U+1)%rows][j]  + p[i][j]*pOvershoot
		#return q
	return q
	
"""
p = sense(p,'G')
for k in p:
	print k
"""
p = move(p,[1,0])
#p = move(p,[1,0])
#p = move(p,[1,0])

print 'after movement:'
for k in p:
	print k

"""
for k in range(len(measurements)):
	p = sense(p,measurements[k])
	p = move(p,motions[k])

print p
"""
"""
for i in range(1000):
	p = move(p,1)
print p 
print sense(p,Z)
"""	

