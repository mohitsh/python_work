
import math
def tor(a,b,c,d):

	ab = [(b[0]-a[0]),(b[1]-a[1]), (b[2]-a[2])]
	bc = [(c[0]-b[0]),(c[1]-b[1]), (c[2]-b[2])]
	cd = [(d[0]-c[0]),(d[1]-c[1]), (d[2]-c[2])]
	
	x = cross(ab,bc)
	y = cross(bc,cd)
	#print x,y
	xdoty = [x[0]*y[0],x[1]*y[1],x[2]*y[2]]
	modx = math.sqrt(x[0]**2 + x[1]**2 + x[2]**2)
	mody = math.sqrt(y[0]**2 + y[1]**2 + y[2]**2)
	#print xdoty
	#print modx
	#print mody

	cosphi = sum(xdoty)/(modx*mody)
	return round(math.acos(cosphi)*(180/math.pi),2)

	


def cross(a,b):
	c = [a[1]*b[2] - a[2]*b[1],
         	a[2]*b[0] - a[0]*b[2],
         	a[0]*b[1] - a[1]*b[0]]

    	return c


a = raw_input().split()
arra = [int(x) for x in a]
b = raw_input().split()
arrb = [int(x) for x in b]
c = raw_input().split()
arrc = [int(x) for x in c]
d = raw_input().split()
arrd = [int(x) for x in d]

print tor(arra,arrb,arrc,arrd)

