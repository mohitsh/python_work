

class Vertex:
	
	__slots__ = '_elements'
	
	def __init__(self,x):
		self._element = x
	
	def element(self):
		return self._element

	def __hash__(self):
		return hash(id(self))

	
class Edge:
	
	__slots__ = '_origin', '_destination', '_element'
	
	def __init__(self,u,v,x):
		self._origin = u
		self._destination = v
		self._element = x
		
	def endpoints(self):
		return (self._origin, self.destination)
