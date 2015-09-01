
def pangram(string):
	check = 'abcdefghijklmnopqrstuvwxyz'
	#print check
	string = string.lower().replace(" ","")
	#print string
	flag = True
	i = 0
	while i<len(check) and flag:
		#print string[i]
		if check[i] not in string:
			flag = False
		i = i +1
	if flag == True:
		print 'pangram'
	else:
		print 'not pangram'

n = raw_input()
pangram(str(n))

#pangram('We promptly judged antique ivory buckles for the next prize')
