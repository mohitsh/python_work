

def BinaryTree(r):
	return [r,[],[]]

def insertLeft(r,newNode):
	# tree is modified; element at position 1 is popped
	t = r.pop(1)
	if len(t) > 1:
		r.insert(1,[newNode,t,[]])
	else:
		r.insert(1,[newNode,[],[]])
	return r

def insertRight(r,newNode):
	t = r.pop(2)
	if len(t) > 1:
		r.insert(2,[newNode,[],t])
	else:
		r.insert(2,[newNode,[],[]])
	return r
		
def getRootVal(r):
	return r[0]

def setRootVal(r,newKey):
	r[0] = newKey

def getLeftChild(r):
	return r[1]
	
def getRightChild(r):
	return r[2]

r = BinaryTree(3)
insertLeft(r,4)
insertLeft(r,5)
insertRight(r,6)
insertRight(r,7)
l = getLeftChild(r)
print(l)

setRootVal(l,9)
print(r)
insertLeft(l,11)
print(r)
print(getRightChild(getRightChild(r)))
