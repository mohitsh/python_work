class Node:
	def __init__(self,item):
		self.data = item
		self.next = None
	def getData(self):
		return self.data
	def getNext(self):
		return self.next
	def setData(self,item):
		self.data = item
	def setNext(self,item):
		self.next = item
	def show(self):
		print self.data
'''
temp = Node(11)
temp.show()
'''

class linked_list:
	# make an empty list 
	# this list has only one head and that points to None
	def __init__(self):
		# here head is a reference that points to a Node
		# here in this case Nond is the node
		# so an empty list contains nothing but just a 
		# reference to some Node
		
		self.head = None
	
	# just reassuring that head is set to None 
	def isEmpty(self):
		return self.head == None
	
	def add(self,item):
		newNode = Node(item)
		newNode.setNext(self.head)
		self.head = newNode
	def size(self):
		# current gets the reference to the first node
		current = self.head
		count = 0
		while current != None:
			# increase the count
			count = count + 1
			# now the current poits to next node
			current = current.getNext()
		return count
	def search(self,item):
		current = self.head
		found = False
		while current != None and not found:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()
		return found
	# in remove function we assume that 
	# item that is being removed is present in 
	# the list
	
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
			previous.setNext(current.getNext())

	def append(self,item):
		newNode = Node(item)
		current = self.head
		previous = None
		# this while loop makes sure that your current 
		# reaches the end of lineked list 
		# at the end of list current -> None and 
		# previous -> last element
		while current != None:
			# this step is very important 
			# DO NOT forget to update previous
			# otherwise size will give you wrong result
			previous = current
			current = current.getNext()
		# now I know that previous poits at the last element
		# so newNode as next Node for previous token 
		previous.setNext(newNode)
	
	def pop(self):
		# three tokens are used current and previous are
		# just as before
		# 'beforePrev' is added to take care of the element
		# just before the last element
		current = self.head
		previous = None
		beforePrev = None
		# as usual current points to the end of lined list
		# that is None previous points the last element of the
		# list and beforePrev points to the second last element
		# current -> None
		# previous -> lastElement
		# beforePrev -> second last element
		while current != None:
			beforePrev = previous
			previous = current 
			current = current.getNext()
		beforePrev.setNext(None)
		return previous.getData()

	def insert(self,index,item):
		newNode = Node(item)
		current = self.head
		previous = None
		count = 0
		while count != index:
			previous = current 
			current = current.getNext()
			count = count + 1
		# now current is at the position where newNode
		# should be inserted 
		# so redirect previous towards the newNode and
		# redirect newNode to current Node
		newNode.setNext(current)
		previous.setNext(newNode)
		
	def index(self,item):
		current = self.head
		count = 0
		while current.getData() != item:
			current = current.getNext()
			count = count + 1	
		return count 	
	
mylist = linked_list()
print 'list size ---> ', mylist.size()
print 'isEmpty ---> ',mylist.isEmpty()

mylist.add(1)
mylist.add('dalla')
mylist.add('kutta')
mylist.add(2)

print 'list size ---> ', mylist.size()
print 'isEmpty ---> ', mylist.isEmpty()

print 'search for dalla ........ ', mylist.search('dalla')
print 'search for kutta ........ ', mylist.search('kutta')
print 'search for 101 ........ ', mylist.search(101)
print 'search for 102 ........ ', mylist.search(102)

mylist.remove('dalla')
print 'search for dalla after removing ........ ', mylist.search('dalla')
mylist.remove(1)
print 'search for 1 after removing ....... ', mylist.search(1)

print 'list size ---> ', mylist.size()
print 'isEmpty ---> ', mylist.isEmpty()

mylist.append(11435)
print 'searching for 11435 ........ ', mylist.search(11435)
print 'list size ---> ', mylist.size()

mylist.append(11449)
print 'searching for 11449 ........ ', mylist.search(11449)
print 'list size ---> ', mylist.size()

mylist.append('tapan')
print 'searching for tapan ....... ', mylist.search('tapan')
print 'list size ---> ', mylist.size()

mylist.append('varun')
print 'searching for varun ....... ', mylist.search('varun')
print 'list size ---> ', mylist.size()
print 'popping varun out ---> ', mylist.pop()
print 'list size ---> ', mylist.size()

mylist.insert(2,11907435)
print 'searching for 11907435 ....... ', mylist.search(11907435)
print 'list size ---> ', mylist.size()

print 'index for kutta ---> ', mylist.index('kutta')
print 'index for 11435 ---> ', mylist.index(11435)
print 'index for tapan ---> ', mylist.index('tapan')
