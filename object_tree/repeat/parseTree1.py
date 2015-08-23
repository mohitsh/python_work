
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
		self.items.pop()
	
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
	print t
	p = Stack()
	expList = exp.split(" ")
	p.push(t)	
	print expList
	currentTree = t
	print currentTree
	
	for i in expList:
		if i == '(':
			print i
			print currentTree
			currentTree.insertLeft("")
			p.push(currentTree)
			currentTree = currentTree.getLeftChild()
			print 'after insertion', currentTree	
		elif i not in ['+','-','*','/',')']:
			currentTree.setRootVal(int(i))
			currentTree = p.pop()

		elif i in ['+','-','*','/']:
			print currentTree
			print i
			currentTree.setRootVal(i)
			currentTree.insertRight('')
			p.push(currentTree)
			currentTree = currentTree.getRightChild()

		elif i == ')':
			currentTree = p.pop()
		
		else:
			raise ValueError

	return t


def evaluate(parseTree):
	opers = {'+':operator_add,'-':operator_sub,'*':operator_mul,'/':operator_div}
	leftC = parseTree.getLeftChild()
	rightC = parseTree.getRightChild()
	
	if leftC and rightC:
		operand = opers[parseTree.getRootVal()]
		return operand(evaluate(leftC),evaluate(rightC))
	else:
		return parseTree.getRootVal()
			
def operator_add(a,b):
	return a+b
def operator_sub(a,b):
	return a-b
def operator_mul(a,b):
	return a*b
def operator_div(a,b):
	return a/b

pt = parseTree("( ( 10 + 5 ) * 3 )")
print evaluate(pt)










	
