class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

	def getData(self):
		return self.data
	def getNext(self):
		return self.next
	def setData(self,item):
		self.data = item
	def setNext(self,item):
		self.next = item

class unorderedList:
	def __init__(self):
		self.head = None
	def isEmpty(self):
		return self.head == None
	def add(self,item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp
	def size(self):
		current = self.head
		count = 0
		while current != None:
			count = count + 1		
			current = current.getNext()
		return count
	def search(self, item):
		current = self.head
		found = False
		while current != None and not found:
			if item == current.getData():
				found = True
			else:
				current = current.getNext()
		return found
	def remove(self,item):
		current = self.head
		previous = None
		found = False
		while not found:
			if current.getData() == item:
				found = True
			else:
				previous = current
				current = current.getNext()
		
		if previous == None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getnext())
	def append(self,item):
		newNode = Node(item)
		current = self.head
		previous = None
		while current != None:
			previous = current
			current = current.getNext()
			
		if previous == None:
			self.head = newNode
		else:
			previous.setNext(newNode)


newlist = unorderedList()
newlist.add(1)
newlist.add(2)
newlist.add(3)
print newlist.size()
print newlist.search(1)
print newlist.search(2)
print newlist.search(21)
newlist.remove(3)
newlist.remove(2)
newlist.remove(1)
print newlist.size()
newlist.append(101)
print newlist.search(101)
print newlist.size()
newlist.append(102)
print newlist.search(102)
print newlist.size()
newlist.append(103)
print newlist.search(103)
print newlist.size()
newlist.append(10001)
print newlist.search(10001)
print newlist.size()
