
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
			return self._destination if self._origin else self._origin 
		def edges(self):
			return (self._origin,self._destination)

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

	def insert_edge(self,u,v,x):
		e = self.Edge(u,v,x)
		self._outgoing[u][v] = e
		self._incoming[v][u] = e

	def vertex_count(self):
		return len(self._outgoing)
	
	def vertices(self):
		return self._outgoing.keys()

	def edge_count(self):
		total = sum(len(self._outgoing[key]) for key in self._outgoing)
		return total if self.is_directed else total//2		
	def edges(self):
		result = set()
		for secmap in self._outgoing.values():
			result.update(secmap.values())
		return result

	def degree(self,v,outgoing=True):
		adj = self._outgoing if directed else self._incoming
		return len(adj[v])

	def getedge(self,u,v):
		return self._outgoing[u][v]

	def incident_edge(self,v,outgoing = True):
		adj = self._outgoing if outgoing else self._incoming
		for edge in adj[v]:
			yield edge

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



