

from stack import Stack
from binary_tree import BinaryTree

def buildParseTree(exp):
	expList = exp.split()
	pstack = Stack()
	t = BinaryTree('')
	pstack.push(t)
	currentTree = t
	
	for i in expList:
		if i == '(':
			currentTree.insertLeft('')
			pstack.push(currentTree)
			currentTree = currentTree.getLeftChild()
		elif i not in ['+','-','*','/',')']:
			currentTree.setRootVal(int(i))
			parent = pstack.pop()
			currentTree = parent
		elif i in ['+','-','*','/']:
			currentTree.setRootVal(i)
			currentTree.insertRight('')
			pstack.push(currentTree)
			currentTree = currentTree.getRightChild()
		elif i == ')':
			currentTree = pstack.pop()
		else:
			raise ValueError
	return t

def evaluate(parseTree):
	opers = {'+':operator.add, '-':operator.sub,
			'*':operator.mul, '/':operator.div
			}
	leftC = parseTree.getLeftChild()
	rightC = parseTree.getRightChild()
	
	if leftC and rightC:
		fn = opers[parseTree.getRootVal()]
		return fn(evaluate(leftC),evaluate(rightC))
	else:
		return parseTree.getRootVat()

	
def preorder(tree):
	if tree != None:	
		print tree.getRootVal()
		preorder(tree.getLeftChild())
		preorder(tree.getRightChild())
	
def inorder(tree):
	if tree != None:
		inorder(tree.getLeftChild())
		print tree.getRootVal()
		inorder(tree.getRightChild())

def postorder(tree):
	if tree != None:
		postorder(tree.getLeftChild())
		postorder(tree.getRightChild())
		print tree.getRootVal()		
		
# same function again
def evaluate(parseTree):
	opers = {'+':operands.add,'-':operands.sub,'*':operands.mul,
			'/':operands.div}
	leftC = parseTree.getLeftChild()
	rightC = parseTree.getRightChild()
	
	if leftC and rightC:
		fn = opers[parseTree.getRootNode()]
		return fn(evaluate(leftC), evaluate(rightC))
	else:
		return parseTree.getRootVal()

def postordereval(tree):
	opers = {'+':operands.add, '-':operands.sub, '*':operands.mul,
			'/':operands.div}
	
	res1 = None
	res2 = None
	
	if tree:
		res1 = postordereval(tree.getLeftChild())
		res2 = postordereval(tree.getRightChild())
	
		if res1 and res2:
			fn = opers[tree.getRootval()]
			return fn(res1,res2)
		else:
			return tree.getRootVal()

def printexp(tree):
	sVal = ''
	if tree:
		sVal = '(' + printexp(tree.getLeftChild())
		sVal = sVal + printexp(tree.getRootval())
		sVal = sVal + printexp(tree.getRightChild()) + ')'
	return sVal

pt = buildParseTree("( ( 10 + 5 ) * 3 )")
print 'postorder' 
postorder(pt)
print 'inorder' 
inorder(pt)
print 'preorder'
preorder(pt)
