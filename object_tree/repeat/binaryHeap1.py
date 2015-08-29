a

class BinHeap:
	def __init__(self):
		self.heapList = [0]
		self.currentSize = None

	def insert(self,key):
		self.heapList.append(key)
		self.currentSize = self.currentSize = self.currentSize + 1
		self.percUp(currentSize)

	def percUp(self,i):
		while i//2 > 0:
			parent = heapList[i//2]
			if parent > heapList[i]:
				temp = parent
				parent = heapList[i]
				heapList[i] = temp
			i = i//2

	def delMin(self):
		# get the root value to return it in the end
		rootval = self.heapList[1]
		# put the last element as the root element
		self.heapList[1] = self.heapList[self.currentSize]
		# decrease the currentsize of heap
		self.currentSize = self.currentSize -1
		# now pop the last element since it is moved to root position
		self.heapList.pop()
		# now percolate the root element down to right position
		self.percDown(1)
		# now return the root value
		return rootval

	def percDown(self,i):
		while i*2 <= self.currentSize:
			mc = self.minChild(i)
			if self.heapList[mc] < self.heapList[i]:
				tmp = self.heapList[mc]
				self.heapList[mc] = self.heapList[i]
				self.heapList[i] = tmp
			i = mc

	def minChild(self,i):
		if i*2 +1 > self.currentSize:
			return i*2
		else:
			if self.heapList[2*i] > self.heapList[2*i +1]:
				return 2*i+1
			else:
				return 2*i

	def buildHeap(self,alist):
		i = len(alist)//2
		self.currentSize = len(alist)
		self.heapList = [0] + alist[:]
		while i > 0:
			self.percDown(i)
			i = i - 1

bh = BinHeap()
bh.buildHeap([9,5,6,2,3])

print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())	


