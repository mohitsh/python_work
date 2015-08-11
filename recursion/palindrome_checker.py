class dequeue:
	def __init__(self):
		self.items = []
	def size(self):
		return len(self.items)
	def isEmpty(self):
		return self.items == []
	def addFront(self,item):
		self.items.append(item)
	def addRear(self,item):
		self.items.insert(0,item)
	def removeFront(self):
		return self.items.pop()
	def removeRear(self):
		return self.items.pop(0)
	def show(self):
		return self.items

def palindrome(word):
	d = dequeue()
	for i in word:
		d.addRear(i)
	flag = True
	while d.size() > 1 and flag:
		if d.removeFront() != d.removeRear():
			flag = False
	return flag
		

print palindrome('radar')
print palindrome('mohahom')
print palindrome('dalaalad')
print palindrome('mohit')
print palindrome('utkarsh')
print palindrome("lsdkjfskf")
