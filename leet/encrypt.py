
import math
def encrypt(s):
	s1 = s.replace(" ","")
	l = len(s1)
	row = math.floor(math.sqrt(l))
	col = math.ceil(math.sqrt(l))
	#print "row", row
	#print "col",col
	ans = []
	for i in range(int(row)):
		
		ans.append(s1[i*int(col):i*int(col)+int(col)])
		#print s1[i*int(col):i*int(col)+int(col)]
	print ans
	dude = []
	lastLen = len(ans[-1])
	for i in range(0,lastLen):
		dabba = ""
		for j in range(int(row)):
			dabba = dabba+ans[j][i]
		dude.append(str(dabba))
	
	for i in range(lastLen,int(row)+1):
		dabba = ""
		for j in range(int(row)-1):
			dabba = dabba + ans[j][i]
		dude.append(str(dabba))
	
	daddu = ""
	for k in dude:
		daddu = daddu + k + " "
	print daddu
		

s = raw_input()
encrypt(str(s))



