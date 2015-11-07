
class Graph:
	class Vertex:
		def __init__(self,x):
			self._element = x
		def element(self):
			return self._element
		def __str__(self):
			return str(self._element)

	class Edge:
		def __init__(self,u,v,x):
			self._origin = u
			self._destination = v
			self._edge = x

		def opposite(self,v):
			return self._destination if self._origin else self._origin 

		def __str__(self):
			return '({0},{1},{2})'.format(self._origin,self._destination,self._edge)

	def __init__(self):
		self._outgoing = {}
		
	def insert_vertex(self,x):
		v = self.Vertex(x)
		self._outgoing[v] = {}
		return v
	def insert_edge(self,u,v,x):
		e = self.Edge(u,v,x)
		self._outgoing[v][v] = x
		return e

	def vertices(self):
		return self._outgoing.keys()

	def edges(self):
		result = set()
		for secmap in self._outgoing.values():
			result.update(secmap.values())
		return result

	def incident_edges(self,v):
		adj = self._outgoing
		arr = []
		return adj.get(v)
	def show(self):
		return self._outgoing

g = Graph()
a = g.insert_vertex('a')
b = g.insert_vertex('b')
c = g.insert_vertex('c')
d = g.insert_vertex('d')
e = g.insert_vertex('e')
f = g.insert_vertex('f')

e1 = g.insert_edge(a,b,3)
e2 = g.insert_edge(b,c,1)
e3 = g.insert_edge(c,d,6)
e4 = g.insert_edge(d,e,8)
e5 = g.insert_edge(e,a,6)
e6 = g.insert_edge(a,f,5)
e7 = g.insert_edge(f,d,5)
e8 = g.insert_edge(b,f,4)
e9 = g.insert_edge(c,f,4)
e10 = g.insert_edge(f,e,2)

start = a
store = []
verts = g.vertices()

ans = g.show()

for key in ans:
	for dude in key:
		print dude,key[dude]
	print ans[key]

#dude = g.incident_edges(start)
#for k in dude:
#	print k





