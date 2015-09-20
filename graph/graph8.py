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
			self._element = x
		def opposite(self):
			return self._destination if self._origin else self._origin
		def edges(self):
			return (self._origin,self._destination)

		def __str__(self):
			return '({0},{1},{2})'.format(self._origin, self._destination, self._element)
	def __init__(self,directed = False):
		self._outgoing = {}
		self._incoming = {} if directed else self._outgoing

	def is_directed(self):
		return self._incoming is not self._outgoing

	def vertex_count(self):
		return len(self._outgoing)

	def vertices(self):
		return self._outgoing.keys()

	def edge_count(self):
		total = sum(len(self._outgoing[v]) for v in self._outgoing)
		if self.is_directed():
			return total
		else:
			return total//2

	def edges(self):
		result = set()
		for sec_map in self._outgoing.values():
			result.update(sec_map.values())
		return result

	def get_edge(self,u,v):
		return self._outgoing[u][v]

	
	def degree(self,v,outgoing = True):
		adj = self._outgoing if outgoing else self._incoming
		return len(adj[v])

	def incident_edges(self,v,outgoing = True):
		adj = self._outgoing if outgoing else self._incoming
		for edge in adj[v]:
			yield edge
	def insert_vertex(self,x=None):
		v = self.Vertex(x)
		self._outgoing[v] = {}
		if self.is_directed():
			self._incoming = {}
		return v    # don't forget to return v 

	def insert_edge(self,u,v,x=None):
		e = self.Edge(u,v,x)
		self._outgoing[u][v] = e
		self._incoming[v][u] = e

g = Graph()

v1 = g.insert_vertex("dalla")
v2 = g.insert_vertex("tapan")
v3 = g.insert_vertex("kutta")
v4 = g.insert_vertex("mittal")
v5 = g.insert_vertex("jangida")

print g.vertex_count()
print g.is_directed()
print 'vertices:'
verts = g.vertices()
for v in verts:
	print v

print "edge_count before insertion:", g.edge_count()
e1 = g.insert_edge(v1,v2,10)
e2 = g.insert_edge(v1,v3,30)
e3 = g.insert_edge(v1,v4,40)
e4 = g.insert_edge(v2,v5,20)
e5 = g.insert_edge(v3,v5,50)
e6 = g.insert_edge(v3,v4,60)
print "edge_cout after insertion:", g.edge_count()

e = g.edges()
for k in e:
	print k

print "edge b/w v1 and v2:", g.get_edge(v1,v2)
print "degree v1:", g.degree(v1)
print "degree v2:", g.degree(v2)
print "degree v3:", g.degree(v3)
print "degree v4:", g.degree(v4)
print "degree v5:", g.degree(v5)

print "incident edges on v1:" 
inci_edges = g.incident_edges(v1)
for k in inci_edges:
	print k

print "incident edges on v5:"
inci_edges = g.incident_edges(v5)
for k in inci_edges:
	print k


