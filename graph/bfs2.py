

class Graph:
	class Vertex:	
		def __init__(self,x):
			self._element = x
		def __str__(self):
			return str(self._element)

	class Edge:
		def __init__(self,u,v,x):
			self._origin = u
			self._destination = v
			self._element = x
		def opposite(self,u):
			return self._destination if u is self._origin else self._origin 
		
		def __str__(self):
			return '({0},{1},{2})'.format(self._origin,self._destination,self._element)		
	
	def __init__(self,directed = False):
		self._outgoing = {}
		self._incoming = {} if directed else self._outgoing
	
	def is_directed(self):
		return self._incoming is not self._outgoing

	def insertVertex(self,x):
		v = self.Vertex(x)
		self._outgoing[v] = {}
		if self.is_directed():
			self._incoming = {}
		return v	
	def insertEdge(self,u,v,x=6):
		e = self.Edge(u,v,x)
		self._outgoing[u][v] = e
		self._incoming[v][u] = e

	def incident_edge(self,u,outgoing = True):
		adj = self._outgoing if outgoing else self._incoming
		for edge in adj[u].values():
			yield edge

	def vertices(self):
		return self._outgoing.keys()
	
	def edges(self):
		result = set()
		for secmap in self._outgoing.values():
			result.update(secmap.values())
		return result

g = Graph()

a = g.insertVertex("a")
b = g.insertVertex("b")
c = g.insertVertex("c")
d = g.insertVertex("d")
e = g.insertVertex("e")
f = g.insertVertex("f")
gg = g.insertVertex("g")
h = g.insertVertex("h")

e1 = g.insertEdge(a,e)
e2 = g.insertEdge(a,f)
e3 = g.insertEdge(a,b)
e4 = g.insertEdge(b,f)
e5 = g.insertEdge(b,c)
e6 = g.insertEdge(c,gg)
e7 = g.insertEdge(c,d)
e8 = g.insertEdge(gg,d)
e9 = g.insertEdge(d,h)
e11 = g.insertEdge(e,f)
e12 = g.insertEdge(b,h)

def bfs(g,s,dic):
	level = [s]
	while len(level) > 0:
		next_level = []
		for u in level:
			for e in g.incident_edge(u):
				v = e.opposite(u)
				if v not in dic:
					dic[v] = e
					next_level.append(v)
		level = next_level
	return dic

def bfs1(g,s,dic):
	level = [s]
	while len(level) > 0:
		next_level = []
		for u in level:
			for e in g.incident_edge(u):
				v = e.opposite(u)
				if v not in dic:
					dic[v] = e
					next_level.append(v)
		level = next_level
	return dic
def construct_path(u,v,dic):
	path = []
	if v in dic:
		path.append(v)
		walk = v
		while walk is not u:
			#print "here"
			e = dic[walk]
			parent = e.opposite(walk)
			path.append(parent)
			walk = parent
		path.reverse()
	return path

print "beware! bfs is running"
dic = {}
result = bfs1(g,a,dic)
for key in result:
	print key,dic[key],dic[key].opposite(key)

print "Behold! this is path"
path = construct_path(a,h,result)
for v in path:
	print v





































