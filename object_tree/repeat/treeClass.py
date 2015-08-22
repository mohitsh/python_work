

class BinaryTree:
	def __init__(self,key):
		self.key = key		#node key value
		self.leftChild = None	# left reference
		self.rightChild = None	# right reference

	def insertLeft(self,node):
		t = BinaryTree(node)
		if self.leftChild == None:
			self.leftChild = t
		else:
			t.leftChild = self.leftChild
			self.leftChild = t

	def insertRight(self,node):
		t = BinaryTree(node)
		if self.rightChild == None:
			self.rightChild = t
		else:
			t.rightChild = self.rightChild
			self.rightChild = t
	
	def getRootVal(self):
		return self.key

	def setRootVal(self,newkey):
		self.key = newkey

	def getLeftChild(self):
		return self.leftChild

	def getRightChild(self):
		return self.rightChild

r = BinaryTree('a')
print r.getRootVal()
print r.getLeftChild()
r.insertLeft('b')
print r.getLeftChild()


