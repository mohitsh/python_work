

	
class Graph:

	class Vertex:
	
		__slots__ = '_elements'
	
		def __init__(self,x):
			self._element = x
	
		def element(self):
			return self._element
	
		def __hash__(self):
			return hash(id(self))
		def __str__(self):
			return str(self._element)
	
	class Edge:
	
		__slots__ = '_origin', '_destination', '_element'
	
		def __init__(self,u,v,x):
			self._origin = u
			self._destination = v
			self._element = x
		
		def endpoints(self):
			return (self._origin, self._destination)

		def opposite(self,v):
			if v is self._origin:
				return self._destination
			else:
				return self._origin

		def element(self):
			return self._element

		def __hash__(self):
			return hash((self._origin, self._destination))

		def __str__(self):
			return str(self._element)		



	def __init__(self, directed = False):
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
		return total if self.is_directed else total//2

	def edges(self):
		result = set()
		for secondry_map in self._outgoing.values():
			result.update(secondry_map.values())
		return result

	def get_edges(self,u,v):
		return self._outgoing[u].get(v)
		
	def degree(self,v,outgoing=True):
		adj = self._outgoing if outgoing else self._incoming
		return len(adj[v])
	
	def incident_edges(self,v,outgoing = True):
		adj = self._outgoing if outgoing else self._incoming
		for edge in adj[v].values():
			yield edge

	def insert_vertex(self,x=None):
		v = self.Vertex(x)
		self._outgoing[v] = {}
		if self.is_directed():
			self._incoming[v] = {}
		return v

	def insert_edge(self,u,v,x=None):
		e = self.Edge(u,v,x)
		self._outgoing[u][v] = e
		self._incoming[v][u] = e


g = Graph()
print g.is_directed()
print g.vertex_count()
print g.vertices()
vert1 = g.insert_vertex('a')
vert2 = g.insert_vertex('b')
print g.vertex_count()
g.insert_edge(vert1,vert2,100)
print g.get_edges(vert1,vert2)
print g.degree(vert1)
print g.degree(vert2)
print g.get_edges(vert1,vert2)
endpoints = g.get_edges(vert1,vert2).endpoints()
for e in endpoints:
	print 'endpoints', e

vert =  g.vertices()
for e in vert:
	print e


def DFS(g,u,discovered):
	
	for e in g.incident_edges(u):
		v = e.opposite(u)
		if v not in discovered:
			discovered[v] = e
			DFS(g,v,discovered)
		















