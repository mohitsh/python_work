

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

#print g1
#print g.incident_edges('a')

disc = {}
def dfs(g,u,disc):
	for e in g.incident_edges(u):
		v = e[1][0]
		if v not in disc:
			disc[v] = e
			dfs(g,v,disc)

dfs(g1,'a',disc)
#print disc


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

def dfs1(g,u,disc):
	for e in g.incident_edges(u):
		v = e[1][0]
		if v not in disc:
			disc[v] = e
			dfs(g,v,disc)

disc = {}
dfs1(g1,'a',disc)
#print disc


def dfs2(g,u,disc):
	for e in g.incident_edges(u):
		v = e[1][0]
		if v not in disc:
			disc[v] = e	
			dfs2(g,v,disc)
disc = {}
dfs2(g1,'a',disc)
#print disc

def construct_path1(u,v,disc):
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

#print construct_path1('a','g',disc)	

def path(u,v,disc):
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

#print path('a','e',disc)

g2 = Graph()

g2.add_vertex('a')
g2.add_vertex('b')
g2.add_vertex('c')
g2.add_vertex('d')
g2.add_vertex('e')
g2.add_vertex('g')
g2.add_vertex('j')
g2.add_vertex('k')
g2.add_vertex('i')
g2.add_vertex('m')
g2.add_vertex('p')

g2.add_edge(['a','b'])
g2.add_edge(['a','c'])
g2.add_edge(['c','d'])
g2.add_edge(['b','d'])
g2.add_edge(['b','g'])
g2.add_edge(['d','e'])
g2.add_edge(['e','g'])
g2.add_edge(['e','j'])
g2.add_edge(['j','k'])
g2.add_edge(['g','k'])
g2.add_edge(['g','i'])
g2.add_edge(['k','m'])
g2.add_edge(['i','m'])
g2.add_edge(['i','p'])

disc = {}
dfs(g2,'a',disc)
#print path('a','p',disc)

# forest 

def dfs_complete(g):
	forest = {}
	for u in g.vertices():
		if u not in forest:
			forest[u] = None
			dfs(g,u,forest)
	return forest

#print "forest: "
#print dfs_complete(g2)	


# cycle detection

for key1 in disc:
	for key2 in disc:
		if disc[key1] == [disc[key2][1],disc[key2][0]]:
			#print disc[key1],disc[key2]
			break


def bfs(g,s,disc):
	level = [s]
	while len(level) > 0:
		next_level = []
		for u in level:
			for e in g.incident_edges(u):
				v = e[1]
				if v not in disc and v != s:
					disc[v] = e
					next_level.append(v)
		level = next_level

g3 = Graph()

g3.add_vertex('a')
g3.add_vertex('b')
g3.add_vertex('c')
g3.add_vertex('d')
g3.add_vertex('e')
g3.add_vertex('f')
g3.add_vertex('g')
g3.add_vertex('h')
g3.add_vertex('i')

g3.add_edge(['a','b'])
g3.add_edge(['b','c'])
g3.add_edge(['a','d'])
g3.add_edge(['d','e'])
g3.add_edge(['e','f'])
g3.add_edge(['f','c'])
g3.add_edge(['d','g'])
g3.add_edge(['g','h'])
g3.add_edge(['h','i'])
g3.add_edge(['b','e'])
g3.add_edge(['e','h'])
g3.add_edge(['f','i'])


"after BFS: "
disc = {}
bfs(g3,'a',disc)
print disc

#print g3.incident_edges('e')













