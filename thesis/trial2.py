
p = [[.1,.1],[.1,.1],[.1,.1],[.1,.1],[.1,.1]]
colors = [['R', 'G'],
          ['R', 'R'],
          ['G', 'R'],
          ['R', 'G'],
          ['G', 'G']]
measurements = ['R', 'R', 'G', 'G', 'G', 'R']
motions = [[0, 0], [-1, 0], [0, 1], [0, -1], [0, 1], [1, 0]]

pHit = 0.99
pMiss = 1- pHit

p_move = 0.97

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
		#print "flag is 1"
		q = []
		for i in range(len(p)):
			q1 = [0]*len(p[i])
			for j in range(len(p[i])):
				q1[(j+U)%len(p[i])] = q1[(j+U)%len(p[i])]+p[i][j]*p_move
				#q1[(j+U-1)%len(p[i])] = q1[(j+U-1)%len(p[i])]+p[i][j]*(1-p_move)
				q1[j] = q1[j]+p[i][j]*(1-p_move)
				#q1[(j+U+1)%len(p[i])] = q1[(j+U+1)%len(p[i])]+p[i][j]*pOvershoot
			q.append(q1)

	if flag == 0:
		rows = len(p)
		cols = len(p[0])
		q = [[0]*cols]*rows
		for i in range(rows):
			q[(i+U)%rows] = [sum(x) for x in zip(q[(i+U)%rows],[k*p_move for k in p[i]])]
			q[i] = [sum(x) for x in zip(q[i],[k*(1-p_move) for k in p[i]])]
			#q[(i+U-1)%rows] =[sum(x) for x in zip(q[(i+U-1)%rows],[k*(1-p_move) for k in p[i]])]
			#q[(i+U+1)%rows] = [sum(x) for x in zip(q[(i+U+1)%rows],[k*pOvershoot for k in p[i]])]		
	return q
	
for k in range(len(measurements)):
	p = move(p,motions[k])
	p = sense(p,measurements[k])

for k in p:
	print k

