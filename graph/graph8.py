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
		self._incoming = {} if directed else self_outgoing

	def is_directed:
		return self._incoming is not self._outcoming

	def vertex_count(self):
		return len(self._outgoing)

	def vertices(self):
		return self._outgoing.keys()

	def edge_count(self):
		total = sum(len(self._outgoing[v]) for v in self._outgoing)
		if is_directed():
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
		adj = self._outgoing if outgoing else self._incomingg
		return len(adj[v])

	def incident_edges(self,v,outgoing = True):
		adj = self._outgoing if outgoing else self._incoming
		for edge in adj[v]:
			yield edge

		
