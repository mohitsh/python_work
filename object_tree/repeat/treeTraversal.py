

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

