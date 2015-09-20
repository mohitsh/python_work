
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
		def opposite(self,v):
			if not isinstance(v,Graph.Vertex):
				raise TypeError('v must be a vertex')
			return self._destination if self._origin else self._origin
			raise ValueError('v not incident to this edge') 
		def edges(self):
			return (self._origin,self._destination)
		def __str__(self):
			return '({0},{1},{2})'.format(self._origin,self._destination,self._element)

	def _validate_vertex(self,v):
		if not isinstance(v,self.Vertex):
			raise TypeError('Vertex Error')
		if v not in self._outgoing:
			raise ValueError("Vertex doesn't belong to this graph")	

	def __init__(self,directed = False):
		self._outgoing = {}
		self._incoming = {} if directed else self._outgoing
		
	def is_directed(self):
		return self._incoming is not self._outgoing

	def insert_vertex(self,x):
		v = self.Vertex(x)
		self._outgoing[v] = {}
		if self.is_directed():
			self._incoming = {}
		return v

	def insert_edge(self,u,v,x):
		if  self.getedge(u,v) is not None:
			raise ValueError('u and v are already adjacent')
		e = self.Edge(u,v,x)
		self._outgoing[u][v] = e
		self._incoming[v][u] = e

	def vertex_count(self):
		return len(self._outgoing)
	
	def vertices(self):
		return self._outgoing.keys()

	def edge_count(self):
		total = sum(len(self._outgoing[key]) for key in self._outgoing)
		return total if self.is_directed() else total//2		
	def edges(self):
		result = set()
		for secmap in self._outgoing.values():
			result.update(secmap.values())
		return result

	def degree(self,v,outgoing=True):
		self._validate_vertex(v)
		adj = self._outgoing if self.is_directed() else self._incoming
		return len(adj[v])

	def getedge(self,u,v):
		self._validate_vertex(u)
		self._validate_vertex(v)
		return self._outgoing[u].get(v)

	def incident_edge(self,v,outgoing = True):
		adj = self._outgoing if outgoing else self._incoming
		for edge in adj[v].values():
			yield edge

'''
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

print "checking for methods:"
print g.vertex_count()
v = g.vertices()
for i in v:
	print i.element()

e1 = g.insert_edge(v1,v2,10)
e2 = g.insert_edge(v2,v4,20)
e3 = g.insert_edge(v1,v4,30)
e4 = g.insert_edge(v1,v5,40)
e5 = g.insert_edge(v1,v3,50)
e6 = g.insert_edge(v3,v5,60)
e7 = g.insert_edge(v4,v5,70)
#e8 = g.insert_edge(v4,v5,10)
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
