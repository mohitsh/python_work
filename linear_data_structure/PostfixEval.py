class Stack:
	def __init__(self):
		self.items = []
	def isEmpty(self):
		return self.items == []
	def size(self):
		return (len(self.items))
	def push(self,item):
		self.items.append(item)
	def peek(self):
		return self.items[len(self.items)-1]
	def pop(self):
		return self.items.pop()

def postfixEval(string):
	inputstr = string.split()
	operandStack = Stack()
	operand = '0123456789'
	operator = '-+*/'
	for i in inputstr:
		if i in operand:
			operandStack.push(int(i))
		elif i in operator:
			second = operandStack.pop()
			first = operandStack.pop()
			ans = calc(first,second,i)
			operandStack.push(ans)
	return operandStack.pop()

def calc(first,second,i):
	if i == '+':
		return first + second
	elif i == '-':
		return first - second
	elif i == '/':
		return first/second
	elif i == '*':
		return first*second
print postfixEval('7 8 + 3 2 + /')
