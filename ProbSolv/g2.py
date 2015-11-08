
class Graph:
	
	def __init__(self,graph_dict = {}):
		self._graph_dict = graph_dict

	def add_vertex(self,vertex):
		if vertex not in self._graph_dict:
			self._graph_dict[vertex] = []
	
	def add_edge(self,edge):
		(vertex1,vertex2) = edge
		if vertex1 in self._graph_dict:
			self._graph_dict[vertex1].append(vertex2)
		else:
			self._graph_dict[vertex1] = [vertex2]
	
	def vertices(self):
		return list(self._graph_dict)
	
	def edges(self):
		return self.generate_edges()

	def generate_edges(self):
		edges = []
		for vertex in self._graph_dict:
			for neighbor in self._graph_dict[vertex]:
				if [vertex,neighbor] not in edges:
					edges.append([vertex,neighbor])
					edges.append([neighbor,vertex])

		return edges

	def __str__(self):
		res = "vertices: " 
		for k in self._graph_dict:
			res += str(k) + " " 
		res += "\nedges: "
		for k in self.generate_edges():
			res += str(k) + " "
		return res

	
	def incident_edges(self,u):
		dude = []
		for k in self.generate_edges():
			if k[0] == u:
				dude.append(k)
		return dude

g = Graph()
g.add_vertex('a')
g.add_vertex('b')
g.add_vertex('c')
g.add_vertex('d')

g.add_edge(['a','b'])
g.add_edge(['a','d'])
g.add_edge(['a','c'])
g.add_edge(['c','b'])
g.add_edge(['c','d'])

print g





