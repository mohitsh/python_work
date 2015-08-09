

class Stack:
	def __init__(self):
		self.items  = []
	def isEmpty(self):
		return self.items == []
	def size(self):
		return len(self.items)
	def push(self,item):
		self.items.append(item)
	def pop(self):
		return self.items.pop()
	def show(self):
		print self.items
'''
wing = Stack()
wing.push('jain')
wing.push('kutta')
wing.push('bohra')
wing.push('mittal')
wing.show()
print wing.pop()
print wing.isEmpty()
print wing.pop()
print wing.isEmpty()
print wing.pop()
print wing.isEmpty()
print wing.pop()
print wing.isEmpty()
'''

rstack = Stack()
def intToStr(num,base):

	convertString = '0123456789ABCDEF'
	while num > 0:
	
		if num < base:
			rstack.push(convertString[num])
	
		else:
			rstack.push(convertString[num%base])
		num = num//base
	res = ''
	while not rstack.isEmpty():
		res = res + str(rstack.pop())
	return res
	

print intToStr(1234,10)
print intToStr(1234,16)

