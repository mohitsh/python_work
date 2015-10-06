
def taum(arr1,arr2):
	b,w = arr1
	x,y,z = arr2
	init_sum = b*x + w*y
	#print "initially: ",init_sum
	for i in range(1,b+1):
		new_sum = (b-i)*x + (w+i)*y + i*z
		if new_sum < init_sum:
			init_sum = new_sum
			#break;
	#print "finally: ",init_sum
	for j in range(1,w+1):
		new_sum = (b+j)*x + j*z + (w-j)*y
		if new_sum < init_sum:
			init_sum = new_sum
			#break;
		
	print init_sum

t = int(raw_input())
for i in range(t):
	dude1 = raw_input().split()
	dude1 = [int(x) for x in dude1]
	dude2 = raw_input().split()
	dude2 = [int(x) for x in dude2]
	taum(dude1,dude2)
