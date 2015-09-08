

from graph6 import Graph


def DFS(g,u,discovered):
	
	for e in g.incident_edge(u):
		v = e.opposite(u)
		if v not in discovered:
			discovered[v] = e
			DFS(g,v,discovered)

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

# computing all connected components

def dfs_complete(g):
	
	forest = {}
	for u in g.vertices():
		if u not in forest:
			forest[u] = None
			DFS(g,u,forest)

	return forest


''' graph implementation '''

E = (
    ('BOS','SFO',1000), ('BOS','JFK',2000), ('BOS','MIA',3000), ('JFK','BOS',4000),
    ('JFK','DFW',9000), ('JFK','MIA',8000), ('JFK','SFO',6000), ('ORD','DFW',5000),
    ('ORD','MIA',3000), ('LAX','ORD',8000), ('DFW','SFO',8000), ('DFW','ORD',5000),
    ('DFW','LAX',2000), ('MIA','DFW',4000), ('MIA','LAX',7000),
    )

g = Graph(directed = True)
V = set()
for e in E:
	V.add(e[0])
   	V.add(e[1])
print V

verts = {}  # map from vertex label to Vertex instance
for v in V:
	verts[v] = g.insert_vertex(v)

for key in verts:
	print key, '-->', verts.get(key).element()

for e in E:
	src = e[0]
    	dest = e[1]
    	element = e[2] if len(e) > 2 else None
    	g.insert_edge(verts[src],verts[dest],element)

edges = g.edge()
for key in edges:
	print key.element()

print verts['JFK']
discovered = {}
DFS(g,verts['JFK'],discovered)

for key in discovered:
	print key, '-->', discovered.get(key)

print 'constructed path -->'
path  = construct_path(verts['JFK'],verts['ORD'],discovered)
for key in path:
	print key
	print key.element()








