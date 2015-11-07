

class Graph:
	def __init__(self,graph_dict = {}):
		self._graph_dict = {}
	def add_vertex(self,u):
		if u not in self._graph_dict.keys():
			self._graph_dict[u] = []
	def add_edge(self,edge):
		(vertex1,vertex2) = edge
		if vertex1 in self._graph_dict:
			self._graph_dict[vertex1].append(vertex2)
		else:
			self._graph_dict[vertex1] = [vertex2]
	def vertices(self):
		return list(self._graph_dict.keys())
	def edges(self):
		return self.generate_edges()
	def generate_edges(self):
		edges = []
		for vertex in self._graph_dict:
			for neighbor in self._graph_dict[vertex]:
				if [vertex,neighbor] not in edges:
					edges.append([vertex,neighbor])
					#edges.append([neighbor[0],[vertex,neighbor[1]]])
					edges.append([neighbor,vertex])

		return edges
	
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
		for k in self.generate_edges():
			if k[0] == u:
				dude.append(k)
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

g1 = Graph()
g1.add_vertex('a')
g1.add_vertex('b')
g1.add_vertex('c')
g1.add_vertex('d')
g1.add_vertex('e')
g1.add_vertex('f')
g1.add_vertex('g')
g1.add_vertex('z')

g1.add_edge(['a','b'])
g1.add_edge(['b','c'])
g1.add_edge(['c','d'])
g1.add_edge(['d','e'])
g1.add_edge(['a','f'])
#g1.add_edge(['f','g'])
g1.add_edge(['g','c'])
g1.add_edge(['z','b'])
g1.add_edge(['z','f'])
g1.add_edge(['z','g'])

print g1

print g.incident_edges('a')
disc = {}
def dfs(g,u,disc):
	for e in g.incident_edges(u):
		v = e[1][0]
		if v not in disc:
			disc[v] = e
			dfs(g,v,disc)

dfs(g1,'a',disc)
print disc


def construct_path(u,v,disc):
	path = []
	if v in disc:
		path.append(v)
		walk = v
		while walk is not u:
			e = disc[walk]		
			parent = e[0]
			path.append(parent)
			walk = parent
		path.reverse()
	return path

path = construct_path('a','b',disc)
print path

path = construct_path('a','c',disc)
print path

path = construct_path('a','d',disc)
print path

path = construct_path('a','d',disc)
print path

path = construct_path('a','e',disc)
print path

path = construct_path('a','f',disc)
print path

path = construct_path('a','z',disc)
print path

path = construct_path('a','g',disc)
print path




