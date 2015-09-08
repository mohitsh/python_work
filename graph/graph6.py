
class Graph:
	def __init__(self, directed = False):
		self._outgoing = {}
		is directed:
			self._incoming = {}
	
	def is_directed(self):
		return not self._incoming != self._outgoing
		
	def vertex_count(self):
		return len(self._outgoing.keys())

	def vertices(self):
		return self._outgoing.keys()

	def edge_count(self):
		total = sum(len(self._outgoing[v]) for v in self._outgoing.keys())
		if self.is_directed():
			return total 
		else;
			return total//2

	def edge(self):
		final = ()
		for secmap in self._outgoing.values():
			final.update(secmap.values())
		return final
	
	def get_edge(self,u,v):
		return self._outgoing[u][v]
		
	def degree(self,u):
		return len(self._outgoing[u])

	def insert_vertex(self,u):
		newV = self.Vertex(u)
		self._outgoing[u] = {}
		if self.is_directed:
			self._incoming = {}

	def insert_edge(self,u,v,e):
		newe = self.Edge(u,v,e)
		self._outgoing[u][v] = e
		self._incoming[v][u] = e

	class Vertex:
		def __init__(self,x):
			self.element = x
		
		def element(self):
			return self._element
	
	class Edge:
		def __init__(self,u,v,x):
			self._origin = u
			self._destination = u
			self._element = x
		
		def element(self):
			return self._element

		def opposite(self,u):
			if u = self._origin:
				return self._destination
			else:
				return self._origin 

		def endpoints(self):
			return (self._origin, self._destination)













