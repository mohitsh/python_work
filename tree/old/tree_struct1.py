

def BinaryTree(r):
	return [r,[],[]]

def insertLeft(r,newBranch):
	t = r.pop(1)
	if len(t) > 1:
		r.insert(1,[newBranch,t,[]])
	else:
		r.insert(1,[newBranch,[],[]])
	return r

def insertRight(r,newBranch):
	t = r.pop(2)
	if len(t) > 1:
		r.insert(2,[newBranch,[],t])
	else:
		r.insert(2,[newBranch,[],[]])
	return r

def getRootVal(root):
	return root[0]
	

def setRootVal(root,newVal):
	root[0] = newVal

def getLeftChild(root):
	return root[1]

def getRightChild(root):
	return root[2]

r = BinaryTree(3)
insertLeft(r,4)
insertLeft(r,5)
insertRight(r,6)
insertRight(r,7)
l = getLeftChild(r)
print l

setRootVal(l,9)
print r
insertLeft(l,11)
print getLeftChild(getLeftChild(r))

