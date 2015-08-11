class Node:
	def __init__(self,item):
		self.data = item 
		self.next = None
	def getData(self):
		return self.data
	def getNext(self):
		return self.next
	def setNext(self, item):
		self.next = item
	def setData(self, item):
		self.data = item

class OrderedLinkedList:
	def __init__(self):
		self.head = None
	def isEmpty(self):
		return self.head == None
	def size(self):
		current = self.head
		count = 0
		while current != None:
			count = count + 1
			current = current.getNext()
		return count
	# everything is same as in unordered list case 
	# one more condition is added to check whether the item in linked list
	# is greater than the item we are searching for 
	# if it is: then we should stop the search
	def search(self,item):
		current = self.head
		found = False
		while not found and current != None and current.getData() <= item:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()
		return found
	
	# same condition here too. check for item in the linked list whether
	# it is greater of less than the item we are searching for 
	# in case item in list is greater than the item we are searching for 
	# stop and insert the item there
	def add(self, item):
		newNode = Node(item)
		current = self.head
		previous = None
		while current != None and current.getData() <= item:
			previous = current 
			current = current.getNext()
		
		if previous == None:
			newNode.setNext(self.head)
			self.head = newNode
			
		else:
			newNode.setNext(current)
			previous.setNext(newNode)
	


mylist = OrderedLinkedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print 'mylist size ---> ', mylist.size()
print 'search for 93 ---> ', mylist.search(93)
print 'search for 100 --> ', mylist.search(100)

'''
mylist = OrderedLinkedList()
print 'is the list empty ---> ', mylist.isEmpty()
print 'mylist length ---> ', mylist.size()
'''
