'''
in this deque example I have considered position 0 to be FRONT 
in other deque exmaples like Palindrome checker last element has
been considered as front. 
Usually first element is considered rear and last one is considered 
front.
I have to manipulate 0 twice to make this code compatible with 0 as 
rear and last as Front 
so no worries!

'''

class Deque:
	def __init__(self):
		self.items = []
	def size(self):
		return len(self.items)
	def isEmpty(self):
		return self.items == []
	def addFront(self,item):	
		self.items.insert(0,item)
	def addRear(self,item):
		self.items.append(item)
	def removeFront(self):
		return self.items.pop(0)
	def removeRear(self):
		return self.items.pop()
	def show(self):
		print self.items

d = Deque()
print d.isEmpty()
print d.size()
d.addFront(1)
d.addFront(2)
d.addFront(3)
print d.isEmpty()
print d.size()
d.show()
d.addRear(10)
d.addRear(11)
d.addRear(12)
d.show()
print d.removeFront()
print d.removeFront()
print d.removeFront()
d.show()
print d.removeRear()
print d.removeRear()
print d.removeRear()
d.show()
