

class Graph:
	class Vertex:	
		def __init__(self,x):
			self._element = x
		def __str__(self):
			return str(self._element)

	class Edge:
		def __init__(self,u,v,x):
			self._origin = u
			self._destination = v
			self._element = x
		def opposite(self,u):
			return self._destinaton if self._origin else self._origin 
		
		def __str__(self):
			return '({0},{1},{2})'.format(self._origin,self._destination,self._element)		
	
	def __init__(self,directed = False):
		self._outgoing = {}
		self._incoming = {} if directed else self._outgoing
	
	def is_directed(self):
		return self._incoming is not self._outgoing

	def insertVertex(self,x):
		v = self.Vertex(x)
		self._outgoing[v] = {}
		if self.is_directed():
			self._incoming = {}
		return v	
	def insertEdge(self,u,v,x=None):
		e = self.Edge(u,v,x)
		self._outgoing[u][v] = e
		self._incoming[v][u] = e

	def incident_edge(self,u,outgoing = True):
		adj = self._outgoing if outgoing else self._incoming
		for edge in adj[u].values():
			yield edge

	def vertices(self):
		return self._outgoing.keys()
	
	def edges(self):
		result = set()
		for secmap in self._outgoing.values():
			result.update(secmap.values())
		return result

g = Graph()

v1 = g.insertVertex("v1")
v2 = g.insertVertex("v2")
v3 = g.insertVertex("v3")
v4 = g.insertVertex("v4")

e1 = g.insertEdge(v1,v2,100)
e2 = g.insertEdge(v1,v3)
e3 = g.insertEdge(v3,v4,300)
e4 = g.insertEdge(v1,v4)
e5 = g.insertEdge(v2,v3)

dude = g.vertices()
for k in dude:
	print k

ndude = g.edges()
for k in ndude:
	print k



