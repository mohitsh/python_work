

def time_convert(n):
	
	#print n
	last = n[len(n)-1]
        status = last[len(last)-2] + last[len(last)-1]
        #print status == 'PM'
        last = (last[len(last)-4] + last[len(last)-3])

	h = int(n[0])
	m = int(n[1])
	s = int(last)
		
	#print h
	#print m
	#print last
	if status == 'AM':
		if h == 12:
			return '00' + ":" + n[1] + ":" + last 
		elif h >=1 and h<=11:
			return n[0]+":"+n[1]+":"+last

	else:	
		if h == 12:
			return str(h)+":"+n[1]+":"+last 
		else:
			return str(h+12)+":"+n[1]+":"+last

n = raw_input().split(":")
print time_convert(n)



