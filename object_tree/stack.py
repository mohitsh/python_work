

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
	def show(self):
		print self.items
