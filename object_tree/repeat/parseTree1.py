
class Stack:
	def __init__(self):
		self.items = []
	
	def isEmpty(self):
		return self.items == []

	def size(self):
		return len(self.items)

	def push(self,item):
		self.items.append(item)

	def pop(self,item):
		self.item.pop()
	
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

	

def parseTree(exp):
	t = BinaryTree('')
	p = Stack()
	expList = exp.split()
	currentTree = t
	p.push(t)
	for i in t:
		if i == '(':
			currentTree.insertLeft("")
			p.push(currentTree)
			currentTree = currentTree.getLeftChild()
			
		elif i not in ['+','-','*','/',')']:
			currentTree.setRootVal(int(i))
			currentTree = p.pop()

		elif i in ['+','-','*','/']:
			currentTree.setRootVal(i)
			currentTree.insertRight('')
			p.push(currentTree)
			currentTree = currentTree.getRightChild()

		elif i == ')':
			currentTree = p.pop()
		
		else:
			raise ValueError

	return t
			
			










	
