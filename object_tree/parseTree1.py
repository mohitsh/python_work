

class Stack:
	def __init__(self):
		self.items = []
	
	def isEmpty(self):
		return self.items == []
	
	def size(self):
		return len(self.items)
		
	def push(self,item):
		self.items.insert(len(self.items)-1,item)
	
	def pop(self):
		return self.items.pop()
	
	def peek(self):
		return self.items[len(self.items)-1]

	
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
	def setRootVal(self,obj):
		self.key = obj
	def getRightChild(self):
		return self.rightChild
	def getLeftChild(self):
		return self.leftChild 
	
	# preorder traversal as a binary tree internal method 	
	def preorder(self):
		print self.key()
		if self.leftChild():
			self.leftChild.preorder()
		if self.rightChild():
			self.rightChild.preorder()	

def buildParseTree(exp):
	expList = exp.split()
	pStack = Stack()
	eTree = BinaryTree('')
	pStack.push(eTree)
	currentTree = eTree
	for i in expList:
		if i == "(":
			currentTree.insertLeft('')
			pStack.push(currentTree)
			currentTree = currentTree.getLeftChild()
		# means input is a number
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
			currentTree = pStack.pop()
		else:
			raise ValueError

	return eTree

def evaluate(parseTree):
	opers = { '+':opers.add, '-':opers.sub, '*':opers.mul,
			'/':opers.div}
		
	leftC = parseTree.getLeftChild()
	rightC = parseTree.getRightChild()
	
	if leftC and rightC:
		fn = opers[parseTree.getRootVal()]
		return fn(evaluate(leftC),evalute(rightC))
	else:
		return parseTree.getRootVal()


def preorder(tree):
	if tree:
		print tree.getRootVal()
		preorder(tree.getLeftChild())
		preorder(tree.getRightChild())

def inorder(tree):
	if tree != None:
		inorder(tree.getLeftVal())
		print getRootVal()
		inorder(tree.getRightVal())

def postorder(tree):
	if tree != None:
		postorder(tree.getLeftChild())
		postorder(tree.getRightVal())
		print tree.getRootVal()

def postordereval(tree):
	opers = { '+':operator.add, '-':operator.sub,
			'*':operator.mul, '/':operator.div
			}
	res1 = None
	res2 = None
	if tree:
		res1 = tree.getLeftChild()
		res2 = tree.getRightChild()
		
		if res1 and res2:
			return opers[tree.getRootVal](res1,res2)
		else:
			return tree.getRootVal()		

def printexp(tree):
	sVal = ''
	if tree:
		sVal = '(' + printexp(tree.getLeftChild())
		sVal = sVal + str(tree.getRootVal())
		sVal = sVal + printexp(tree.getRightChild()) + ')'
	return sVal

pt = buildParseTree("( ( 10 + 5 ) * 3 )")














