# this code is not working properly need some improvement.

class Stack:
	def __init__(self):
		self.items = []
	def isEmpty(self):
		return self.items == []
	def size(self):
		return len(self.items)
	def push(self,item):
		self.items.append(item)
	def pop(self):
		return self.items.pop()
	def peek(self):
		return self.items[len(self.items)-1]
	def show(self):
		print self.items

def infixToPrefix(string):
	inputstr = string.split()
	output = []
	opstack = Stack()
	operator = {}
	operator["*"] = 3
	operator["/"] = 3
	operator["-"] = 2
	operator["+"] = 2
	operator["("] = 1
	check = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
	for i in inputstr:
		if i in check:
			output.insert(0,i)
		elif i == "(":
			output.insert(0,i)
		elif i == ")":
			top = opstack.pop()
			while top != "(":
				output.insert(0,top)
				top = output.pop()
		else:
			while (not opstack.isEmpty()) and (operator[opstack.peek()]>=operator[i]):
				output.insert(0,opstack.pop())
			opstack.push(i)
	while not opstack.isEmpty():
		output.insert(0,opstack.pop())
	return "".join(output)

print infixToPrefix("( A + B ) * C - ( D - E ) * ( F + G )")

			
	
