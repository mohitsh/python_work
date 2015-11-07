
class Graph:
	def __init__(self,graph_dict = {}):
		self._graph_dict = graph_dict
	def vertices(self):
		return list(self._graph_dict.keys())
	def edges(self):
		return self.generate_edges()
	def generate_edges(self):
		edges = []
		for vertex in self._graph_dict:
			for neighbor in self._graph_dict[vertex]:
				if [neighbor,vertex] not in edges:
					edges.append([vertex,neighbor])
					edges.append([neighbor[0],[vertex,neighbor[1]]])
		return edges
	def add_vertex(self,vertex):
		if vertex not in self._graph_dict:
			self._graph_dict[vertex] = []
	def add_edge(self,edge):
		(vertex1, vertex2) = edge
		if vertex1 in self._graph_dict:
			self._graph_dict[vertex1].append(vertex2)
		else:
			self._graph_dict[vertex1] = [vertex2]
	def __str__(self):
		res = "vertices: " 
		for k in self._graph_dict:
			res += str(k) + " "
		res += "\nedges"
		for edge in self.generate_edges():
			res += str(edge) + " " 
		return res
	def incident_edges(self,u):
		dude = []
		edges = self.generate_edges()
		for e in edges:
			if e[0] == u:
				dude.append(e)
		return dude
		

g = Graph()
g.add_vertex('a')
g.add_vertex('b')
g.add_vertex('c')
g.add_vertex('d')
g.add_vertex('e')
g.add_vertex('f')

g.add_edge(['a',['b',3]])
g.add_edge(['a',['f',5]])
g.add_edge(['a',['e',6]])
g.add_edge(['b',['f',4]])
 
g.add_edge(['b',['c',1]])
g.add_edge(['c',['f',4]])
g.add_edge(['c',['d',6]])
g.add_edge(['d',['e',8]])

g.add_edge(['d',['f',5]])
g.add_edge(['e',['f',2]])

start = 'a'
v = g.vertices()
length = len(v)

verts = g.incident_edges('b')
minim = verts[0][1][1]
for k in verts:
	print k
	if k[1][1] < minim:
		minim = k[1]

print minim
	



