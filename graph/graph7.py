
class Graph:
	
	class Vertex:
		def __init__(self,x):
			self._element = x;
		
		def element(self):
			return self._element

		def __str__(self):
			return str(self._element)

	class Edge:
		def __init__(self,u,v,x):
			self._origin = u
			self._destination = v
			self._element = x

		def endpoints(self):
			return (self._origin, self_destination)

		def opposite(self,u):
			return self._destination if u is self._origin else self._origin 
			
		def element(self):
			return self._element

		def __str__(self):
			return '({},{},{})'.format(self._origin,self._destination,self._element)
	
	def __init__(self,directed=False):
		self._outgoing = {}
		self.directed = directed
		if directed:
			self._incoming = {}

	def is_directed(self):
		if self.directed:
			return True
		else:
			return False

	def vertex_count (self):
		return len(self._outgoing)

	def vertices(self):
		return self._outgoing.keys()

	def edge_count(self):
		total = sum(len(self._outgoing[i]) for i in self._outgoing)
		#total = sum(len(self._outgoing[v]) for v in self._outgoing)
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
		return self._outgoing.get(u).get(v)

	def degree(self,v,outgoing = True):
		if outgoing:
			return len(self._outgoing[v])
		else:	
			return len(self._outgoing[v])

	def incident_edges(self,v,outgoing=True):
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
		if self.is_directed():
			self._incoming[v][u] = e



#check for vertex and edge

g = Graph(directed=False)
v1 = g.insert_vertex("dalla")
v2 = g.insert_vertex("kutta")
v3 = g.insert_vertex("baniya")
v4 = g.insert_vertex("bohra")


e1 = g.insert_edge(v1,v2,10)
e2 = g.insert_edge(v1,v3,40)
e3 = g.insert_edge(v2,v4,20)
e4 = g.insert_edge(v3,v4,30)

# checking ends here
print g.is_directed()
print g.vertex_count()
vert  = g.vertices()

for k in vert:
	print k
print g.edge_count()
edges = g.edges()
for k in edges:
	print k
