
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
	def out_degree(self,u):
		count = 0
		for e in self.generate_edges():
			if e[0] == u:
				count += 1
		return count
	
	def in_degree(self,u):
		count = 0
		for e in self.generate_edges():
			if e[1][0] == u:
				count += 1
		return count

			
"""
g = Graph()
g.add_vertex('v1')
g.add_vertex('v2')
g.add_vertex('v3')
g.add_vertex('v4')
g.add_vertex('v5')
g.add_vertex('v6')
g.add_vertex('v7')

g.add_edge(['v1',['v4',1]])
g.add_edge(['v1',['v5',1]])
g.add_edge(['v1',['v7',1]])
g.add_edge(['v4',['v5',1]])
g.add_edge(['v3',['v4',1]])
g.add_edge(['v3',['v5',1]])
g.add_edge(['v2',['v3',1]])
g.add_edge(['v2',['v5',1]])
g.add_edge(['v2',['v6',1]])
g.add_edge(['v6',['v7',1]])
g.add_edge(['v5',['v6',1]])
g.add_edge(['v5',['v7',1]])
"""


def topological_sort(g):
	topo = []
	ready = []
	incount = {}
	
	for u in g.vertices():
		incount[u] = g.in_degree(u)
		if incount[u] == 0:
			ready.append(u)
	while len(ready) > 0:
		u = ready.pop()
		topo.append(u)
		for e in g.incident_edges(u):
			v = e[1][0]
			incount[v] -= 1
			if incount[v] == 0:
				ready.append(v)
	return topo

#print topological_sort(g)

g1 = Graph()
g1.add_vertex("underpants")
g1.add_vertex("pants")
g1.add_vertex("belt")
g1.add_vertex("socks")
g1.add_vertex("shoes")
g1.add_vertex("shirt")
g1.add_vertex("tie")
g1.add_vertex("jacket")

g1.add_edge(["underpants",["pants",1]])
g1.add_edge(["pants",["belt",1]])
g1.add_edge(["belt",["jacket",1]])
g1.add_edge(["underpants",["shoes",1]])
g1.add_edge(["socks",["shoes",1]])
g1.add_edge(["pants",["shoes",1]])
g1.add_edge(["shirt",["belt",1]])
g1.add_edge(["shirt",["tie",1]])
g1.add_edge(["tie",["jacket",1]])

print topological_sort(g1)





