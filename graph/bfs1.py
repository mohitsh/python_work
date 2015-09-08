
from graph6 import Graph

def BFS(g,s,discovered):
	
	level = [s]
	while len(level) > 0:
		next_level = []
		
		for u in level:
			for e in g.incident_edge(u):
				v = e.opposite(u)
				if v not in discovered:
					discovered[v] = e
					next_level.append(v)
		level = next_level

''' graph implementation '''

'''
g = Graph(directed = True)

bos = g.insert_vertex('bos')
jfk = g.insert_vertex('jfk')
dfw = g.insert_vertex('dfw')
lax = g.insert_vertex('lax')
ordo = g.insert_vertex('ordo')
sfo = g.insert_vertex('sfo')
mia = g.insert_vertex('mia')

g.insert_edge(bos,jfk,10)
g.insert_edge(jfk,dfw,20)
g.insert_edge(dfw,lax,30)
g.insert_edge(lax,ordo,40)
g.insert_edge(ordo,mia,50)
g.insert_edge(dfw,sfo,60)
'''

'''
print 'constructed path b/w BOS and JFK-->'
path  = construct_path(bos,jfk,discovered)
for key in path:
        print key.element()
print 'constructed path b/w BOS and SFO-->'
path  = construct_path(bos,sfo,discovered)
for key in path:
        print key.element()

print 'constructed path b/w JFK and LAX-->'
path  = construct_path(jfk,lax,discovered)
for key in path:
        print key.element()

print 'constructed path b/w DFW and ORD-->'
path  = construct_path(dfw,ordo,discovered)
for key in path:
        print key.element()
'''
g = Graph()
t = int(raw_input())
for i in range(t):
	nodeAndEdge = raw_input().split()
	arr1 = [int(x) for x in nodeAndEdge]
	n_nodes = arr1[0]
	n_edges = arr1[1]
	verts = {}
	for k in range(1,n_nodes+1):
		verts[k] = g.insert_vertex(k)
	#for key in verts:
	#	print key, verts[key]
	
	for j in range(n_edges):
		nodeHasEdge = raw_input().split()
		arr2 = [int(x) for x in nodeHasEdge]
		g.insert_edge(verts[arr2[0]],verts[arr2[1]],6)
	start = int(raw_input())
	
	'''
	edges = g.edge()
	for key in edges:
        	print key, '-->', key.element()

	vertices = g.vertices()
	for ver in vertices:
		print ver, '-->', ver.element()
	'''
	
	discovered = {}
	BFS(g,verts[start],discovered)
	for key in discovered:
		print key.element(), discovered[key].element()
	ans = [-1]*(n_nodes+1)
	for key in discovered: 	
		#print key.element(), discovered.get(key).element()
		if discovered.get(key).element() != -1:
			ans[key.element()] = discovered.get(key).element()

	print ' '.join(str(x) for x in ans[2:])

	'''
	def construct_path(u,v,discovered):

        	path = []
        	if v in discovered:
                	path.append(v)
                	walk = v
                	while walk is not u:
                        	e = discovered[walk]
                        	parent = e.opposite(walk)
                     	  	path.append(parent)
                        	walk = parent
                        #print walk
                	path.reverse()
        	return path
	'''







