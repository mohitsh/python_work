class Node:
	def __init__(self,initdata):
		self.data = initdata
		self.next = None

	def getData(self):
		return self.data
	def getNext(self):
		return self.next
	def setData(self, newData):
		self.data = newdata
	def setNext(self,nextData):
		self.next = nextData


class UnorderedList:
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
	def search(self,item):
		current = self.head
		match = False
		while current != None and not match:
			if item == current.getData():
				match = True
			else:
				current = current.getNext()
		return match
	
	def remove(self,item):
		current = self.head
		previous = None
		match = False
		while not match:
			if current.getData() == item:
				match = True
			else:
				previous = current
				current = current.getNext()
		if previous == None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())
	# this append method is not yet finished will finish soon
	def append(self,item):
		current = self.head
		previous = None
		while current != None:
			previous = current
			current = current.getNext()
		previous.setNext(item)


node = Node(11)
mylist = UnorderedList()
mylist.add(12)
mylist.add(13)
mylist.add(14)
mylist.add(15)
mylist.add(16)
print mylist.search(20)
print mylist.search(13)
mylist.remove(16)
mylist.remove(15)
mylist.remove(14)
print mylist.search(14)
print mylist.search(15)
print mylist.search(101)
print mylist.search(102)
mylist.append(101)
mylist.append(102)
print mylist.search(101)
print mylist.search(102)

