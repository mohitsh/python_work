

def preorder(tree):
	if tree:
		print tree.getRootVal()
		preorder(tree.getLeftChild())
		preorder(tree.getRightChild())

'''
def preorder(self):
	print self.key
	if (self.LeftChild):
		self.LeftChild.preorder()

	if (self.RighChild()):
		self.RightChild().preorder()

'''
def postorder(tree):
	if tree:
		postorder(tree.getLeftChild())
		postorder(tree.getRightChild())
		print tree.getRootVal()

def inorder(tree):
	if tree:
		inorder(tree.getLeftChild())
		print tree.getRootVal()
		inorder(tree.getRightChild())

def postOrderEval(tree):
	opers = { '+':operator.add, '-':operator.sub, 
		'*':operator.mul, '/':operator.div}

	res1 = None
	res2 = None
	if tree:
		res1 = postOrderEval(tree.getLeftChild())
		res2 = postOrderEval(tree.getRightChild())
		if res1 and res2:
			fn = opers(tree.getRootVal())
			return fn(postOrderEval(res1),postOrderEval(res2))
		else:
			return tree.getRootVal()
