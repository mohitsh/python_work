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


def infixTopostfix(infix):
	opstack = Stack()
	output = []
	operator = {}
	operator["*"] = 3
	operator["/"] = 3
	operator["+"] = 2
	operator["-"] = 2
	operator["("] = 1
	inputexp = infix.split()

	for i in inputexp:
		if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or i in "0123456789":
			output.append(i)
		elif i == "(":
			opstack.push(i)
		elif i == ")":
			top = opstack.pop()
			while top != "(":
				postfix.append(top)
				top = opstack.pop()
		else:
			while (not opstack.isEmpty()) and (operator[opstack.peek()]>=operator[i]):
				output.append(opstack.pop())
			opstack.push(i)
	while not opstack.isEmpty():
		output.append(opstack.pop())
	return " ".join(output)

print infixTopostfix("A * B * C * C")
				
