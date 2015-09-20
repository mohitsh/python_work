
from graph10 import Graph

g = Graph()

v1 = g.insert_vertex("dalla")
v2 = g.insert_vertex("tapan")
v3 = g.insert_vertex("kutta")
v4 = g.insert_vertex("mittal")
v5 = g.insert_vertex("jangida")
e1 = g.insert_edge(v1,v2,10)
e2 = g.insert_edge(v2,v4,20)
e3 = g.insert_edge(v1,v4,30)
e4 = g.insert_edge(v1,v5,40)
e5 = g.insert_edge(v1,v3,50)
e6 = g.insert_edge(v3,v5,60)
e7 = g.insert_edge(v4,v5,70)

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


def DFS(g,u,dic):
	for e in g.incident_edge(u):
		v = e.opposite(u)
		if v not in dic:
			dic[v] = e
			DFS(g,v,dic)

dic = {}
DFS(g,v1,dic)
for key in dic:
	print key,dic[key]


