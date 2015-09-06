

from stack1 import ArrayStack

def delim(string):
	s = ArrayStack()
	openb = list('[{(')
	#print openb
	closeb = list(')}]')
	#print closeb
	strlist = list(string)
	#print strlist
	for char in strlist:
		
		if char in openb:
			print char
			s.push(char)
		elif char in closeb:
			print char
			oind = openb.index(s.top())
			cind = closeb.index(char)
			if cind == len(openb)-1-oind:
				print s.pop()
	if len(s) == 0:
		return True
	else:
		return False


print delim('[{()}]')
print delim('[{)]')
