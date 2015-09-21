
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

def dfs_complete(g):
	forest = {}
	for u in g.vertices():
		if u not in forest:
			forest[u] = None
			dfs(g,u,forest)
	return forest

dic = {}
dic = dfs(g,v5,dic)
for key in dic:
	print key,dic[key]


'''
print "beware forest below"
forest = dfs_complete(g)
for key in forest:
	print key,forest.get(key)
'''
