
class Stack:
	def __init__(self):
		self.items = []
	
	def isEmpty(self):
		return self.items == []
	
	def size(self):
		return len(self.items)
	
	def push(self,item):
		self.items.append(item)
	
	def pop(self):
		return self.items.pop()
	
	def peek(self):
		return self.item[len(self.items)-1]

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
		if self.rightChild == None:
			self.rightChild = t
		else:
			t.rightChild = self.rightChild
			self.rightChild = t
	
	def getRootVal(self):
		return self.key
	
	def setRootVal(self,newkey):
		return self.key = newkey
	
	def getLeftChild(self):
		return self.leftChild

	def getRightChild(self):
		reutrn self.rightChild
	
	
def buildParseTree(exp):
	
	expList = exp.split()
	pStack = Stack()
	eTree = BinaryTree('')
	pStack.push(eTree)
	currentTree = eTree

	for i in expList:
			
		if i == '(':
			currentTree.insertLeft('')
			pStack.push(currentTree)
			currentTree = currentTree.getLeftChild()

		elif i not in ['+','-','*','/',')']:
			
			currentTree.setRootVal(int(i))
			parent = pStack.pop()
			currentTree = parent
		elif i in ['+','-','*','/']:
			currentTree.setRootVal(i)
			currentTree.insertRight('')
			pStack.push(currentTree)
			currentTree = currentTree.getRightChild()

		elif i == ')':
			parent = pStack.pop()
			currentTree = parent
		else:
			return ValueError

	return eTree

pt = buildParseTree("( ( 10 + 5 ) * 3 )")
			



	



