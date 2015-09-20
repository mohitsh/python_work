

def hash_code(s):
	mask = (1<<32) - 1
	h = 0
		
	for char in s:
		h = (h << 5 & mask) | (h >> 27)
		h += ord(char)

	return h

print hash_code("mohit")


def hash_code1(s):
	mask = (1<<32) -1
	h = 0
	
	for char in s:
		h = (h<<5 & mask) | (h >> 27)
		h += ord(char)

	return h

print hash_code1("mohit")
print hash_code1("shukla")
