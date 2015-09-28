

def move(p, U):
    #
    #ADD CODE HERE
    #
    	n = len(p)
	q = []
 	for i in range(len(p)):
		q.append(p[(i-U)%len(p)])
    	return q

p = [1,2,3,4,5,6]
print p
print move(p, 1)
