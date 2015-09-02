

def gamet(string):
	length = len(string)
	ulist = ''.join(set(string))
	countD = {}
	for i in ulist:
		countD[i] = string.count(i)
	#print ulist
	#print countD
	flag = True
	if length%2 == 0:
		for key in countD:
			if countD[key]%2 != 0:
				print 'NO'
				break
		else:
			print 'YES'
	elif length%2 != 0:
		count = 0
		for key in countD:
			if countD[key]%2 != 0:
				count = count+1
		if count > 1:
			print 'NO'
		elif count == 1:
			print 'YES'


n = raw_input()
gamet(str(n))
#gamet('aaabbbb')
#gamet('cdefghmnopqrstuvw')

