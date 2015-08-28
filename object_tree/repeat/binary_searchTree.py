


class BinarySearchTree:
	
	def __init__(self):
		self.root = None
		self.size = 0
	
	def lenght(self):
		return self.size
	
	def __len__(self):
		return self.size
	
	def __iter__(self):
		return self.root.__iter__()

	def put(self,key,val):
		if self.root:
			self._put(key,val,self.root)
		else:
			 self.root = TreeNode(key,val)
		self.size = self.size + 1
	
	
class TreeNode:
	
	def __init__(self,key,val,left=None,right=None,parent=None):
		
		self.key = key
		self.val = val
		self.leftChild = left
		self.rightChild = right
		self.paretn = parent
		
	def hasLeftChild(self):
		return self.leftChild
	
	def hasRightChild(self):
		return self.rightChild
	
	def isLeftChild(self):	
		return self.parent and self.parent.leftChild == self
	
	def isRightChild(self):
		return self.parent and self.parent.rightChild == self

	def isRoot(self):
		return not self.parent	

	def isLeaf(self):
		return not (self.rightChild and self.leftChild)
	
	def hasAnyChildren(self):
		return (self.rightChild or self.leftChild)_

	def hasBothChild(self):
		return (self.rightChild and self.rightChild)
	
	def replaceNodeData(self,key,value,lc,rc):
		self.key = key
		self.payload = value
		self.leftChild = lc
		self.rightChild = rc
		if self.hasLeftChild(self):
			self.leftChild.parent = self
		if self.hasRightChild(self):
			self.rightChild.parent = self

		




