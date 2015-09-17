
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
		if directed:
			self._incoming = {}

	def is_directed(self):
		if directed:
			return True
		else:
			return False

	def vertex_cout (self):
		return len(self._outgoing)

	def vertices(self):
		return self._outgoing.keys()

	def edge_cout(self):
		total = sum[len(self._outgoing[key]) for key in self._outgoing.keys()]
		if directed:
			return total
		else:
			return total//2
	







#check for vertex and edge

g = Graph()
v1 = g.Vertex("dalla")
v2 = g.Vertex("kutta")
v3 = g.Vertex("baniya")
v4 = g.Vertex("bohra")
print v1.element()
print v2.element()
print v3.element()
print v4.element()

e1 = g.Edge(v1,v2,10)
e2 = g.Edge(v1,v3,40)
e3 = g.Edge(v2,v4,20)
e4 = g.Edge(v3,v4,30)
print e1
print e2
print e3
print e4

# checking ends here

