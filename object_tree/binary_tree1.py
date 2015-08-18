

class BinaryTree:
	def __init__(self,rootObj):
		self.key = rootObj
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
		if self.rightChild == None:
			self.rightChild = t
		else:
			t.rightChild = self.rightChild 	
			self.rightChild = t

	def getRightChild(self):
		return self.rightChild
	
	def getLeftChild(self):
		return self.leftChild
	
	def getRootVal(self):
		return self.key

	def setRootVal(self,obj):
		self.key = obj
	
r = BinaryTree('a')
print(r.getRootVal())
print(r.getLeftChild())
r.insertLeft('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())
r.insertRight('c')
print(r.getRightChild())
print(r.getRightChild().getRootVal())
r.getRightChild().setRootVal('hello')
print(r.getRightChild().getRootVal())
