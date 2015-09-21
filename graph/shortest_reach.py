

class Graph:
	class Vertex:
		def __init__(self,x):
			self._element = x
		def __str__(self):
			return str(self._element)
	class Edge:
		def __init__(self,u,v,x):
			self._origin  = u
			self._destination = v
			self._element = x
		def opposite(self,u):
			return self._destination if u is self._origin else self._origin
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
			self._incoming[v] = {}
		return v	
	
	def insertEdge(self,u,v,x=6):
		e = self.Edge(u,v,x)
		self._outgoing[u][v] = e
		self._incoming[v][u] = e

	def incident_edges(self,u,outgoing = True):
		adj = self._outgoing if outgoing else self._incoming
		for edge in adj[u].values():
			yield edge
	def vertices(self):
		return self._outgoing.keys()
	def edges(self):
		result = set()
		for sec_map in self._outgoing.values():
			result.update(sec_map.values())
		return result

g = Graph()

a = g.insertVertex("a")
b = g.insertVertex("b")
c = g.insertVertex("c")

a_b = g.insertEdge(a,b)
a_c = g.insertEdge(a,c)
b_c = g.insertEdge(b,c)

vert = g.vertices()
for k in vert:
	print k

edge = g.edges()
for k in edge:
	print k



 
