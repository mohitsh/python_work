
def intToStr(num):
	ints = []
	intstring  = '0123456789'	
	while num > 0:
		
		ints.insert(0,intstring[num%10])
		
		num = num/10
	return "".join(ints)

print intToStr(769)

# recursive version

def RecurIntToStr(num, base):
	intTostring = '0123456789ABCDEF'
	if num < base:
		return intTostring[num]
	else:
		return RecurIntToStr(num/base, base) + intTostring[num%base] 

print RecurIntToStr(769,10)
print RecurIntToStr(1453,16)
