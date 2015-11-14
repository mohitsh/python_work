

p=[0.2,0.2,0.2,0.2,0.2]
world = ['green','red','red','green','green']
Z = ['red','red']
motions = [1,1]
pHit = 0.6
pMiss = 0.2

pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def sense(p,Z):
	for i in range(len(p)):
		hit = (Z == world[i])
		p[i] = (p[i]*(hit*pHit + (1-hit)*pMiss))
	dude_sum = sum(p)
	#print dude_sum
	for i in range(len(p)):
		p[i] = p[i]/dude_sum
	return p


def move(p,U):
	q = [0]*len(p)
	for i in range(len(p)):
		q[(i+U)%len(p)] = q[(i+U)%len(p)]+p[i]*pExact
		q[(i+U-1)%len(p)] = q[(i+U-1)%len(p)]+p[i]*pUndershoot
		q[(i+U+1)%len(p)] = q[(i+U+1)%len(p)]+p[i]*pOvershoot
	return q

p = [0.2,0.2,0.2,0.2,0.2]
print p

for k in range(len(Z)):
	p = sense(p,Z[k])
	p = move(p,motions[k])

print p

"""
for i in range(1000):
	p = move(p,1)
print p 
print sense(p,Z)
"""	

