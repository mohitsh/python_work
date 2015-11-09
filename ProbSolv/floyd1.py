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

def bfs(g,s,disc):
	level = [s]
	while len(level) > 0:
		next_level = []
		for u in level:
			for e in g.incident_edges(u):
				v = e[1][0]
				if v not in disc:
					disc[v] = e
					next_level.append(v)
		level = next_level

def path(u,v,disc):
	path = []
	if v in disc:
		#path.append(v)
		walk = v
		while walk is not u:
			e = disc[walk]
			parent = e[0]
			path.append(e[1][1])
			walk = parent
	path.reverse()
	return path
			
"""
g = Graph()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
#g.add_vertex(5)
#g.add_vertex(6)
#g.add_vertex(7)

g.add_edge([1,[2,5]])
g.add_edge([1,[4,24]])
g.add_edge([2,[4,6]])
g.add_edge([3,[2,7]])
g.add_edge([3,[4,4]])
#g.add_edge([3,[5,1]])
#g.add_edge([5,[6,1]])
#g.add_edge([5,[7,1]])
"""
#tc = floyd_warshall(g)
#dude =  tc.generate_edges()

start = 1
end = 4

def find(dude,start,end):
	flag = -1
	for i in dude:
		for j in dude:
			if i[0] == start and j[1][0] == end:
				Flag = 1
				return [i[0],j[1][0]]
	return flag

#print find(dude,start,end)
disc = {}
#bfs(g,3,disc)
#for key in disc:
#	print "vertex: ", key, "edge: ", disc[key]		
		
#print sum(path(1,2,disc))
#if sum(path(3,1,disc)) == 0:
	#print -1
#print sum(path(1,4,disc))

g = Graph()

n_e = raw_input().split()
n,e = [int(x) for x in n_e]
for i in range(e):
	inp = raw_input().split()
	v1,v2,e = [int(x) for x in inp]
	g.add_vertex(v1)
	g.add_vertex(v2)
	g.add_edge([v1,[v2,e]])
		
#print g

tc = floyd_warshall(g)
dude =  tc.generate_edges()
#print dude

q = int(raw_input())
for i in range(q):
        inp = raw_input().split()
        v1,v2 = [int(x) for x in inp]
	ans = find(dude,v1,v2)
	if ans == -1:
		print ans
	else:
		disc = {}
		bfs(g,v1,disc)
		direct = path(v1,v2,disc)
		print sum(direct)




