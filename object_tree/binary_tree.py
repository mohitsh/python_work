

class BinaryTree:
	def __init__(self,obj):
		self.key = obj
		self.leftChild = None
		self.rightChild = None
	
	def insertLeft(self,newNode):		
		t = BinaryTree(newNode)
		if self.leftChild == None:
			self.leftChild = t
		else:
			t.leftChild = self.leftChild
			self.leftChild = t
	def insertRight(self,newNode):	
		t = BinaryTree(newNode)
		if self.rightNode == None:
			self.rightNode = t
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
	
