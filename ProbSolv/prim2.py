
class Graph:
	def __init__(self,graph_dict = {}):
		self._graph_dict = graph_dict
	def vertices(self):
		return list(self._graph_dict.keys())
	def edges(self):
		return self._generate_edges()
	def _generate_edges(self):
		edges = []
		for vertex in self._graph_dict:
			for neighbor in self._graph_dict[vertex]:
				if {neighbor,vertex} not in edges:
					edges.append({vertex, neighbor})
		return edges

	def add_vertex(self,vertex):
		if vertex not in self._graph_dict:
			self._graph_dict[vertex] = []
	def add_edge(self,edge):
		#edge = set(edge)
		(vertex1,vertex2) = tuple(edge)
		if vertex1 in self._graph_dict:
			self._graph_dict[vertex1].append(vertex2)
		else:
			self._graph_dict[vertex1] = [vertex2]	
	def __str__(self):
		res = "vertices: "
		for k in self._graph_dict:
			res += str(k) + " " 
		res += "\nedges: "
		for edge in self._generate_edges():
			res += str(edge) + " " 
		return res


g = Graph()
g.add_vertex("a")
g.add_vertex("b")
g.add_vertex("c")
g.add_vertex("d")
g.add_vertex("e")
g.add_vertex("f")

#print g.vertices()
	
g.add_edge(['a','d'])
g.add_edge(['d','c'])
g.add_edge(['c','c'])
g.add_edge(['c','b'])
g.add_edge(['c','e'])

#print g.edges()
print g


	
