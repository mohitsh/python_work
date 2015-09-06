

def incrypt(string,r):
	alpha = 'abcdefghijklmnopqrstuvwxyz'
	strlist = list(string)
	for i in range(len(strlist)):
		if strlist[i] == ' ':
			pass
		else:
			index = alpha.index(strlist[i])
			newindex = (index+r)%26
			strlist[i] = alpha[newindex]
	return ''.join(strlist)



def decrypt(string,r):
	alpha = 'abcdefghijklmnopqrstuvwxyz'
	strlist = list(string)
	for i in range(len(strlist)):
		if strlist[i] == ' ':
			pass
		else:
			index = alpha.index(strlist[i])
			newindex = (index-r)%26
			#print newindex
			#print alpha[newindex]
			strlist[i] = alpha[newindex]
	return ''.join(strlist)

print incrypt('abcdef',1)
print decrypt(incrypt('abcdef',1),1)
print incrypt('mohit',5)
print decrypt(incrypt('mohit',5),5)		
print incrypt('deepak kumar dalakoti',5)
print decrypt(incrypt('deepak kumar dalakoti',5),5)
