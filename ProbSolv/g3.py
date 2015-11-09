
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
		return list(self._graph_dict.keys())
	
	def edges(self):
		return self.generate_edges()

	def generate_edges(self):
		edges = []
		for vertex in self._graph_dict:
			for neighbor in self._graph_dict[vertex]:
				if [vertex,neighbor] not in edges:
					edges.append([vertex,neighbor])
					#edges.append([neighbor,vertex])

		return edges
	
	def incident_edges(self,u):
		dude = []
		for k in self.generate_edges():
			if k[0] == u:
				dude.append(k)

		return dude

	def __str__(self):
		res = "vertices: " 
		for k in self._graph_dict.keys():
			res += str(k) + " "
		res += "\nedges: "
		for k in self.generate_edges():
			res += str(k) + " "

		return res

	def get_edge(self,u,v):
		for e in self.incident_edges(u):
			if e[1] == v:
				return e

g = Graph()
g.add_vertex('a')
g.add_vertex('b')
g.add_vertex('c')
g.add_vertex('d')

g.add_edge(['a','b'])
g.add_edge(['a','d'])
g.add_edge(['a','c'])
#g.add_edge(['c','b'])
g.add_edge(['c','d'])
#g.add_edge(['c','f'])
#g.add_edge(['c','e'])
#g.add_edge(['e','p'])
#g.add_edge(['e','q'])
#g.add_edge(['p','x'])
#g.add_edge(['p','y'])
g.add_edge(['b','d'])
g.add_edge(['d','e'])
g.add_edge(['b','e'])
g.add_edge(['e','f'])

def dfs(g,u,disc):
	for e in g.incident_edges(u):
		v = e[1]
		if v not in disc:
			disc[v] = e
			dfs(g,v,disc)

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
"""
	
disc = {}
dfs(g,'a',disc)
print disc

disc = {}
bfs(g,'a',disc)
print disc

"""

def bfs(g,s,disc):
	level = [s]	
	while len(level) > 0:
		next_level = []
		for u in level:
			for e in g.incident_edges(u):
				v = e[1]
				if v not in disc:
					disc[v] = e
					next_level.append(v)
		level = next_level
"""	
disc = {}
bfs(g,'a',disc)
print "Call bfs: "
for key in disc:
	print key, disc[key]
"""


def dfs(g,u,disc):
	for e in g.incident_edges(u):
		v = e[1]
		if v not in disc:
			disc[v] = e
			dfs(g,v,disc)

"""
disc = {}
dfs(g,'a',disc)
print "Call dfs: "
for key in disc:
	print key,disc[key]
"""


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


def dfs11(g,u,disc):
	for e in g.incident_edges(u):
		v = e[1]
		if v not in disc:
			disc[v] = e
			dfs11(g,v,disc)

def bfs11(g,s,disc):
	level = [s]
	while len(level) > 0:
		next_level = []
		for u in level:
			for e in g.incident_edges(u):
				v = e[1]
				if v not in disc:
					disc[v] = e
					next_level.append(v)
		level = next_level

def path11(u,v,disc):
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

"""
disc = {}
dfs11(g,'a',disc)
print "Call dfs: "
for key in disc:
        print key,disc[key]

print path11('a','y',disc)

disc = {}
bfs11(g,'a',disc)
print "Call bfs: "
for key in disc:
        print key,disc[key]

print path11('a','y',disc)
"""

# floyd warshall gets you all the paths in graph
import copy

def floyd_warshall(g):
	closure = copy.deepcopy(g)
	verts = list(closure.vertices())
	n = len(verts)
	for k in range(n):
		for i in range(n):
			if i!=k and closure.get_edge(verts[i],verts[k]) is not None:
				for j in range(n):
					if i!=j!=k and closure.get_edge(verts[k],verts[j]) is not None:
						if closure.get_edge(verts[i],verts[j]) is None:
							closure.add_edge([verts[i],verts[j]])
	return closure

print floyd_warshall(g)


def floydWarshall1(g):
	closure = copy.deepcopy(g)
	verts = g.vertices()
	n = len(verts)
	for k in range(n):
		for i in range(n):
			# edge i to k exists
			if i!=k and closure.get_edge(verts[i],verts[k]) is not None:
				for j in range(n):
					# edge k to j exists
					if i!=j!=k and closure.get_edge(verts[k],verts[j]) is not None:
						# edge i to j
						if closure.get_edge(verts[i],verts[j]) is None:
							closure.add_edge([verts[i],verts[j]])
	return closure

print floydWarshall1(g)



def floydWarshall2(g):
	closure = copy.deepcopy(g)
	verts = g.vertices()
	n = len(verts)
	for k in range(n):
		for i in range(n):
			if i!=k and closure.get_edge(verts[i],verts[k]) is not None:
				for j in range(n):
					if i!=j!=k and closure.get_edge(verts[k],verts[j]) is not None:
						if closure.get_edge(verts[i],verts[j]) is None:
							closure.add_edge([verts[i],verts[j]])
	return closure

print floydWarshall2(g)

def floydWarshall3(g):
	closure = copy.deepcopy(g)
	verts = closure.vertices()
	n = len(verts)
	for k in range(n):
		for i in range(n):
			if i!=k and closure.get_edge(verts[i],verts[k]) is not None:
				for j in range(n):
					if i!=j!=k and closure.get_edge(verts[k],verts[j]) is not None:
						if closure.get_edge(verts[i],verts[j]) is None:
							closure.add_edge([verts[i],verts[j]])
	return closure

print floydWarshall3(g)



















































































































