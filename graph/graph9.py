

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
		def opposite(self,u):
			return self._destination if self._origin else self._origin
		def edges(self):	
			return (self._origin, self._destination) 
		def _str__(self):
			return '({0},{1},{2})'.format(self._origin,self._destination,self._element)
	def __init__(self,directed=False):
		self._outgoing = {}
		self._incoming = {} if directed else self._outgoing

	def is_directed(self):
		return self._incoming is not self._outgoing

	def vertex_count(self):
		return len(self._outgoing)
	def vertices(self):
		return self._outgoing.keys()
	def edge_count(self):
		total = sum(len(self._outgoing[key]) for key in self._outgoing)
		return total if directed else total//2
	def edges(self):
		result = set()
		for secmap in self._outgoing.values():
			set.update(secmap.values())
		return result
	def getedge(self,u,v):	
		return self._outgoing[u][v]
	def degree(self,v,outgoing=True):
		adj = self._outgoing if outgoing else self._incoming
		return len(adj[v])
	def incident_edges(self,v,outgoing = True):
		adj = self._outgoing if outogig else self._incoming
		for edge in adj[v]:
			yield edge
	def insert_vertex(self,x):
		v = self.Vertex(x)
		self._outgoing[v] = {}
		if self.is_directed():
			self._incoming = {}
		return v
	def insert_edge(self,u,v,x):
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

