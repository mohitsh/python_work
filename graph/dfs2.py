
from graph10 import Graph

g = Graph()

v1 = g.insert_vertex("a")
v2 = g.insert_vertex("b")
v3 = g.insert_vertex("c")
v4 = g.insert_vertex("d")
v5 = g.insert_vertex("e")
v6 = g.insert_vertex("f")
v7 = g.insert_vertex("g")
v8 = g.insert_vertex("h")

e1 = g.insert_edge(v1,v5,10)
e2 = g.insert_edge(v1,v6,20)
e3 = g.insert_edge(v1,v2,30)
e4 = g.insert_edge(v5,v6,40)
e5 = g.insert_edge(v2,v6,50)
e6 = g.insert_edge(v2,v3,60)
e7 = g.insert_edge(v3,v4,70)
e8 = g.insert_edge(v3,v7,80)
e9 = g.insert_edge(v4,v7,90)
e10 = g.insert_edge(v4,v8,100)

'''
print g.vertex_count()
print g.is_directed()
print 'vertices:'
verts = g.vertices()
for v in verts:
        print v
print "checking for methods:"
print g.vertex_count()
v = g.vertices()
for i in v:
        print i.element()
print g.edge_count()
e = g.edges()
for k in e:
        print k

print "fucking degree: "
print g.degree(v1)
print g.degree(v5)
e1 = g.getedge(v1,v2)
e2 = g.getedge(v1,v5)
print e1
print e2
print "beware!!"
in_edges = g.incident_edge(v1)
for k in in_edges:
        print k
'''
#e1 = g.getedge(v1,v5)
#print e1.opposite(v5)
#print e1.opposite(v1)

def DFS(g,u,dic):
	for e in g.incident_edge(u):
		v = e.opposite(u)
		if v not in dic:
			dic[v] = e
			DFS(g,v,dic)
	return dic

def construct_path(u,v,dic):
	path = []
	if v in dic:
		path.append(v)
		walk = v
		while walk is not u:
			#print "inside while"
			e = dic[walk]
			parent = e.opposite(walk)
			path.append(parent)
			walk = parent
		path.reverse()
	return path

dic = {}
dude = DFS(g,v1,dic)

#for key in dude:
#	print key,dude[key]

path = construct_path(v1,v8,dude)
for line in path:
	print line
	






