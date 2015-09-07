
class Graph:

	class Vertex:
		def __init__(self,e):
			self._element = e
		
		def element(self):
			return self._element
	
		#def __str__(self):
		#return self._element

	class Edge:
		def __init__(self,u,v,e):
			self._element = e
			self._origin = u
			self._destination = v
	
		def opposite(self,u):
			if self._origin == u:
				return self._destination

			else:
				return self._origin 
		
		def endpoints(self):
			return (self._origin, self._destination)

		def elements(self):
			return self._element

	def __init__(self, directed = False):
		
		self._outgoing = {}
		if directed == True:
			self._incoming = {}
		
	def is_directed(self):
		return self._incoming != self._outgoing
	
	def vertex_count(self):
		return len(self._outgoing)

	def vertices(self):
		return self._outgoing.keys()

	def edge_count(self):
		total = sum(len(self._outgoing[v]) for v in self._outgoing)
		if self.is_directed:
			return total
		else:
			return total//2
	
	def edge(self):
		result = set()
		for second_map in self._outgoing.values():
			result.update(second_map.values())	
		return result

	def get_edge(self,u,v):
		return self._ougoing[u].get(v)

	def degree(self,v,outgoing = True):
		if outgoing:
			return len(self._outgoing[v])
		else:
			return len(self._incoming[v])

	def incident_edges(self,v,outgoing = Tree):
		adj = self._outgoing if outgoing else self._incoming
		for edge in adj[v].values():
			yield edge

	def insert_vertex(self,x=None):
		v = self.Vertex(x)
		self._outgoing[v] = {}
		if self.is_directed():
			self.incoming = {}
		return v
	
	def insert_edge(self,u,v,x = None):
		e = self.Edge(u,v,x)
		self._outgoing[u][v] = e
		self._incoming[v][u] = e
		










'''
v = Vertex('dalla')
a = v.element()
print a

e = Edge('tapan','bohra',100)
print e.opposite('bohra')
print e.opposite('tapan')
print e.endpoints()
print e.elements()
'''
