

tree = ['a',
		['b',['d',[],[]],['e',[],[]]],
		['c',[],[]]
	]

print 'root',tree[0]
print 'leftchild',tree[1]
print 'rightchild',tree[2]
left = tree.pop(1)
right = tree.pop(1)
print len(left)
print len(right)
