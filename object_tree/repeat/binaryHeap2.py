
class BinHeap:
	def __init__(self):
		self.heapList = [0]
		self.currentSize = None
	
	def insert(self,key):
		self.heapList.append(key)
		self.currentSize = self.currentSize + 1
		self.percUp(self.currentSize)
	
	def percUp(self,i):
		while i//2 > 0:
			parent = self.heapList[i//2]
			if parent > self.heapList[i]:
				tmp = self.heapList[i]
				self.heapList[i] = parent 
				parent = tmp
			i = i//2
		 
	def delMin(self):
		rootVal = self.heapList[1]
		self.heapList[1] = self.heapList[self.currentSize]
		# pop and currentSize can be reversed
		self.heapList.pop()
		self.currentSize = self.currentSize - 1
		# this thing can be checked
		self.percDown(1)
		return rootVal

	def minChild(self,i):
		if i*2 +1  > self.currentSize:
			return i*2
		else:
			if self.heapList[i*2] <self.heapList[i*2+1]:
				return i*2
			else:
				return i*2 + 1

	def percDown(self,i):
		while i*2 <= self.currentSize:
			mc = self.minChild(i)
			if self.heapList[mc] < self.heapList[i]:
				tmp = self.heapList[mc]
				self.heapList[mc] = self.heapList[i]
				self.heapList[i] = tmp
			i = mc
	'''
	def minChild(self,i):
		if i*2+1 > self.currentSize:
			return i*2 + 1
		else:
			if self.heapList[i*2] < self.heapList[i*2+1]:
				return i*2
			else:
				return i*2+1	
	'''
	
	def buildHeap(self,alist):
		i = len(alist)//2
		self.currentSize = len(alist)
		self.heapList = [0] + alist[:]
		while i > 0:
			self.percDown(i)
			i = i -1 
						
	def show(self,k):
		print self.heapList[1:k]

bh = BinHeap()
bh.buildHeap([9,5,6,2,3])
bh.show(3)
bh.show(2)
bh.show(4)
bh.show(5)
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())


