
def time(h,m):
	
	hour = {}
	hour[1] = "one"
        hour[2] = "two"
        hour[3] = "three"
        hour[4] = "four"
        hour[5] = "five"
        hour[6] = "six"
        hour[7] = "seven"
        hour[8] = "eight"
        hour[9] = "nine"
        hour[10] = "ten"
        hour[11] = "eleven"
        hour[12] = "twelve"
	
	#for key in hour:
	#	print key, "->", hour.get(key)

	minute = {
		0:"o' clock",1:"one minute",2:"two minutes",3:"three minutes",
		4:"four minutes",5:"five minutes",6:"six minutes",7:"seven minutes",
		8:"eight minutes",9:"nine minutes",10:"ten minutes",
		11:"eleven minutes",12:"twelve minutes",13:"thirteen minutes",
		14:"fourteen minutes",15:"fifteen minutes",16:"sixteen minutes",
		17:"seventeen minutes",18:"eighteen minutes",19:"nineteen minutes",
		20:"twenty minutes",21:"twenty minutes",22:"twenty two minutes",
		23:"twenty three minutes",24:"twenty four minutes", 
		25:"twenty five minutes",
		26:"twenty six minutes",27:"twenty seven minutes",
		28:"twenty eight minutes",
		29:"twenty nine minutes",30:"half past"
		}
	#for key in minute:
	#	print key, "->", minute.get(key)	
	
	if (m==0):
		h_dude = hour.get(h)	
		m_dude = minute.get(m)
		print h_dude,m_dude
	elif (30>m>0):
		if (m==15):
			h_dude = hour.get(h)
			print "quarter past",h_dude
		else:
			h_dude = hour.get(h)
			m_dude = minute.get(m)
			print m_dude,"past",h_dude
	elif (m==30):
		h_dude = hour.get(h)
		print "half past",h_dude
	elif (59>=m>30):
		if (m==45):
			h_dude = hour.get(h+1)
			print "quarter to",h_dude
		else:
			h_dude = hour.get(h+1)
			m_dude = minute.get(60-m)
			print m_dude,"to",h_dude


h = int(raw_input())
m = int(raw_input())
time(h,m)
