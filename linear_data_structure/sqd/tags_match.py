
from stack1 import ArrayStack

def is_matched(raw):
	
	S = ArrayStack()
	j = raw.find('<')
	while j != -1:
		k = raw.find('>',j+1)
		if k == -1:
			return False
		tag = raw[j+1:k]
		
		if not tag.startswith('/'):
			S.push(tag)
		else:
			if S.is_empty():
				return False
			if tag[1:] != S.pop():
				return False
		j = raw.find('<',k+1)
	return S.is_empty()
raw = '<html> this is fucking sparta and this is dude. </html><body> this is fucked up > </body>'
print is_matched(raw)
raw = '<html> this is fucing sparta and fucked up'
print is_matched(raw)
		
		
