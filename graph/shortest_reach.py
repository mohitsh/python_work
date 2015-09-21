

class Graph:
	class Vertex:
		def __init__(self,x):
			self._element = x
		def __str__(self):
			return str(self._element)
	class Edge:
		def __init__(self,u,v,x):
			self._origin  = u
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
			self._incoming[v] = {}
		return v	
	
	def insertEdge(self,u,v,x=6):
		e = self.Edge(u,v,x)
		self._outgoing[u][v] = e
		self._incoming[v][u] = e

	def incident_edges(self,u,outgoing = True):
		adj = self._outgoing if outgoing else self._incoming
		for edge in adj[u].values():
			yield edge
	def vertices(self):
		return self._outgoing.keys()
	def edges(self):
		result = set()
		for sec_map in self._outgoing.values():
			result.update(sec_map.values())
		return result

def bfs(g,s,dic):
        level = [s]
        while len(level) > 0:
                next_level = []
                for u in level:
                        for e in g.incident_edges(u):
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


g = Graph()

k = int(raw_input())
for i in range(k):
	n_m1 = raw_input().split()
	n_m = [int(x) for x in n_m1]
	store = {}
	for i in range(1,n_m[0]+1):
		store[i] = g.insertVertex(str(i))
	for j in range(n_m[1]):
		edge1 = raw_input().split()
		edge = [int(x) for x in edge1]
		g.insertEdge(store[edge[0]],store[edge[1]])
	

	start = int(raw_input())
	dic = {}
	dude = bfs(g,store[start],dic)
	ans = []
	for key in store:
		
		if key != start:
			path = construct_path(store[start],store[key],dude)
			if len(path) == 0:
				ans.append(-1)
			else:
				ans.append(6*(len(path)-1))
	print ' ' .join(str(x) for x in ans)
					
		


'''
vert = g.vertices()
print "vertices"
for k in vert:
        print k

edge = g.edges()
print "edges"
for k in edge:
        print k
'''
