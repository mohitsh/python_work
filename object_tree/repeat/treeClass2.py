

class BinaryTree:
	def __init__(self,key):
		self.key = key
		self.leftChild = None
		self.rightChild = None
	
	def insertLeft(self,node):
		t = BinaryTree(node)
		if self.leftChild == None:
			t.leftChild = self.leftChild 
			self.leftChild = t
		else:
			self.leftChild = t
	
	def insertRight(self,node):
		t = BinaryTree(node)
		if self.rightChild == None:
			t.rightChild = self.rightChild
			self.rightChild = t
		else:
			self.rightChild = t

	def getRootVal(self):	
		return self.key
		
	def setRootVal(self,newkey):
		self.key = newkey

	def getLeftChild(self):
		return self.leftChild
	
	def getRightChild(self):
		return self.rightChild


r = BinaryTree(3)
print r
print r.getLeftChild()
print r.getRightChild()
r.setRootVal('wing')
print r
print r.getRootVal()
r.insertLeft('CE')
print r.getLeftChild().getRootVal()
r.insertRight('EE')
print r.getRightChild().getRootVal()
r.getLeftChild().insertLeft('Mohit')
print r.getLeftChild().getLeftChild().getRootVal()
r.getLeftChild().insertRight('Varun')
print r.getLeftChild().getRightChild().getRootVal()
r.getRightChild().insertLeft('Jain')
print r.getRightChild().getLeftChild().getRootVal()
r.getRightChild().insertRight('Indra')
print r.getRightChild().getRightChild().getRootVal()
	
