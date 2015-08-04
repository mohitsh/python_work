
class Stack:
	def __init__(self):
		self.items = []
	def isEmpty(self):
		return self.items == []
	def size(self):
		return len(self.items)
	def push(self,item):
		self.items.append(item)
	def peek(self):
		return self.items[len(self.items)-1]
	def pop(self):
		return self.items.pop()


def infixTopostfix(string):
	# split the input string based on space
	inputstr = string.split()
	# array to space output
	output = []
	# stack created
	opstack = Stack()
	# dictionary created
	operator = {}
	operator["*"] = 3
	operator["/"] = 3
	operator["-"] = 2
	operator["+"] = 2
	operator["("] = 1
	check = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
	
	for i in inputstr:
		if i in check:
			output.append(i)
		elif i == "(":
			opstack.push(i)
		elif i == ")":
			top = opstack.pop()
			while top != "(":
				output.append(top)
				top = opstack.pop()
		else:
			while (not opstack.isEmpty()) and (operator[opstack.peek()]>=operator[i]):
				output.append(opstack.pop())
			opstack.push(i)
	while not opstack.isEmpty():
		output.append(opstack.pop())
	return "".join(output)

print infixTopostfix("A * B * C *")
print infixTopostfix("( A + B ) * C - ( D - E ) * ( F + G )")




	
	
