
def grid(mat1,mat2):
	for line in mat2:
		if line in mat1:
			ind = mat1.index(line)
		


t = int(raw_input())
for i in range(t):
	dude = raw_input().split()
	dude = [int(x) for x in dude]
	R = dude[0]
	C = dude[1]
	matrix1 = []
	for k in range(R):
		dude1 = raw_input()
		matrix1.append(dude1)
	dude2 = raw_input().split()
	dude2 = [int(x) for x in dude2]
	r = dude2[0]
	c = dude2[1]
	matrix2 = []
	for i in range(r):
		dude3 = raw_input()
		matrix2.append(dude3)
	print matrix1
	print matrix2
	
