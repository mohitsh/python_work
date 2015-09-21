from graph10 import Graph

g = Graph()

v1 = g.insert_vertex("v1")
v2 = g.insert_vertex("v2")
v3 = g.insert_vertex("v3")
v4 = g.insert_vertex("v4")
v5 = g.insert_vertex("v5")
v6 = g.insert_vertex("v6")
v7 = g.insert_vertex("v7")
#v8 = g.insert_vertex("h")

e1 = g.insert_edge(v1,v2,10)
e2 = g.insert_edge(v1,v3,20)
e3 = g.insert_edge(v3,v4,30)
e4 = g.insert_edge(v1,v4,40)
e5 = g.insert_edge(v2,v3,50)
e6 = g.insert_edge(v5,v7,60)
e7 = g.insert_edge(v6,v7,70)
e8 = g.insert_edge(v5,v6,80)
#e9 = g.insert_edge(v4,v7,90)
#e10 = g.insert_edge(v4,v8,100)

def dfs(g,u,dic):
	for e in g.incident_edge(u):
		v = e.opposite(u)
		if v not in dic:
			dic[v] = e
			dfs(g,v,dic)
	return dic

def construct_path(u,v,dic):
	path = []
	if v in dic:
		path.append(v)
		walk = v
		while walk is not u:
			e = dic[walk]
			parent = e.opposite(walk)
			path.append(parent)
			walk = parent
		path.reverse()
	return path


def dfs1(g,v,dic):
	for e in g.incident_edge(v):
		u = e.opposite(v)
		if u not in dic:
			dic[u] = e
			dfs(g,u,dic)
	return dic


def construct_path1(u,v,dic):
	path = []
	if v in dic:
		path.append(v)
		walk = v
		while walk is not u:
			e = dic[walk]
			parent = e.opposite(walk)
			path.append(parent)
			walk = parent
		path.reverse()
	return path

dic = {}
dude = dfs1(g,v5,dic)
print "dictionary ->"
for key in dic:
	print key,dic[key]

print "path b/w v1 and v7 ->"
path = construct_path1(v5,v7,dude)
for v in path:
	print v

# connected components

print "no of connected components are equal to vertices having None as edge"
def dfs_complete(g):
	forest = {}
	for u in g.vertices():
		if u not in forest:
			forest[u] = None
			dfs(g,u,forest)
	return forest

forest = dfs_complete(g)
for k in forest:
	print k,forest[k]
