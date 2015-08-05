# queue abstract data type 
# main functionality queue, dequeue and size

class queue:
	def __init__(self):
		self.items = []
	def isEmpty(self):
		return queue.items == []
	def size(self):
		return len(self.items)
	def enqueue(self,item):
		self.items.insert(0,item)
	def peek(self):
		return self.items[len(self.items)-1]
	def dequeue(self):
		return self.items.pop()
	def show(self):
		print self.items

'''
In hot potato problem a list of names is supplied
which is converted into a queue for further uses.
remember in queue simultaneous dequeing and enqueing 
make it behave like a circle.
for num no of times queue is being dequed and enqued 
and then dequed 
until only one element is left that is the person who
wins/survives.
'''
def hotPotato(names,num):
	q = queue()
	for i in range(len(names)-1,-1,-1):
		q.enqueue(names[i])
	
	while q.size() > 1:
		for i in range(num):
			q.enqueue(q.dequeue())
		q.dequeue ()
	return q.dequeue()

nameList = ['Brad','Kent','Jane','Susan','David','Bill']
print hotPotato(nameList,3)
print hotPotato(nameList, 7)
	
