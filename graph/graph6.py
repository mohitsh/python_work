
class Graph:
	def __init__(self, directed = False):
		self._directed = directed
		self._outgoing = {}
		if directed:
			self._incoming = {}
		else:
			self._outgoing
	
	def is_directed(self):
		return self._directed
		
	def vertex_count(self):
		return len(self._outgoing.keys())

	def vertices(self):
		return self._outgoing.keys()

	def edge_count(self):
		total = sum(len(self._outgoing[v]) for v in self._outgoing.keys())
		if self.is_directed():
			return total 
		else:
			return total//2

	def edge(self):
		final = ()
		for secmap in self._outgoing.values():
			final.update(secmap.values())
		return final
	
	def get_edge(self,u,v):
		return self._outgoing[u].get(v)
		
	def degree(self,u):
		return len(self._outgoing[u])

	def insert_vertex(self,x = None):
		newV = self.Vertex(x)
		self._outgoing[newV] = {}
		if self.is_directed():
			self._incoming[newV] = {}
		return newV

	def insert_edge(self,u,v,x = None):
		newe = self.Edge(u,v,x)
		self._outgoing[u][v] = newe
		if self.is_directed(): self._incoming[v][u] = newe

	class Vertex:
		def __init__(self,x):
			self.element = x
		
		def element(self):
			return self._element
		
		#def __str__(self):
		#	return self.element
	
	class Edge:
		def __init__(self,u,v,x):
			self._origin = u
			self._destination = v
			self._element = x
		
		def element(self):
			return self._element

		def opposite(self,u):
			if u == self._origin:
				return self._destination
			else:
				return self._origin 

		def endpoints(self):
			return (self._origin, self._destination)


g = Graph()
print g
ver1 = g.insert_vertex('dalla')
print ver1
ver2 = g.insert_vertex('tapan')
print ver2
ver3 = g.insert_vertex('jain')
ver4 = g.insert_vertex('namit')
g.insert_edge(ver1,ver2,1000)
a = g.vertices()

print 'directed -->', g.is_directed()
print 'vertex_count -->', g.vertex_count()
print 'edge b/w dalla and tapan -->', g.get_edge(ver1,ver2)
#print a.element()










