

class BinaryHeap:
	def __init__(self):
		self.heapList = [0]
		self.currentSize = 0
	
	# k is inserted at the end of the list
	def insert(self,k):
		# append k at the end of the list
		self.heapList.append(k)
		# increase the list size by one
		self.currentSize = self.currentSize + 1
		# call percUp to on the last element i.e. the element
		# added to maintain the heap property
		self.percUp(self.currentSize)
	
	def percUp(self,i):
		while i//2 > 0:
			if self.heapList[i] < self.heapList[i//2]:
				tmp = self.heapList[i]
				self.heapList[i] = self.heapList[i//2]
				self.heapList[i//2] = tmp
			i = i//2
		
	def percDown(self,i):
		while i*2 <= self.currentSize:
			mc = self.minChild(i)
			if self.heapList[i] > self.heapList[mc]:
				tmp = self.heapList[i]
				self.heapList[i] = self.heapList[mc]
				self.heapList[mc] = tmp
			i = mc
	
	def minChild(self,i):
		# there is no left child then return the left child
		if i*2 + 1 > self.currentSize:
			return i*2
		else:
			# if left node is less than right node return left
			if self.heapList[i*2] < self.heapList[i*2+1]:
				return i*2
			else:
			# else return right node
				return i*2 + 1

	def delMin(self):
		retval = self.heapList[1]
		self.heapList[1] = self.heapList[self.currentSize]
		self.currentSize = self.currentSize - 1
		self.heapList.pop()
		self.percDown(1)
		return retval

	def buildHeap(self,alist):
		i = len(alist)//2
		self.currentSize = len(alist)
		self.heapList = [0] + alist[:]
		while i>0:
			self.percDown(i)
			i = i - 1

bh = BinaryHeap()
bh.buildHeap([9,5,6,2,3])

print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())

	
